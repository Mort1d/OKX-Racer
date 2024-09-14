API_ID = 123
API_HASH = 'API_HASH'

DELAYS = {
    'ACCOUNT': [5, 15],  # задержка между подключениями к аккаунтам (чем больше аккаунтов, тем дольше задержка)
    'PREDICT': [5, 8],   # задержка после прогноза
    'TASK': [2, 3],      # задержка после выполнения задачи
    'REPEAT': [100, 180] # задержка для повторений
}

INVITE_CODE = 'linkCode_26194459' #ваш реферальный код

BOOST_TURBO_CHARGER = False # True - покупка буста, False - не покупать буст

BLACKLIST_TASKS = ['Connect Telegram and complete identity verification', 'Подключите Telegram и пройдите верификацию личности', 'Подключение TON к кошельку OKX']


PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - если использовать прокси из файла, False - если использовать прокси из accounts.json
    "PROXY_PATH": "data/proxy.txt",  # путь к файлу с прокси
    "TYPE": {
        "TG": "socks5",  # тип прокси для клиента tg. Поддерживаются "socks4", "socks5" и "http"
        "REQUESTS": "socks5"  # тип прокси для запросов. "http" для https и http прокси, "socks5" для socks5 прокси.
    }
}

# папка для сессий
WORKDIR = "sessions/"

# тайм-аут в секундах для проверки валидности аккаунтов
TIMEOUT = 30