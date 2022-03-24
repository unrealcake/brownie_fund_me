from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    # check if MockV3Aggregator is already deployed or not
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            # add 18 decimals to 2000
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()},
        )
        # use the most recently deployed MockV3Aggregator
        print("Mocks Deployed!")
