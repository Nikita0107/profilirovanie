import asyncio
import aiohttp

async def fetch(session, url):
    # функция для отправки одного запроса
    async with session.get(url) as response:
        return await response.text()

async def send_requests(url, num_requests):
    rate_limit = 10  # ограничение на количество запросов

    async with aiohttp.ClientSession() as session:
        all_responses = []
        for i in range(0, num_requests, rate_limit):
            tasks = []
            batch_size = min(rate_limit, num_requests - i)
            for _ in range(batch_size):
                task = asyncio.create_task(fetch(session, url))
                tasks.append(task)
            # Выполняем группу задач
            batch_responses = await asyncio.gather(*tasks)
            all_responses.extend(batch_responses)
        return all_responses

if __name__ == "__main__":
    total_requests = 50
    request_url = 'http://google.com'

    responses = asyncio.run(send_requests(request_url, total_requests))

    for index, response_text in enumerate(responses):
        print(f'Ответ {index + 1}')