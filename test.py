# from publisher.client import PublisherClient
# from publisher.fetcher import *
# from publisher.assets import ALL_ASSETS
# from config.chain import Networks

# a = PublisherClient("FVM_testnet", "1dd3a5652ee5590dca9f6afef8340fab052a144c710505bd2341bb9387b3a23f", "1dd3a5652ee5590dca9f6afef8340fab052a144c710505bd2341bb9387b3a23f")
# a.add_fetchers(
# 	[BitstampFetcher(ALL_ASSETS, "DOM"),
# 	CoinbaseFetcher(ALL_ASSETS, "DOM"),
# 	AscendexFetcher(ALL_ASSETS, "DOM"),
# 	OkxFetcher(ALL_ASSETS, "DOM"),
# 	GeminiFetcher(ALL_ASSETS, "DOM")]
# )

# data = a.fetch_sync()
# data = a.remove_fetch_error(data)

# results = []
# for entry in data:
#     if type(entry) != PublisherFetchError:
#         results.append(entry)
