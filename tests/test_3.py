from aioresponses import aioresponses
from Google_queries import send_requests

async def test_send_requests():
    url = "http://test.com"
    num_requests = 5  # Тестируем с 5 запросами

    with aioresponses() as mocked:
        # Настраиваем фейковые ответы
        for i in range(num_requests):
            mocked.get(url, body=f"Response {i + 1}")

        # Выполняем тестируемую функцию
        responses = await send_requests(url, num_requests)

    # Проверяем, что количество полученных ответов соответствует числу запросов
    assert len(responses) == num_requests

    # Проверяем, что каждый ответ соответствует ожидаемому
    for i, response in enumerate(responses):
        assert response == f"Response {i + 1}"
