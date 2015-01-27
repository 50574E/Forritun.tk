from django.test import TestCase
from discourse.discoursesso import DiscourseSSO


class DiscourseTests(TestCase):
    domain = "http://discuss.example.com"
    url = "http://www.example.com/discourse/sso"
    secret = "d836444a9e4084d5b224a60c208dce14"
    sso = DiscourseSSO(secret_key=secret)

    def test_validation(self):
        """
        Discourse payloads should be validated with HMAC-SHA256
        """
        # Values from https://meta.discourse.org/t/official-single-sign-on-for-discourse/13045
        url_payload = "bm9uY2U9Y2I2ODI1MWVlZmI1MjExZTU4YzAwZmYxMzk1ZjBjMGI%3D%0A"
        sig = "2828aa29899722b35a2f191d34ef9b3ce695e0e6eeec47deb46d588d70c7cb56"
        validated = self.sso.validate(url_payload, sig)
        self.assertEqual(validated, True)

    def test_get_nounce(self):
        """
        get_nounce() should get nounce out of payload
        """
        url_payload = "bm9uY2U9Y2I2ODI1MWVlZmI1MjExZTU4YzAwZmYxMzk1ZjBjMGI%3D%0A"
        correct_nounce = "cb68251eefb5211e58c00ff1395f0c0b"
        nounce = self.sso.get_nonce(url_payload)
        self.assertEqual(correct_nounce, nounce)
