# тестовое простое

# Написать скрипт-замерятель скорости интернета со своего компьютера.

# Он должен принимать адрес, куда стучаться (какая-нибудь тяжелая картинка) , за
# пускать последовательно 10 запросов к этому адресу, дожидаться ответа, вычислять сред
# нее время запроса, объем скачанных данных и печатать в консоли скорость мб/с.

# Ответ залить на github и дать репозиторий с инструкциями.

import requests
import time

def get_url(url, timeout=10):
    time_start = time.perf_counter()
    res = requests.get(url, timeout=timeout)
    res.raise_for_status()
    return time.perf_counter() - time_start, len(res.content)
    
def speed_test(url: str) -> float:
    times = 0
    len_content = 0 
    for i in range(10):
        res_time, content = get_url(url)
        times += res_time
        len_content += content

    return (len_content * 8) / 1000000 / times
    
input_url = input("Введите адрес для теста скорости: ")
print("{:.2f}".format(speed_test(input_url)), "Мбит/с")
    