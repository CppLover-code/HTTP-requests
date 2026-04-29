# Библиотека aiohttp
"""
Что такое aiohttp

aiohttp — это библиотека для асинхронных HTTP-запросов в Python.

👉 Она работает вместе с asyncio и позволяет:

делать запросы к сайтам 🌐
работать с API
скачивать данные параллельно

Главная идея: не блокировать поток, а выполнять много задач одновременно.
"""

"""
Установка
pip install aiohttp
"""

# Базовый пример (GET запрос)
print("GET-запросы")

import aiohttp
import asyncio

async def main():
    url = "https://httpbin.org/get"
    # async with автоматически закрывает соединения
    async with aiohttp.ClientSession() as session:  # создаёт HTTP-сессию (как браузер)
        async with session.get(url) as response:    # отправляет GET-запрос
            print("Status:", response.status)       

            text = await response.text()            # # получает ответ
            print("Body:", text[:200])              # Первые 200 символов

asyncio.run(main())

print("***************************************************************************")

# еще один пример get запроса асинхронно и быстро
print("GET-запросы")
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status
        
async def main():
    tasks = []
    for _ in range(5):
        tasks.append(fetch("https://example.com"))

    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())

print("***************************************************************************")
print("GET-запросы")
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, "https://example.com")
            for _ in range(5)
        ]
        results = await asyncio.gather(*tasks)
        print(len(results))

asyncio.run(main())


print("***************************************************************************")
print("Параллельные запросы")
# Параллельные запросы

# Cписок URL, к которым обращаемся
urls = [
    "https://api.github.com",
    "https://google.com",
    "https://httpbin.org/get"
]

async def fetch(session,url):                           # объявление асинхронной функции
    try:                                                # (если сайт упадёт — программа не сломается)
        async with session.get(url) as r:               # отправляем HTTP GET запрос
            return url, r.status
    except Exception as e:
        return url, str(e)
    
async def main():
    async with aiohttp.ClientSession() as session:      # создаём одну HTTP-сессию, переиспользуется соединение
        tasks = [fetch(session, url) for url in urls]   # создаём список задач

        """
        Что делает gather:
            запускает ВСЕ задачи одновременно
            ждёт, пока все завершатся
            возвращает список результатов
        👉 именно тут происходит параллельность
        """
        results = await asyncio.gather(*tasks)          

        for url, result in results:
            print(url, result)

asyncio.run(main())

print("***************************************************************************")
print("POST запросы")
"""
POST — это HTTP-запрос, который используется, чтобы отправить данные на сервер.
GET → “дай мне данные”
POST → “вот тебе данные, обработай их”

📌 Примеры POST:

регистрация пользователя
отправка формы
создание записи в базе
отправка JSON в API

JSON (JavaScript Object Notation) — это формат передачи данных
"""

async def post_example():
    async with aiohttp.ClientSession() as session:
        async with session.post(                    # метод .post() = отправка данных
            "https://httpbin.org/post",
            json={"name":"Mark"}
        ) as resp:
            data = await resp.json()
            print(data)

asyncio.run(post_example())

print("***************************************************************************")
print("Загрузка файлов")
async def download_image():
    url = "https://picsum.photos/200"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()

            with open("image.jpg", "wb") as f:
                f.write(content)

asyncio.run(download_image())

print("***************************************************************************")
print("Ограничение количества запросов (очень важно)")
"""
максимум 3 запроса одновременно
остальные ждут своей очереди

📌 Без семафора:

все 10 запросов полетят сразу
можно перегрузить сервер или получить блокировку

📌 С семафором:

аккуратная очередь → стабильная работа
"""

import asyncio
import aiohttp

# asyncio.Semaphore(3) — это ограничитель количества одновременно выполняющихся задач.
sem = asyncio.Semaphore(3)

async def fetch(session, url):
    async with sem:
        async with session.get(url) as resp:
            return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, "https://example.com") for _ in range(10)]
        await asyncio.gather(*tasks)

asyncio.run(main())

print("***************************************************************************")
print("aiohttp как сервер (мини backend)")

"""
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, Mark!")

app = web.Application()
app.router.add_get("/", hello)

web.run_app(app, port=8080)
"""

print("***************************************************************************")
print("REST API пример")
from aiohttp import web

users = []

async def get_users(request):
    return web.json_response(users)

async def add_user(request):
    data = await request.json()
    users.append(data)
    return web.json_response({"added": data})

app = web.Application()

# ✅ сначала настраиваем
app.router.add_get("/users", get_users)
app.router.add_post("/users", add_user)

# ✅ потом запускаем
web.run_app(app, port=8080)
