from ansible import parse_title, query_api, parse_results, url, fields


def test_simple_title():
    """
    Test if a simple title is parsed correctly
    """
    test_string = "title \u2014 Ansible Documentation"
    assert ("title", "Ansible Documentation") == parse_title(test_string)


def test_full_title():
    """
    Test if a full title is parsed correctly
    """
    test_string = "title \u2013 subtitle \u2014 Ansible Documentation"
    assert ("title", "subtitle") == parse_title(test_string)


def test_odd_title():
    """
    Test if an odd title returns only the title
    """
    test_string = "And now to something completely different"
    assert (test_string, "") == parse_title(test_string)


def test_query_wrong_api():
    """
    Test whether a wrong url results in an error
    """
    url = "https://search-api.swiftype.com/api/v1/public/installs/test/search.json"
    assert "error" in query_api(url, "test")[0]


def test_query_api_result_length():
    """
    Test if the ansible swiftype api returns a dictionary containing paged records
    """
    result = query_api(url, "test")
    assert len(result) == 10


def test_query_api_result_fields():
    """
    Test if the swiftype api returns the expected fields
    """
    # Pick the first result and test for all fields
    result = query_api(url, "test")[0]
    assert all(field in result.keys() for field in fields)


def test_parse_results_error():
    """
    Test if parse_results returns a script filter json message containing the error
    """
    error_result = [{"error": "test"}]
    assert [{"title": "Error",
             "subtitle": "test",
             "valid": False}] == parse_results(error_result)


def test_parse_results_empty():
    """
    Test if parse_results returns an empty response for an empty list
    """
    assert [] == parse_results({})


def test_parse_results_valid():
    """
    Test if a valid result is correctly parsed and returned in script filter json
    """
    valid_result = [{
        "url": "https://docs.ansible.com/ansible/.../test.html",
        "sections": ["test"],
        "title": "title – subtitle — Ansible Documentation",
        "body": "Long body containing flavor text",
        "_index": "5693d1e68db231f24d000003",
        "_type": "5693d1e68db231f24d000004",
        "_score": 1,
        "_version": "",
        "_explanation": "",
        "sort": "",
        "id": "test",
        "highlight": {}
    }]
    assert [{"title": "title",
             "subtitle": "subtitle",
             "arg": "https://docs.ansible.com/ansible/.../test.html",
             "valid": True}] == parse_results(valid_result)
