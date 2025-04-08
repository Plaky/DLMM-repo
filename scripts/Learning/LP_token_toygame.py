import requests
from datetime import datetime
from solana.rpc.api import Client
from solders.pubkey import Pubkey

# This function is used to find the earliest created liquidity pool for a token using DexScreener API
def find_earliest_pool(token_address: str):
    """
    Finds the earliest created liquidity pool for a token using DexScreener API
    
    Args:
        token_address (str): The token address to search pools for
        
    Returns:
        dict: Information about the earliest pool including address, DEX, pool type, and creation date,
              or error information if no pool is found
    """
    try:
        # Call DexScreener API to get all pairs for the token
        url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            return {"error": f"DexScreener API error: {response.status_code}"}
            
        # Get all pairs from the response
        pairs = response.json().get("pairs", [])
        # print(pairs)
        if not pairs:
            return {"error": "No liquidity pools found for this token"}
            
        # Find the pair with the earliest creation timestamp across all DEXes
        earliest_pair = min(pairs, key=lambda x: x.get('pairCreatedAt', float('inf')))
        
        # Extract relevant information
        result = {
            "pairAddress": earliest_pair.get('pairAddress'),
            "dexId": earliest_pair.get('dexId'),
            "baseToken": earliest_pair.get('baseToken', {}).get('symbol'),
            "quoteToken": earliest_pair.get('quoteToken', {}).get('symbol'),
            "liquidity": earliest_pair.get('liquidity', {}).get('usd')
        }
        
        # Add human-readable creation date
        timestamp = earliest_pair.get('pairCreatedAt')
        if timestamp:
            creation_date = datetime.fromtimestamp(timestamp / 1000)
            result["createdAt"] = creation_date.strftime('%Y-%m-%d %H:%M:%S')
            result["timestamp"] = timestamp
        
        # Add pool type information directly from DexScreener
        labels = earliest_pair.get('labels', [])
        if 'CLMM' in labels:
            result["pool_type"] = "CLMM"
        elif 'DLMM' in labels:
            result["pool_type"] = "DLMM"
        elif 'DYN' in labels:
            result["pool_type"] = "DYN"
        else:
            # Default to AMM if no specific label is provided
            result["pool_type"] = "AMM"
        
        # Add dex information (already available from dexId)
        result["dex"] = result["dexId"].capitalize()
        
        return result
        
    except Exception as e:
        return {"error": f"Failed to find earliest pool: {str(e)}"}
    
# Example usage
if __name__ == "__main__":
    # Example token address
    print(find_earliest_pool('C3DwDjT17gDvvCYC2nsdGHxDHVmQRdhKfpAdqQ29pump'))

