import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def test_check_status_code_200():
    """Test if the API returns status code 200"""
    response = requests.get(API_URL)
    assert response.status_code == 200, "Status code is not 200"

def test_check_unique_phrase_in_response():
    """Test if the API response contains a unique phrase"""
    response = requests.get(API_URL)
    unique_phrase = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert unique_phrase in response.text, f"Response does not contain the unique phrase: {unique_phrase}"

def test_ckeck_word_tabdil_in_response():
    """Test if the API response contains the word 'tabdil'"""
    response = requests.get(API_URL)
    assert "tabdil" in response.text, "The word 'tabdil' was not found in the response"

# command-in-python terminal = pytest test_Api_vori_open-tabs_posetive.py --html=report.html --self-contained-html




