from solana.rpc.api import Client
from solders.pubkey import Pubkey
import requests

# Raydium programs
RAYDIUM_CLMM_PROGRAM = "CAMMCzo5YL8w4VFF8KVHrK22GGUsp5VTaW7grrKgrWqK"  # Raydium Concentrated Liquidity Market Maker
RAYDIUM_AMM_PROGRAM = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"  # Raydium Standard AMM (CPMM)
# Meteora programs
METEORA_DLMM_PROGRAM = "LBUZKhRxPF3XUpBCjp4YzTKgLccjZhTSDM9YuVaPwxo"  # Meteora Dynamic Liquidity Market Maker
# Orca programs
ORCA_WHIRLPOOL_PROGRAM = "whirLbMiicVdio4jvUfM5KAg6Ct8VwpasGwh5RV6a"  # Orca Whirlpools (CLMM)
# PumpSwap programs
PUMPSWAP_PROGRAM = "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"  # PumpSwap Standard AMM (CPMM)

# Cache for pool type results
pool_type_cache = {}

def identify_pool_type(pool_address):
    """
    Determines the type of Solana liquidity pool based on its program ID
    
    Args:
        pool_address: A Solders Pubkey object representing the pool address
        
    Returns:
        A dictionary with information about the pool type, program ID, and DEX
    """
    # Check cache first
    cache_key = str(pool_address)
    if cache_key in pool_type_cache:
        return pool_type_cache[cache_key]
    
    try:
        # Get account info to determine program ID
        solana_client = Client("https://api.mainnet-beta.solana.com")
        account_info = solana_client.get_account_info(pool_address)
        
        if not account_info.value:
            result = {"error": "Pool account not found"}
            pool_type_cache[cache_key] = result
            return result
        
        program_id = str(account_info.value.owner)
        
        # Determine pool type
        if program_id == RAYDIUM_CLMM_PROGRAM:
            result = {
                "pool_type": "CLMM",
                "program_id": program_id,
                "dex": "Raydium"
            }
        elif program_id == RAYDIUM_AMM_PROGRAM:
            result = {
                "pool_type": "AMM",
                "program_id": program_id,
                "dex": "Raydium"
            }
        elif program_id == METEORA_DLMM_PROGRAM:
            result = {
                "pool_type": "DLMM",
                "program_id": program_id,
                "dex": "Meteora"
            }
        elif program_id == ORCA_WHIRLPOOL_PROGRAM:
            result = {
                "pool_type": "CLMM",
                "program_id": program_id,
                "dex": "Orca"
            }
        elif program_id == PUMPSWAP_PROGRAM:
            result = {
                "pool_type": "AMM",
                "program_id": program_id,
                "dex": "PumpSwap"
            }
        else:
            result = {
                "pool_type": "Unknown",
                "program_id": program_id,
                "message": "Unrecognized pool program"
            }
        
        # Cache result before returning
        pool_type_cache[cache_key] = result
        return result
    
    except ValueError as e:
        result = {"error": f"Invalid pool address format: {str(e)}"}
        pool_type_cache[cache_key] = result
        return result
    except requests.exceptions.RequestException as e:
        result = {"error": f"RPC connection error: {str(e)}"}
        pool_type_cache[cache_key] = result
        return result
    except Exception as e:
        result = {"error": f"Unexpected error: {str(e)}"}
        pool_type_cache[cache_key] = result
        return result


# Example usage
if __name__ == "__main__":
    # Example pool address
    pool_address = 'C6tRBKe69kEXVZHebne3GFypxrRRgVHJTJAoNmiacujd'
    pubkey = Pubkey.from_string(pool_address)
    result = identify_pool_type(pubkey)
    print(result) 
    
    # Demonstrate cache usage
    # print("Calling again (should use cache):")
    # result2 = identify_pool_type(pubkey)
    # print(result2) 