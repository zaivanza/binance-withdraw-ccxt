import time
import ccxt
from termcolor import cprint
import random

API_KEY = ""
API_SECRET = ""


def binance_withdraw(address, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET):

    try:
        account_binance.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "network": network
            }
        )
        cprint(f">>> Успешно | {address} | {amount_to_withdrawal}", "green")
    except Exception as error:
        cprint(f">>> Неудачно | {address} | ошибка : {error}", "red")


if __name__ == "__main__":

    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]

    account_binance = ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    balances = account_binance.fetch_balance()['info']['balances']
    for i in balances:
        if i['asset'] == 'ETH':
            balance = i['free']
            print(f'Your ETH balance is {balance}')
            break

    symbolWithdraw = 'ETH'
    network = ''

    network_input = int(
        input('Select Chain (min amount): \n 1. ETH 0.0098 \n 2. ARB 0.0008 \n 3. OP 0.001 \n 4. BSC 0.00011 \n '))

    match (network_input):
        case (1):
            network = 'ETH'
        case (2):
            network = 'Arbitrum'
        case (3):
            network = 'Optimism'
        case (4):
            network = 'BSC'

    amount_input = float(input('Input amount of ETH: '))

    cprint('\a\n/// start withdrawing...', 'white')
    for wallet in wallets_list:
        # amount from ... to ...
        amount_to_withdrawal = amount_input
        binance_withdraw(wallet, amount_to_withdrawal,
                         symbolWithdraw, network, API_KEY, API_SECRET)
        time.sleep(random.randint(10, 30))
