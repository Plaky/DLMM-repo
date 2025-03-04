import unittest
from src.token_analyzer import TokenAnalyzer
from src.models.security_report import SecurityReport

class TestTokenAnalyzer(unittest.TestCase):

    def setUp(self):
        self.token_analyzer = TokenAnalyzer()

    def test_check_mint_authority(self):
        token_address = "example_token_address"
        mint_authority = self.token_analyzer.check_mint_authority(token_address)
        self.assertIsNotNone(mint_authority)
        # Add more assertions based on expected mint authority behavior

    def test_check_freeze_authority(self):
        token_address = "example_token_address"
        freeze_authority = self.token_analyzer.check_freeze_authority(token_address)
        self.assertIsNotNone(freeze_authority)
        # Add more assertions based on expected freeze authority behavior

    def test_check_upgradeable(self):
        token_address = "example_token_address"
        is_upgradeable = self.token_analyzer.check_upgradeable(token_address)
        self.assertIsInstance(is_upgradeable, bool)
        # Add more assertions based on expected upgradeable behavior

    def test_check_metadata_verified(self):
        token_address = "example_token_address"
        metadata_verified = self.token_analyzer.check_metadata_verified(token_address)
        self.assertIsInstance(metadata_verified, bool)
        # Add more assertions based on expected metadata verification behavior

if __name__ == '__main__':
    unittest.main()