import asyncio
import random
import cProfile
from memory_profiler import profile

def time_prof(func):
    # Декоратор для профилирования времени!
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()  # Создаем профайлер
        pr.enable()  # Включаем профайлер
        result = func(*args, **kwargs)  # Вызываем функцию
        pr.disable()  # Отключаем профайлер

        # Печатаем результаты по времени
        print('Профилирование по времени:')
        pr.print_stats(sort='cumulative')  # Сортируем и выводим результаты
        return result  # Возвращаем результат оригинальной функции
    return wrapper

@time_prof
@profile
async def async_number(number):
    lst = []
    for n in range(1, int(number ** 0.5) + 1):
        if number % n == 0:
            lst.append(n)
            if n != number // n:
                lst.append(number // n)
    return sorted(lst)

async def main():
    number = random.randint(1_000_000, 20_000_000)  # Генерация числа
    print(f'Случайно выбранное число: {number}')

    divisors = await async_number(number)  # Вызываем функцию для получения делителей
    print(f'Делители числа {number}: {divisors}')

# Запуск основной функции
if __name__ == "__main__":
    asyncio.run(main())