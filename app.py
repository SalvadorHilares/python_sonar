import unittest

class Usuario():
    def __init__(self, username):
        self.username = username

class Tests(unittest.TestCase):

    user = Usuario('pepito')

    def test_login(self):
        test_password=''.join(reversed(self.user.username))
        self.assertEqual(self.user.username,'pepito')
        self.assertEqual(test_password,'otipep')

if __name__ == '__main__':
    unittest.main()