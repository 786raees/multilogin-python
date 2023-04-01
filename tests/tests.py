import unittest
from multilogin.client import MultiloginClient

# Replace this with your actual Multilogin API token
API_TOKEN = "your_api_token"

class TestMultiloginClient(unittest.TestCase):

    def setUp(self):
        self.client = MultiloginClient(API_TOKEN)

    def test_get_all_profiles(self):
        profiles = self.client.get_all_profiles()
        self.assertIsInstance(profiles, list, "The result should be a list of profiles")
        # You can add more specific assertions depending on your account's profiles

if __name__ == "__main__":
    unittest.main()
