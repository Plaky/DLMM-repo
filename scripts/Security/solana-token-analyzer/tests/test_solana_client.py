import unittest
from src.utils.solana_client import SolanaClient

class TestSolanaClient(unittest.TestCase):
    def setUp(self):
        self.client = SolanaClient()

    def test_get_token_info(self):
        token_address = "YourTokenAddressHere"
        token_info = self.client.get_token_info(token_address)
        self.assertIsNotNone(token_info)
        self.assertIn('mintAuthority', token_info)
        self.assertIn('freezeAuthority', token_info)
        self.assertIn('isUpgradeable', token_info)
        self.assertIn('metadataVerified', token_info)

    def test_invalid_token_address(self):
        invalid_address = "InvalidTokenAddress"
        with self.assertRaises(ValueError):
            self.client.get_token_info(invalid_address)

if __name__ == '__main__':
    unittest.main()