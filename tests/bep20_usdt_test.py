from dotenv import dotenv_values
from src.tx_managers.transfer_tx_generator import TransferTxGenerator

config = dotenv_values(".env")

private_key = config["BNB_TEST_PRIVATE_KEY"]
to_address = "0x80583D6eFC0c324818e0811bF641d37B4D8fb0FC"
amount_to_send = 1
nonce = 100
expected_raw_tx = "0xf8aa6484b2d05e00830111709455d398326f99059ff775485246999027b319795580b844a9059cbb00000000000000000000000080583d6efc0c324818e0811bf641d37b4d8fb0fc0000000000000000000000000000000000000000000000000de0b6b3a76400008194a0d3f6de24127187dbbb6b97eef9b9d95c3c96d70608a2261f4265d7b49da8a662a045e9b8a953a6a3cc8e5bcc66ac839b964c7d97476265310802f6500fb356a7b1"


def test_bep20_usdt_transfer_tx():
    tx_generator = TransferTxGenerator.bep20_usdt(private_key)
    raw_tx = tx_generator.generate_transfer_tx(to_address, amount_to_send, nonce)
    assert raw_tx == expected_raw_tx, "Wrong Tx"
