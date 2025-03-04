def get_token_metadata(connection, token_address):
    from solana.rpc.api import Client
    from spl.token.constants import TOKEN_PROGRAM_ID
    from spl.token.instructions import get_account_info

    # Create a Solana client
    client = Client(connection)

    # Fetch the account info for the token address
    account_info = client.get_account_info(token_address)

    if account_info['result']['value'] is None:
        raise ValueError("Token address not found.")

    # Decode the token account data
    token_data = get_account_info(account_info['result']['value']['data'][0])

    return token_data


def check_mint_authority(token_data):
    return token_data['mint_authority']


def check_freeze_authority(token_data):
    return token_data['freeze_authority']


def check_upgradeable(token_data):
    return token_data.get('upgradeable', False)


def check_metadata_verified(token_data):
    return token_data.get('metadata_verified', False)