from . search_classes import SearchRequest, sort_and_analyze, search_cat_url

search_cat_request_params = {"size": "", "format": "", "order": "",
                             "page": "", "limit": "", "mime_types": ""
                             }


def test_search_without_params():
    empty_params = {
        "size": "",
        "format": "",
        "order": "",
        "page": "",
        "limit": "",
        "mime_types": ""
    }
    without_param_response = SearchRequest(search_cat_url, empty_params).make_request_for_json()
    assert len(without_param_response) == 1


def test_non_valid_params():
    invalid_params = {
        "size": "8673409856745986735098673458906735409867345098654376095834753670985673406874",
        "format": "0,12323123132414214123120942380923840237498234723984623874623746",
        "order": "Взять всех живьем!",
        "page": "True",
        "limit": "-2",
        "mime_types": "null"
    }
    invalid_params_response = SearchRequest(search_cat_url, invalid_params).make_request_for_json()
    assert len(invalid_params_response) == 1


def test_out_of_max_limit():
    out_of_max = {
        "size": "",
        "format": "",
        "order": "",
        "page": "",
        "limit": "26",
        "mime_types": "gif"
    }
    out_of_max_response = SearchRequest(search_cat_url, out_of_max).make_request_for_json()
    assert len(out_of_max_response) == 25


def invalid_page_number():
    testcase = {
        "size": "medium",
        "format": "src",
        "order": "desc",
        "page": "20",
        "limit": "15",
        "mime_types": "gif",
    }
    param_response = SearchRequest(search_cat_url, testcase).make_request_for_json()
    assert len(param_response) == str(testcase["limit"])


def test_tescase_01():
    testcase = {
        "size": "small",
        "format": "json",
        "order": "random",
        "page": "1",
        "limit": "1",
        "mime_types": "gif"
    }
    sort_and_analyze(testcase)


def test_testcase_02():
    testcase = {
        "size": "small",
        "format": "src",
        "order": "random",
        "page": "8",
        "limit": "12",
        "mime_types": "png",
    }
    sort_and_analyze(testcase)


def test_testcase_03():
    testcase = {
        "size": "small",
        "format": "",
        "order": "desc",
        "page": "",
        "limit": "9",
        "mime_types": "jpg",
    }
    sort_and_analyze(testcase)


def test_testcase_04():
    testcase = {
        "size": "small",
        "format": "",
        "order": "",
        "page": "",
        "limit": "10",
        "mime_types": "",
    }
    sort_and_analyze(testcase)


def test_testcase_05():
    testcase = {
        "size": "medium",
        "format": "",
        "order": "",
        "page": "3",
        "limit": "11",
        "mime_types": "png",
    }
    sort_and_analyze(testcase)


def test_testcase_06():
    testcase = {
        "size": "medium",
        "format": "",
        "order": "random",
        "page": "6",
        "limit": "6",
        "mime_types": "jpg",
    }
    sort_and_analyze(testcase)


def test_testcase_07():
    testcase = {
        "size": "medium",
        "format": "json",
        "order": "asc",
        "page": "",
        "limit": "7",
        "mime_types": "",
    }
    sort_and_analyze(testcase)


def test_testcase_08():
    testcase = {
        "size": "medium",
        "format": "src",
        "order": "desc",
        "page": "",
        "limit": "15",
        "mime_types": "gif",
    }
    sort_and_analyze(testcase)


def test_testcase_09():
    testcase = {
        "size": "full",
        "format": "json",
        "order": "desc",
        "page": "10",
        "limit": "15",
        "mime_types": "gif",
    }
    sort_and_analyze(testcase)


def test_testcase_10():
    testcase = {
        "size": "full",
        "format": "src",
        "order": "desc",
        "page": "8",
        "limit": "17",
        "mime_types": "",
    }
    sort_and_analyze(testcase)


def test_testcase_11():
    testcase = {
        "size": "full",
        "format": "",
        "order": "random",
        "page": "",
        "limit": "18",
        "mime_types": "gif",
    }
    sort_and_analyze(testcase)


def test_testcase_12():
    testcase = {
        "size": "full",
        "format": "",
        "order": "asc",
        "page": "",
        "limit": "19",
        "mime_types": "png",
    }
    sort_and_analyze(testcase)


def test_testcase_13():
    testcase = {
        "size": "thumb",
        "format": "",
        "order": "asc",
        "page": "3",
        "limit": "20",
        "mime_types": "",
    }
    sort_and_analyze(testcase)


def test_testcase_14():
    testcase = {
        "size": "thumb",
        "format": "",
        "order": "desc",
        "page": "5",
        "limit": "23",
        "mime_types": "gif",
    }
    sort_and_analyze(testcase)


def test_testcase_15():
    testcase = {
        "size": "thumb",
        "format": "json",
        "order": "",
        "page": "",
        "limit": "24",
        "mime_types": "png",
    }
    sort_and_analyze(testcase)


def test_testcase_16():
    testcase = {
        "size": "thumb",
        "format": "src",
        "order": "random",
        "page": "",
        "limit": "25",
        "mime_types": "jpg",
    }
    sort_and_analyze(testcase)
