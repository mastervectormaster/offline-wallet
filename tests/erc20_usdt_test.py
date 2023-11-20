from dotenv import dotenv_values
from src.tx_managers.transfer_tx_generator import TransferTxGenerator

config = dotenv_values(".env")

private_key = config["ETHEREUM_TEST_PRIVATE_KEY"]
to_address = "0x80583D6eFC0c324818e0811bF641d37B4D8fb0FC"
amount_to_send = 1
nonce = 4
expected_raw_tx = "0xf8a5040f8301117094dac17f958d2ee523a2206206994597c13d831ec780b844a9059cbb00000000000000000000000080583d6efc0c324818e0811bf641d37b4d8fb0fc00000000000000000000000000000000000000000000000000000000000f424025a0a908d934c7060aec608d8f6a03ad2ff00279d98898e44e784eeb08a646565d2ba067cba243798b68775d124e82a57450dfe42c260a82823b37ebf70496c5d33a5b"


def test_ethereum_usdt_transfer_tx():
    tx_generator = TransferTxGenerator.erc20_usdt(private_key)
    raw_tx = tx_generator.generate_transfer_tx(to_address, amount_to_send, nonce)
    assert raw_tx == expected_raw_tx, "Wrong Tx"
