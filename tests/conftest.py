import os
import pytest
@pytest.fixture
async def cleanup_files():
    # Фикстура для очистки созданных файлов перед и после тестов
    folder_name = 'created_files'
    # Перед тестом: удаляем папку, если она существует
    if os.path.exists(folder_name):
        for filename in os.listdir(folder_name):
            file_path = os.path.join(folder_name, filename)
            os.remove(file_path)
        os.rmdir(folder_name)
    yield
    # После теста: удаляем папку и файлы
    if os.path.exists(folder_name):
        for filename in os.listdir(folder_name):
            file_path = os.path.join(folder_name, filename)
            os.remove(file_path)
        os.rmdir(folder_name)
