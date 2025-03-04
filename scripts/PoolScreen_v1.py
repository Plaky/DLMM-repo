import requests
import pandas as pd

def fetch_all_pairs(
    base_url: str = "https://dlmm-api.meteora.ag",
    include_unknown: bool = True,
    page: int = 0,
    limit: int = 50,
    hide_low_tvl: float = 0.0
):
    """
    Fetches all pairs using the /pair/all_with_pagination endpoint.
    Adjust the query parameters as needed.
    """
    endpoint = f"{base_url}/pair/all_with_pagination"
    params = {
        "include_unknown": str(include_unknown).lower(),
        "page": page,
        "limit": limit,
        "hide_low_tvl": 7000,
        "sort_key": "feetvlratio30m",
        "order_by": "desc",
        # "include_pool_token_pairs": "true"
    }
    resp = requests.get(endpoint, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

# Fetch the data
pairs_data = fetch_all_pairs()

# Keep only a subset of columns
columns_to_keep = [
    'address', 'name', 'mint_x', 'bin_step', 'base_fee_percentage', 'max_fee_percentage',
    'liquidity', 'fees_24h', 'trade_volume_24h', 'fees', 'fee_tvl_ratio', 'volume'
]
df = pd.DataFrame(pairs_data['pairs'])[columns_to_keep]

# Extract 30m and 1h only, discard 2h
for col in ['fees', 'fee_tvl_ratio', 'volume']:
    df[f"{col}_min_30"] = df[col].apply(lambda x: x.get('min_30') if isinstance(x, dict) else None)
    df[f"{col}_hour_1"] = df[col].apply(lambda x: x.get('hour_1') if isinstance(x, dict) else None)

# Drop the original columns
df.drop(columns=['fees', 'fee_tvl_ratio', 'volume'], inplace=True)

# Keep the 30m fee_tvl_ratio in its own column
df['fee_tvl_ratio_30m'] = df['fee_tvl_ratio_min_30']

def simple_momentum(row, col_prefix):
    v30 = row[f"{col_prefix}_min_30"]
    v1h = row[f"{col_prefix}_hour_1"]
    if v30 is None or v1h is None:
        return None
    # If 30m * 2 > 1h => "+", else "-"
    return "+" if (v30 * 2) > v1h else "-"

# Add momentum columns
df['fees_momentum'] = df.apply(lambda row: simple_momentum(row, "fees"), axis=1)
df['fee_tvl_ratio_momentum'] = df.apply(lambda row: simple_momentum(row, "fee_tvl_ratio"), axis=1)
df['volume_momentum'] = df.apply(lambda row: simple_momentum(row, "volume"), axis=1)

# Reorder and rename columns
desired_columns = [
    'name',
    'address',
    'mint_x',
    'liquidity',                # Will become 'TVL'
    'fee_tvl_ratio_min_30',     # Will become 'Fee/TVL 30m'
    'bin_step',
    'base_fee_percentage',      # Will become 'Fee %'
    'max_fee_percentage',       # Will become 'Max fee %'
    'fee_tvl_ratio_momentum',   # Will become 'Fee/TVL mom'
    'volume_momentum',          # Will become 'Vol mom'
    'fees_momentum',            # Will become 'Fees mom'
    'volume_min_30'            # Will become 'Vol 30m'
]
df = df[desired_columns].rename(columns={
    'liquidity': 'TVL',
    'address': 'DLMM Address',
    'mint_x': 'CA',
    'fee_tvl_ratio_min_30': 'Fee/TVL 30m',
    'base_fee_percentage': 'Fee %',
    'max_fee_percentage': 'Max fee %',
    'fee_tvl_ratio_momentum': 'Fee/TVL mom',
    'volume_momentum': 'Vol mom',
    'fees_momentum': 'Fees mom',
    'volume_min_30': 'Vol 30m'
})

# Add a prefix to the DLMM Address column
df["DLMM Address"] = df["DLMM Address"].apply(lambda addr: f"https://app.meteora.ag/dlmm/{addr}")

# Create a new column "APR 30m" after "Fee/TVL 30m"
# First remove any '%' characters
df["Fee %"] = df["Fee %"].astype(str).str.strip('%')

# Now convert to float and divide by 100
df["Fee %"] = pd.to_numeric(df["Fee %"], errors="coerce")

# Then handle Vol 30m and TVL
df["Vol 30m"] = pd.to_numeric(df["Vol 30m"], errors="coerce")
df["TVL"] = pd.to_numeric(df["TVL"], errors="coerce")

df["APR 30m"] = (df["Vol 30m"] * df["Fee %"]) / df["TVL"]

# Reorder columns to place "APR 30m" right after "Fee/TVL 30m"
final_column_order = [
    'name',
    'Fee/TVL 30m',
    'APR 30m',
    'bin_step',
    'Fee %',
    'Max fee %',
    'Fee/TVL mom',
    'Vol mom',
    'Fees mom',
    'Vol 30m',
    'TVL',
    'CA',
    'DLMM Address'
]
df = df[final_column_order]

# Optionally adjust display
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.max_colwidth', None)  # or a large integer

print(df.head(10))