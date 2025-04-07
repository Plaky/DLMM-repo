#!/usr/bin/env python3

from solana.rpc.api import Client
from solders.pubkey import Pubkey

def identify_pool_type(pool_address):
    """
    Determines the type of Solana liquidity pool based on its program ID
    
    Args:
        pool_address: A Solders Pubkey object representing the pool address
        
    Returns:
        A dictionary with information about the pool type, program ID, and DEX
    """
    try:
        # Get account info to determine program ID
        solana_client = Client("https://api.mainnet-beta.solana.com")
        account_info = solana_client.get_account_info(pool_address)
        
        if not account_info.value:
            return {"error": "Pool account not found"}
        
        program_id = str(account_info.value.owner)
        
        # Define known program IDs
        RAYDIUM_CLMM_PROGRAM = "CAMMCzo5YL8w4VFF8KVHrK22GGUsp5VTaW7grrKgrWqK"  # Raydium Concentrated Liquidity Market Maker
        RAYDIUM_AMM_PROGRAM = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"  # Raydium Standard AMM (CPMM)
        METEORA_DLMM_PROGRAM = "LBUZKhRxPF3XUpBCjp4YzTKgLccjZhTSDM9YuVaPwxo"  # Meteora Dynamic Liquidity Market Maker
        ORCA_WHIRLPOOL_PROGRAM = "whirLbMiicVdio4jvUfM5KAg6Ct8VwpasGwh5RV6a"  # Orca Whirlpools (CLMM)
        LIFINITY_PROGRAM = "EewxydAPJAb2sBCLQeoVwR1n6yUpG7djL2T3nBdw2A2n"  # Lifinity Proactive Market Maker
        PHOENIX_PROGRAM = "PhoeniXxDaP9rssfjbPPbFR7bGCDNE6SR9t6Fc1nxJ"  # Phoenix Order Book DEX
        CREMA_CLMM_PROGRAM = "CRMaCEMsB9d6vM6V9D5q5g5vSUr9N2nT3BPCzppMJr9h"  # Crema Finance CLMM
        
        # Determine pool type
        if program_id == RAYDIUM_CLMM_PROGRAM:
            return {
                "pool_type": "CLMM",
                "program_id": program_id,
                "dex": "Raydium"
            }
        elif program_id == RAYDIUM_AMM_PROGRAM:
            return {
                "pool_type": "AMM",
                "program_id": program_id,
                "dex": "Raydium"
            }
        elif program_id == METEORA_DLMM_PROGRAM:
            return {
                "pool_type": "DLMM",
                "program_id": program_id,
                "dex": "Meteora"
            }
        elif program_id == ORCA_WHIRLPOOL_PROGRAM:
            return {
                "pool_type": "CLMM", 
                "program_id": program_id,
                "dex": "Orca"
            }
        elif program_id == LIFINITY_PROGRAM:
            return {
                "pool_type": "PMM",  # Proactive Market Maker
                "program_id": program_id,
                "dex": "Lifinity"
            }
        elif program_id == PHOENIX_PROGRAM:
            return {
                "pool_type": "Order Book",
                "program_id": program_id,
                "dex": "Phoenix"
            }
        elif program_id == CREMA_CLMM_PROGRAM:
            return {
                "pool_type": "CLMM",
                "program_id": program_id,
                "dex": "Crema Finance"
            }
        else:
            return {
                "pool_type": "Unknown",
                "program_id": program_id,
                "message": "Unrecognized pool program"
            }
    
    except Exception as e:
        return {"error": f"Failed to identify pool type: {str(e)}"}


def main():
    """Test the identify_pool_type function with example pool addresses"""
    
    # Example pool addresses to test different DEXes
    pool_addresses = [
        "C6tRBKe69kEXVZHebne3GFypxrRRgVHJTJAoNmiacujd",  # Example Meteora pool
        # Add more pool addresses here to test other DEXes
    ]
    
    print("Testing pool identification with various DEX pools")
    print("-" * 50)
    
    for address in pool_addresses:
        print(f"\nAnalyzing pool: {address}")
        pubkey = Pubkey.from_string(address)
        result = identify_pool_type(pubkey)
        
        print(f"Pool type: {result.get('pool_type', 'Unknown')}")
        print(f"DEX: {result.get('dex', 'Unknown')}")
        print(f"Program ID: {result.get('program_id', 'N/A')}")
        
        if 'error' in result:
            print(f"Error: {result['error']}")
        elif 'message' in result:
            print(f"Message: {result['message']}")


if __name__ == "__main__":
    main() 