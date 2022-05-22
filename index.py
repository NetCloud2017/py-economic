import akshare as ak

futures_zh_spot_df = ak.futures_zh_spot(
    symbol='P2209', market="CF", adjust='0')
print(futures_zh_spot_df)
