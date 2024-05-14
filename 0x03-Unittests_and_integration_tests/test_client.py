#!/usr/bin/env python3
""" Module for testing client """


from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing Github Org Client """

    @parameterized.expand ([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
