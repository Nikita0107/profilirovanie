import aiohttp
import asyncio
import ssl
from aiohttp import ClientSession
from asyncio import Semaphore

async def fetch(session: ClientSession, url: str, semaphore: Semaphore):
    async with semaphore:
        # Выполняем асинхронный GET-запрос к указанному URL без проверки SSL-сертификата
        async with session.get(url, ssl=False) as response:
            return response.status

async def make_requests(url: str, total_requests: int, limit: int, output_file: str):
    semaphore = Semaphore(limit)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, semaphore) for _ in range(total_requests)]
        responses = await asyncio.gather(*tasks)

    with open(output_file, 'w') as f:
        # Записываем статус-код каждого ответа в файл
        for status in responses:
            f.write(f"Status: {status}\n")

# основная функция
async def main():
    url = "https://example.com/"
    total_requests = 50
    limit = 10
    output_file = "responses.txt"

    await make_requests(url, total_requests, limit, output_file)


if __name__ == "__main__":
    asyncio.run(main())