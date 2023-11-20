from src.interactors.chain_interactor_interface import ChainInteractor
from src.interactors.ethereum.erc20_usdt_interactor import Erc20UsdtInteractor
from src.interactors.bnb.bep20_usdt_interactor import Bep20UsdtInteractor


class TransferTxGenerator:
    def __init__(self, chain_interactor: ChainInteractor):
        self.chain_interactor = chain_interactor

    def generate_transfer_tx(
        self, to_address: str, amount_to_send: float, nonce: int = 0
    ) -> str:
        return self.chain_interactor.build_signed_tx(to_address, amount_to_send, nonce)

    @staticmethod
    def erc20_usdt(private_key: str):
        chain_interactor = Erc20UsdtInteractor(private_key)
        return TransferTxGenerator(chain_interactor)

    @staticmethod
    def bep20_usdt(private_key: str):
        chain_interactor = Bep20UsdtInteractor(private_key)
        return TransferTxGenerator(chain_interactor)
