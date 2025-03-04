# Solana Token Analyzer

## Overview
The Solana Token Analyzer is a Python application designed to assess the security risks associated with tokens on the Solana blockchain. It connects to the Solana API to retrieve information about token smart contracts and evaluates key attributes such as mint authority, freeze authority, upgradeability, and metadata verification.

## Features
- **Mint Authority Check**: Verifies the mint authority of a token to ensure it is secure.
- **Freeze Authority Check**: Assesses the freeze authority to determine if the token can be frozen.
- **Upgradeable Check**: Checks if the token's smart contract is upgradeable, which may pose security risks.
- **Metadata Verification**: Validates the token's metadata to ensure it is verified and trustworthy.

## Project Structure
```
solana-token-analyzer
├── src
│   ├── main.py
│   ├── token_analyzer.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── solana_client.py
│   │   └── token_metadata.py
│   └── models
│       ├── __init__.py
│       └── security_report.py
├── config
│   └── settings.py
├── tests
│   ├── __init__.py
│   ├── test_token_analyzer.py
│   └── test_solana_client.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/solana-token-analyzer.git
   ```
2. Navigate to the project directory:
   ```
   cd solana-token-analyzer
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```
Follow the prompts to input the token address you wish to analyze.

## Testing
To run the unit tests for the application, use:
```
pytest
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.