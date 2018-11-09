import requests
from PIL import Image

from . settings import image_sizes

search_cat_url = "https://api.thecatapi.com/v1/images/search"


class CatCard(object):
    size = ""
    mime_type = ""


class ExpectedCatCard(CatCard):
    """this is the description of the photo that the user expects to receive.
    Based on the parameters of the user request json converted to dict"""
    picture_max_height = 0
    picture_min_height = 0
    picture_max_width = 0
    picture_min_width = 0

    def __init__(self, search_request_params):
        self.size = search_request_params["size"]
        if self.size == '':
            self.size = 'med'
        if self.mime_type == '':
            self.mime_type = 'JPEG'
        if search_request_params["mime_types"] == 'jpg':
            self.mime_type = 'JPEG'
        if search_request_params["mime_types"] == 'png':
            self.mime_type = 'PNG'
        if search_request_params["mime_types"] == 'gif':
            self.mime_type = 'GIF'

    def params_init(self):
        self.picture_max_height = image_sizes[self.size]["max_height"]
        self.picture_min_height = image_sizes[self.size]["min_height"]
        self.picture_min_width = image_sizes[self.size]["min_width"]
        self.picture_max_width = image_sizes[self.size]["max_width"]


class ActualCatCard(CatCard):
    """contains the parameters of the image that the user received on
    their request. Download & analyze the image by the 'picture_dissection'"""
    cat_picture = ''
    picture_width = 0
    picture_height = 0

    def picture_dissection_from_url(self, picture_url):
        try:
            get_picture = requests.get(picture_url)
        except Exception:
            raise ConnectionError('Unable to download picture')
        out = open('./picture', "wb")
        out.write(get_picture.content)
        out.close()
        self.cat_picture = Image.open('./picture')
        self.mime_type = self.cat_picture.format
        (self.picture_width, self.picture_height) = self.cat_picture.size

    def picture_dissection_from_request(self, img_request):
        out = open('./picture' + self.mime_type, "wb")
        out.write(img_request.content)
        out.close()
        self.cat_picture = Image.open('./picture' + self.mime_type)
        (self.picture_width, self.picture_height) = self.cat_picture.size
        self.mime_type = self.cat_picture.format


class SearchRequest(object):
    querystring = {}
    url = ""
    headers = {
        'Content-Type': "application/json",
        'x-api-key': "1d6102aa-adb0-4e4a-ac50-14f1b71b0720",
        'cache-control': "no-cache",
        'Postman-Token': "01368fa0-54ba-470e-b4ad-2401f4d8fe30"
    }

    def __init__(self, address, params):
        self.querystring = params
        self.url = address

    def make_request_for_json(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        return response.json()

    def make_request_for_src(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        return response


def sort_and_analyze(params):
    expected_picture = ExpectedCatCard(params)
    expected_picture.params_init()
    actual_picture = ActualCatCard()
    if params["format"] == "src":
        param_response = SearchRequest(search_cat_url, params).make_request_for_src()
        actual_picture.picture_dissection_from_request(param_response)
        picture_assertion(expected_picture, actual_picture)
    else:
        param_response = SearchRequest(search_cat_url, params).make_request_for_json()
        assert len(param_response) == int(params["limit"])
        for i in range(len(param_response)):
            picture_url = (param_response[i])['url']
            actual_picture.picture_dissection_from_url(picture_url)
            picture_assertion(expected_picture, actual_picture)


def picture_assertion(expected_picture, actual_picture):
    if expected_picture.mime_type != actual_picture.mime_type:
        raise AssertionError(' - Wrong mime type! actual:' + actual_picture.mime_type + \
                             ' expected: ' + expected_picture.mime_type)
    elif actual_picture.picture_width < expected_picture.picture_min_width:
        raise AssertionError(' - Width lesser that minimal! width: ' + str(actual_picture.picture_width) \
                             + ' minimal: ' + str(expected_picture.picture_min_width))
    elif actual_picture.picture_height < expected_picture.picture_min_height:
        raise AssertionError('Height lesser that minimal! height: ' + str(actual_picture.picture_height) \
                             + ' minimal: ' + str(expected_picture.picture_min_height))
    elif actual_picture.picture_width > expected_picture.picture_max_width:
        raise AssertionError('Width bigger that maximal! width: ' + str(actual_picture.picture_width) \
                             + ' maximal: ' + str(expected_picture.picture_max_width))
    elif actual_picture.picture_height > expected_picture.picture_max_height:
        raise AssertionError('Height bigger that maximal! height: ' + str(actual_picture.picture_height) \
                             + ' height: ' + str(expected_picture.picture_max_height))

