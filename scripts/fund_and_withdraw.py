from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = fund_me = FundMe.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    somePrice = fund_me.getPrice()
    # print(somePrice)
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    print("Withdrawing...")
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("Withdraw complete")


def main():
    fund()
    withdraw()
