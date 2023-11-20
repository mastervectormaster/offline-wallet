import pytest
from src.contracts.contract_builder import ContractBuilder
from src.constants.enums import Coin


def test_contract_build_success_on_supported_coins():
    supported_coins = [coin for coin in Coin if coin.name != "UNKNOWN"]
    for coin in supported_coins:
        ContractBuilder.build(coin)


def test_contract_build_fail_on_unsupported_coin():
    with pytest.raises(NotImplementedError):
        ContractBuilder.build(Coin.UNKNOWN)
