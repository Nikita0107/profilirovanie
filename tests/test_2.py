import os
import aiofiles
from creatt import create_file, main_create

async def test_create_file(cleanup_files):
    # Тестирует create_file
    index = 5
    await create_file(index)
    folder_name = 'created_files'
    filename = f'{folder_name}/file_{index}.txt'
    assert os.path.exists(filename), f"Файл {filename} не был создан"

    # Проверяем содержимое файла
    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()

        assert content == str(index), f"Содержимое файла {filename} неверно"
async def test_main_create(cleanup_files):
    await main_create()
    folder_name = 'created_files'

    for i in range(10):
        filename = f'{folder_name}/file_{i}.txt'
        assert os.path.exists(filename), f"Файл {filename} не был создан"

        # Проверяем содержимое файла
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
            assert content == str(i), f"Содержимое файла {filename} неверно"