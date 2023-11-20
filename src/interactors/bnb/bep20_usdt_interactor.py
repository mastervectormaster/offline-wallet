from web3 import Web3
from src.interactors.chain_interactor_interface import ChainInteractor
from src.constants.enums import Coin
from src.contracts.contract_builder import ContractBuilder
from src.constants import gas_info as GasInfo
from src.constants import chain_ids as ChainIDs


class Bep20UsdtInteractor(ChainInteractor):
    def __init__(self, private_key: str):
        super().__init__(private_key)
        self.token_contract = ContractBuilder.build(Coin.BEP20_USDT)

    def build_unsigned_tx(
        self, to_address: str, amount_to_send: float, nonce: int
    ) -> any:
        usdt_amount = int(amount_to_send * 10**18)
        gas_info = GasInfo.BNB
        unsigned_tx = self.token_contract.functions.transfer(
            to_address, usdt_amount
        ).build_transaction(
            {
                "chainId": ChainIDs.BNB,
                "gas": gas_info["gas"],
                "gasPrice": gas_info["gasPrice"],
                "nonce": nonce,
            }
        )
        return unsigned_tx

    def sign_tx(self, unsigned_tx) -> str:
        web3 = Web3()
        signed_tx = web3.eth.account.sign_transaction(unsigned_tx, self.private_key)
        return signed_tx.rawTransaction.hex()
