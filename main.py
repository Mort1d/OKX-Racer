import os
import asyncio
import pyfiglet
from data import config
from colorama import Fore, init
from utils.core.telegram import Accounts
from utils.starter import start, stats
import warnings

init(autoreset=True)
warnings.filterwarnings("ignore", category=DeprecationWarning)

async def run_application():
    banner = pyfiglet.figlet_format("SAMURAI   SOFT")
    print(Fore.RED + banner)

    choice = int(input("Выберите действие:\n0. Запуск\n1. Получить статистику\n2. Создание сессий\n\n> "))

    if not os.path.exists('sessions'):
        os.mkdir('sessions')

    if config.PROXY['USE_PROXY_FROM_FILE']:
        if not os.path.exists(config.PROXY['PROXY_PATH']):
            open(config.PROXY['PROXY_PATH'], 'w').close()
    else:
        if not os.path.exists('sessions/accounts.json'):
            open('sessions/accounts.json', 'w').close()

    if choice == 2:
        await Accounts().create_sessions()
    elif choice == 1:
        await stats()
    elif choice == 0:
        account_list = await Accounts().get_accounts()
        tasks = [asyncio.create_task(start(session_name=acc['session_name'], phone_number=acc['phone_number'], thread=idx, proxy=acc['proxy'])) for idx, acc in enumerate(account_list)]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(run_application())

