# import asyncio
# import aiofiles
# import os
#
# async def create_file(index):
#     folder_name = 'created_files'
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#
#     filename = f'{folder_name}/file_{index}.txt'
#     async with aiofiles.open(filename, 'w') as f:
#         await f.write(str(index))
#
# async def main_create():
#    # Создаем 10 файлов параллельно
#     tasks = [asyncio.create_task(create_file(i)) for i in range(10)]
#     await asyncio.gather(*tasks)
#
# # Запуск основной функции
# if __name__ == "__main__":
#     asyncio.run(main_create())

import asyncio
import aiofiles
import os
import cProfile
import tracemalloc

def time_profile(func):
    # Декоратор для профилирования времени выполнения функции.
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()  # Создаем профайлер
        pr.enable()  # Включаем профайлер
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        pr.disable()  # Отключаем профайлер

        # Печатаем результаты профилирования по времени
        print('Профилирование по времени:')
        pr.print_stats(sort='cumulative')  # Сортируем и выводим результаты
        return result  # Возвращаем результат оригинальной функции
    return wrapper

async def create_file(index):
    folder_name = 'created_files'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    filename = f'{folder_name}/file_{index}.txt'
    async with aiofiles.open(filename, 'w') as f:
        await f.write(str(index))

@time_profile  # Применяем декоратор для профилирования времени
async def main_create():
    # Инициализация профилирования памяти
    tracemalloc.start()

    # Создаем 10 файлов параллельно
    tasks = [asyncio.create_task(create_file(i)) for i in range(10)]
    await asyncio.gather(*tasks)

    # Получаем текущее состояние памяти
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[TOP 10 MEMORY USAGE]")
    for stat in top_stats[:10]:
        print(stat)

    tracemalloc.stop()  # Останавливаем профилирование памяти

# Запуск основной функции
if __name__ == "__main__":
    asyncio.run(main_create())