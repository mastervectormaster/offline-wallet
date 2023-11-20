from abc import ABC, abstractclassmethod


class ChainInteractor(ABC):
    def __init__(self, private_key):
        self.private_key = private_key

    def build_signed_tx(
        self, to_address: str, amount_to_send: float, nonce: int
    ) -> any:
        unsigned_tx = self.build_unsigned_tx(to_address, amount_to_send, nonce)
        signed_tx = self.sign_tx(unsigned_tx)
        return signed_tx

    @abstractclassmethod
    def build_unsigned_tx(self) -> any:
        pass

    @abstractclassmethod
    def sign_tx(self) -> str:
        pass
