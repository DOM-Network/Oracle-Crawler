import logging
from typing import Optional, List
import json
from web3 import Web3, HTTPProvider

from config.chain import Networks
from core.entry import SpotEntry
from core.utils import str_to_bytes32

logger = logging.getLogger(__name__)

class CoreClient:
    def __init__(
        self,
        network,
        client_address: str,
        client_private_key: str
    ):
        if network not in Networks.keys():
            raise NotImplementedError(f"Network {network} not recognized")

        self.client_address = client_address
        self.client_private_key = client_private_key
        self.network = Networks[network]
        self.web3 = Web3(HTTPProvider(self.network['RPC']))
        self._setup_contracts

    def _setup_contracts(self):
        oracle_abis = json.load(open("abis/Oracle.json", "r"))
        self.oracle = serialize.w3.eth.contract(
            address=self.network["Oracle Contract Address"], 
            abi=oracle_abis)

        publisher_registry_abis =  json.load(open("abis/PublisherRegistry.json", "r"))
        self.publisher_registry = serialize.w3.eth.contract(
            address=self.network["Publisher Registry Contract Address"], 
            abi=publisher_registry_abis)

    async def get_nonce(self):
        return self.web3.eth.getTransactionCount(self.client_address)

    async def publish_spot_entry(self, spot_entry: SpotEntry):
        nonce = self.get_nonce()
        call_function = contract.functions.publishSpotEntry({
          base: {
            timestamp: spot_entry.base.timestamp,
            source: str_to_bytes32(spot_entry.base.source),
            publisher: str_to_bytes32(spot_entry.base.publisher),
          },
          pairId: str_to_bytes32(spot_entry.pair_id),
          price: spot_entry.price,
          volume: spot_entry.volume,
        }).buildTransaction({"chainId": Chain_id, "from": caller, "nonce": nonce, "gasPrice": w3.eth.gas_price})
        signed_tx = self.web3.eth.account.sign_transaction(call_function, private_key = self.client_private_key)
        send_tx = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)
        return print(tx_receipt)

    async def publish_spot_entry(self, spot_entry: SpotEntry):        
        call_function = contract.functions.publishSpotEntry({
          base: {
            timestamp: spot_entry.base.timestamp,
            source: str_to_bytes32(spot_entry.base.source),
            publisher: str_to_bytes32(spot_entry.base.publisher),
          },
          pairId: str_to_bytes32(spot_entry.pair_id),
          price: spot_entry.price,
          volume: spot_entry.volume,
        }).buildTransaction({"chainId": Chain_id, "from": caller, "nonce": nonce, "gasPrice": w3.eth.gas_price})

        nonce = self.get_nonce()
        signed_tx = self.web3.eth.account.sign_transaction(call_function, private_key = self.client_private_key)
        send_tx = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)
        return print(tx_receipt)

    async def publish_spot_entries(self, spot_entries:List[SpotEntry]):
        call_function = contract.functions.publishSpotEntries([{
          base: {
            timestamp: spot_entry.base.timestamp,
            source: str_to_bytes32(spot_entry.base.source),
            publisher: str_to_bytes32(spot_entry.base.publisher),
          },
          pairId: str_to_bytes32(spot_entry.pair_id),
          price: spot_entry.price,
          volume: spot_entry.volume,
        } for spot_entry in spot_entries]).buildTransaction({"chainId": Chain_id, "from": caller, "nonce": nonce, "gasPrice": w3.eth.gas_price})
        
        nonce = self.get_nonce()
        signed_tx = self.web3.eth.account.sign_transaction(call_function, private_key = self.client_private_key)
        send_tx = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)
        return print(tx_receipt)

