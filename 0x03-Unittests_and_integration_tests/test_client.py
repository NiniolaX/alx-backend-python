#!/usr/bin/env python3
""" Tests for client module
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
from unittest.mock import patch, Mock


class TestGithibOrgClient(unittest.TestCase):
    """ Test case for GithubOrgClient """
    @parameterized.expand([
        ("google", {"login": "google",
                    "repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"login": "abc",
                 "repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 expected_result: Dict,
                 mock_get_json: Mock) -> None:
        """
        Tests GithubOrgClient.org returns correct value for given org_name
        Mocks get_json to avoid actual API calls
        """
        mock_get_json.return_value = expected_result

        # Create instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call `org` property and check that it matches expected result
        self.assertEqual(client.org, expected_result)

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == "__main__":
    unittest.main()
