from solana.rpc.api import Client
from scripts.config import HELIUS_RPC_URL

# Create a singleton Solana client instance
solana_client = Client(HELIUS_RPC_URL)

def get_client():
    """
    Returns the configured Solana client instance.
    This ensures we're using the same client throughout the application.
    """
    return solana_client 