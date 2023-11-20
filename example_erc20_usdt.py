from dotenv import dotenv_values
from src.tx_managers.transfer_tx_generator import TransferTxGenerator

config = dotenv_values(".env")


private_key = config["ETHEREUM_PRIVATE_KEY"]
to_address = "0x80583D6eFC0c324818e0811bF641d37B4D8fb0FC"
amount_to_send = 1
nonce = 4

tx_generator = TransferTxGenerator.erc20_usdt(private_key)
raw_tx = tx_generator.generate_transfer_tx(to_address, amount_to_send, nonce)

print("Generated Raw Transaction")
print(raw_tx)
