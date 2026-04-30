"""
API (Application Programming Interface) — язык, на котором приложения общаются 
между собой. С помощью API одно приложение может использовать возможности другого 
приложения. Например, интернет-магазин может вызывать банковские сервисы для оплаты 
покупок.
"""
"""
REST = REpresentational State Transfer
клиент (браузер / приложение) → отправляет запрос → сервер → возвращает ответ (обычно JSON)
Важна суть: ресурсы + HTTP методы
"""
"""
🔑 HTTP методы (самое важное)
Метод	        Что делает	        Пример
GET	            получить данные	    получить список пользователей
POST	        создать	            создать нового пользователя
PUT	            полностью обновить	заменить пользователя
PATCH	        частично обновить	изменить имя
DELETE	        удалить	            удалить пользователя
"""

# Пример на Python (aiohttp клиент)
import aiohttp
import asyncio

async def get_users():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/users") as resp:
            data = await resp.json()
            print(data)

asyncio.run(get_users())


# Пример backend (как это выглядит на сервере)
from aiohttp import web
# Импортируем модуль web из библиотеки aiohttp
# Это фреймворк для создания асинхронных веб-серверов на Python
async def get_users(request):            # асинхронная функция (обработчик)
    # request — объект, в котором лежат данные запроса, параметры, headers, тело запроса
    return web.json_response([           # Возвращаем ответ в формате JSON
        {"id": 1, "name": "Mark"}
    ])

app = web.Application()                  # Создаём экземпляр веб-приложения, это ядро сервера, где
                                         # регистрируются марщруты, настраиваются middleware,
                                         # хранится логика приложения
app.router.add_get("/users", get_users)  # Регистрация маршрута (endpoint)
web.run_app(app)                         # Запуск сервера

