import json
from web3 import Web3
from src.constants.enums import Coin
from src.constants.token_info import ETH_USDT, BEP20_USDT


class ContractBuilder:
    @staticmethod
    def build(coin: Coin) -> any:
        if coin == Coin.ERC20_USDT:
            contract_address = ETH_USDT["address"]
            contract_abi = json.loads(ETH_USDT["abi"])
            contract = Web3().eth.contract(address=contract_address, abi=contract_abi)
            return contract
        elif coin == Coin.BEP20_USDT:
            contract_address = BEP20_USDT["address"]
            contract_abi = json.loads(BEP20_USDT["abi"])
            contract = Web3().eth.contract(address=contract_address, abi=contract_abi)
            return contract
        else:
            raise NotImplementedError("{0} not Supported".format(coin))
