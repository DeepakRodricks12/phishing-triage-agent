import unittest

class TestEmailAnalyzer(unittest.TestCase):

    def test_valid_email(self):
        # Example test for a valid email
        result = email_analyzer.analyze('test@example.com')
        self.assertEqual(result, 'valid')

    def test_invalid_email(self):
        # Example test for an invalid email
        result = email_analyzer.analyze('test@.com')
        self.assertEqual(result, 'invalid')

    def test_spam_email(self):
        # Example test for a spam email
        result = email_analyzer.analyze('offer@spam.com')
        self.assertEqual(result, 'spam')

    def test_empty_email(self):
        # Example test for an empty email
        result = email_analyzer.analyze('')
        self.assertEqual(result, 'invalid')

if __name__ == '__main__':
    unittest.main()