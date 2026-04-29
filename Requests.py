# Создаём запросы с requests
# pip install requests

# импортируем модуль time, чтобы можно было засекать время
import time
# импортируем библиотеку requests для запросов
import requests

# пишем основной адрес, куда будем слать запросы
BASE_URL = "https://postman-echo.com"


# пишем функцию GET-запроса
def fetch_get():
   # объявляем переменную, в которой отправляем GET-запрос на нужный адрес
   response = requests.get(f"{BASE_URL}/get")
   # возвращаем статус-код от сервера и ответ в формате JSON
   return response.status_code, response.json()


# пишем функцию POST-запроса
def fetch_post():
   # объявляем переменную и указываем, что нужно добавить
   data_to_post = {"key": "value"}
   # объявляем переменную, в которой отправляем POST-запрос на нужный адрес
   response = requests.post(f"{BASE_URL}/post", json=data_to_post)
   # возвращаем статус-код от сервера и ответ в формате JSON
   return response.status_code, response.json()


# пишем функцию PUT-запроса
def fetch_put():
   # объявляем переменную и указываем, что нужно обновить
   data_to_put = {"key": "updated_value"}
   # объявляем переменную, в которой отправляем PUT-запрос на нужный адрес
   response = requests.put(f"{BASE_URL}/put", json=data_to_put)
   # возвращаем статус-код от сервера и ответ в формате JSON
   return response.status_code, response.json()


# пишем функцию DELETE-запроса
def fetch_delete():
   # объявляем переменную, в которой отправляем DELETE-запрос на нужный адрес
   response = requests.delete(f"{BASE_URL}/delete")
   # возвращаем статус-код от сервера и ответ в формате JSON
   return response.status_code, response.json()


# пишем основную функцию
def main():
   # начинаем отсчёт времени
   start = time.perf_counter()

   # выполняем GET-запрос
   status_code, response_json = fetch_get()
   # выводим код ответа от сервера и содержимое ответа
   print(f"GET Status Code: {status_code}")
   print(f"GET Response: {response_json}")
   # выполняем POST-запрос
   status_code, response_json = fetch_post()
   # выводим код ответа от сервера и содержимое ответа
   print(f"POST Status Code: {status_code}")
   print(f"POST Response: {response_json}")
   # выполняем PUT-запрос
   status_code, response_json = fetch_put()
   # выводим код ответа от сервера и содержимое ответа
   print(f"PUT Status Code: {status_code}")
   print(f"PUT Response: {response_json}")
   # выполняем DELETE-запрос
   status_code, response_json = fetch_delete()
   # выводим код ответа от сервера и содержимое ответа
   print(f"DELETE Status Code: {status_code}")
   print(f"DELETE Response: {response_json}")

   # останавливаем отсчёт времени и выводим результат,
   # округляя до двух цифр после запятой
   end = time.perf_counter()
   print(f"Time taken: {end - start:.2f} seconds.")


# запускаем основную функцию
main()