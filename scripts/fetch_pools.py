import requests

# Define the base URL of the API
BASE_URL = "https://dlmm-api.meteora.ag"  # Replace with the correct API URL if needed

# Endpoint to fetch all pools
endpoint = "/pair/all"

# Define the request parameters (optional)
params = {
    "include_unknown": True  # Include pools with unverified tokens (default: True)
}

# Make the request
try:
    response = requests.get(BASE_URL + endpoint, params=params)
    response.raise_for_status()  # Raise an error for HTTP errors (4xx, 5xx)
    
    # Parse JSON response
    pools = response.json()

    # Display the first few pools
    print("Retrieved Pools:")
    for pool in pools[:5]:  # Show only first 5 for brevity
        print(f"Name: {pool['name']}, Address: {pool['address']}, TVL: {pool.get('liquidity', 'N/A')}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching pools: {e}")
