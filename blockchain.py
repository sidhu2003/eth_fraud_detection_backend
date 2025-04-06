from web3 import Web3

# Connect to local Ethereum node (Docker)
WEB3_PROVIDER = "http://127.0.0.1:8545"  # Update with sender node URL
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Contract details
CONTRACT_ADDRESS = "0xYourDeployedContractAddress"  # Replace with your deployed contract address
CONTRACT_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_wallet", "type": "address"}],
        "name": "isBlocked",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "_wallet", "type": "address"}],
        "name": "blockWallet",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Load the contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def is_wallet_blocked(wallet_address):
    """Check if a wallet is blocked on the blockchain."""
    return contract.functions.isBlocked(wallet_address).call()

def block_wallet(wallet_address, sender_private_key):
    """Block a fraudulent wallet on the blockchain."""
    sender_account = web3.eth.account.privateKeyToAccount(sender_private_key)
    nonce = web3.eth.getTransactionCount(sender_account.address)

    txn = contract.functions.blockWallet(wallet_address).build_transaction({
        'chainId': 1337,  # Use appropriate chain ID
        'gas': 500000,
        'gasPrice': web3.to_wei('5', 'gwei'),
        'nonce': nonce
    })

    # Sign and send transaction
    signed_txn = web3.eth.account.sign_transaction(txn, sender_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)
