from utils.solana_client import SolanaClient
from token_analyzer import TokenAnalyzer

def main():
    # Initialize the Solana client
    solana_client = SolanaClient()

    # Get user input for the token address
    token_address = input("Enter the token address: ")

    # Initialize the TokenAnalyzer
    token_analyzer = TokenAnalyzer(solana_client)

    # Perform security checks
    report = token_analyzer.analyze_token(token_address)

    # Display the security report
    print("Security Report:")
    print(f"Mint Authority: {report.mint_authority}")
    print(f"Freeze Authority: {report.freeze_authority}")
    print(f"Upgradeable: {report.upgradeable}")
    print(f"Metadata Verified: {report.metadata_verified}")

if __name__ == "__main__":
    main()