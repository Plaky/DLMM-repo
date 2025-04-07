import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
HELIUS_API_KEY = os.getenv('HELIUS_API_KEY')

# Validate that the API key exists
if not HELIUS_API_KEY:
    raise ValueError("HELIUS_API_KEY not found in environment variables. Please check your .env file.")

# Create RPC URL
HELIUS_RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}" 