from scripts.solana_client import get_client

class SolanaClient:
    def __init__(self):
        self.client = get_client()

    def get_token_info(self, token_address):
        response = self.client.get_account_info(token_address)
        if response['result']['value'] is None:
            return None
        return response['result']['value']

    def check_mint_authority(self, token_address):
        token_info = self.get_token_info(token_address)
        if token_info:
            return token_info['data']['parsed']['info']['mintAuthority']
        return None

    def check_freeze_authority(self, token_address):
        token_info = self.get_token_info(token_address)
        if token_info:
            return token_info['data']['parsed']['info']['freezeAuthority']
        return None

    def check_upgradeable(self, token_address):
        token_info = self.get_token_info(token_address)
        if token_info:
            return token_info['data']['parsed']['info']['isMutable']
        return None

    def check_metadata_verified(self, token_address):
        # This method would typically involve fetching metadata from a specific source
        # and checking its verification status. Placeholder for actual implementation.
        return True  # Placeholder return value for metadata verification status.