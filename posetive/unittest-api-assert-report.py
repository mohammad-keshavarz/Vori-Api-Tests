import unittest
import requests


class TestAPI(unittest.TestCase):

    API_URL = "https://jsonplaceholder.typicode.com/posts/1"

    def test_check_status_code_200(self):
        print("\n===============================")
        print(f"Testing API: {self.API_URL}")
        print("===============================\n")

        # ارسال درخواست GET به API
        response = requests.get(self.API_URL)
        print(f"Received response with status code: {response.status_code}")
        print("\n--------------------------------\n")

       # 200
        try:
            self.assertEqual(response.status_code, 200, "Status code is not 200")
            print("✅ Status code is 200\n")
        except AssertionError as e:
            print(f"❌ {str(e)}\n")
            raise

        # tabdil
        unique_word = "tabdil"
        print(f"Checking if response contains the word: '{unique_word}'\n")

        if unique_word in response.text:
            print(f"✅ Found the word '{unique_word}' in the response!\n")
        else:
            print(f"❌ The word '{unique_word}' was not found in the response.\n")

        #  check responce have a unique message
        unique_phrase = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        print(f"Checking if response contains the unique phrase:\n\n'{unique_phrase}'\n")

        try:
            self.assertIn(unique_phrase, response.text, f"Response does not contain the unique phrase: {unique_phrase}")
            print("✅ Unique phrase is found in the response\n")
        except AssertionError as e:
            print(f"❌ {str(e)}\n")
            raise


if __name__ == "__main__":
    unittest.main()























































