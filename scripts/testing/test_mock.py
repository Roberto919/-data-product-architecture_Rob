#users_test/test_users.py
import unittest
from users import get_users, get_user
from unittest.mock import patch, Mock


class BasicTests(unittest.TestCase):
    @patch('users.get_users')
    def test_get_one_user(self, mock_get_users):
        """
        Test for getting one user using their userID
        Demonstrates mocking third party functions
        """
        users = [
            {'phone': '514-794-6957', 'first_name': 'Brant', 'last_name': 'Mekhi', 'id': 0},
            {'phone': '772-370-0117', 'first_name': 'Thalia', 'last_name': 'Kenyatta', 'id': 1},
            {'phone': '176-290-7637', 'first_name': 'Destin', 'last_name': 'Soledad', 'id': 2}
        ]
        mock_get_users.return_value = Mock()
        mock_get_users.return_value.json.return_value = users
        user = get_user(2)
        self.assertEqual(user, users[2])