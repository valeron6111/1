import json
from jsonpath_ng import jsonpath, parse

# Открываем файл и загружаем его содержимое в переменную data
response = requests.get("https://raw.githubusercontent.com/valeron6111/1/main/data.json")
data = response.json()

# Используем jsonpath для получения списка кодов активных и основных подписок
codes_expr = parse("$.[?(@.primary && @.active)].code")
codes = [match.value for match in codes_expr.find(data)]

# Для каждого кода подписки ищем процент на остаток используя jsonpath
for code in codes:
    rate_expr = parse(f"$.[?(@.primary && @.active && @.code=='{code}')].details[?(@.code=='tbundle_cu_interest_rate')].toBe")
    rate = rate_expr.find(data)
    if rate:
        print(f"Процент на остаток для подписки {code}: {rate[0].value}")
    else:
        print(f"Для подписки {code} процент на остаток не найден.")
