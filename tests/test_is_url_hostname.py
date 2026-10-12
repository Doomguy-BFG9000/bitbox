import unittest

from tools.is_url import run


class URLHostnameTests(unittest.TestCase):
    def test_authority_without_host_is_false(self):
        for value in ("http://:80", "http://user@", "https://user:dummy@", "https://@:"):
            with self.subTest(value=value):
                self.assertEqual(run(value), "false")

    def test_http_and_https_hosts_remain_valid(self):
        for value in ("http://example.test", "https://example.test/path?q=1", "http://localhost:8000", "http://127.0.0.1", "http://[::1]:8000", "https://user:dummy@example.test"):
            with self.subTest(value=value):
                self.assertEqual(run(value), "true")

    def test_existing_invalid_inputs(self):
        for value in ("", "example.test", "file:///tmp/demo", "ftp://example.test", "http:///path", "http://[broken"):
            with self.subTest(value=value):
                self.assertEqual(run(value), "false")

    def test_whitespace_and_missing_argument(self):
        self.assertEqual(run("  https://example.test  "), "true")
        self.assertEqual(run(), "Error: expected a string argument")


if __name__ == "__main__":
    unittest.main()
