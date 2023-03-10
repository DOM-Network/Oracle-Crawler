import os
import time
from dotenv import dotenv_values

config = dotenv_values(".env")
PRIV_KEY = os.environ.get("PRIV_KEY")
ADDRESS = os.environ.get("ADDRESS")

from publisher.client import PublisherClient
from publisher.fetcher import *
from publisher.assets import ALL_ASSETS
from config.chain import Networks
from core.utils import str_to_bytes32

publisher = PublisherClient(
    "FVM_testnet", 
    config["ADDRESS"], 
    config["PRIV_KEY"]
)


publisher.add_fetchers(
	[BitstampFetcher(ALL_ASSETS, "DOM"),
	CoinbaseFetcher(ALL_ASSETS, "DOM"),
	AscendexFetcher(ALL_ASSETS, "DOM"),
	OkxFetcher(ALL_ASSETS, "DOM"),
	GeminiFetcher(ALL_ASSETS, "DOM")]
)


while True:    
    data = publisher.fetch_sync()
    publisher.publish_spot_entries(data)
    time.sleep(500)
