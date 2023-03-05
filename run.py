import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
PRIV_KEY = os.environ.get("PRIV_KEY")
ADDRESS = os.environ.get("ADDRESS")

from publisher.client import PublisherClient
from publisher.fetcher import *
from publisher.assets import ALL_ASSETS
from config.chain import Networks
from core.utils import str_to_bytes32

publisher = PublisherClient(
    "FVM_testnet", 
    ADDRESS, 
    PRIV_KEY)


publisher.add_fetchers(
	[BitstampFetcher(ALL_ASSETS, "DOM"),
	CoinbaseFetcher(ALL_ASSETS, "DOM"),
	AscendexFetcher(ALL_ASSETS, "DOM"),
	OkxFetcher(ALL_ASSETS, "DOM"),
	GeminiFetcher(ALL_ASSETS, "DOM")]
)


while True:
    time.sleep(20)
    data = publisher.fetch_sync()
    publisher.publish_spot_entries(data)
