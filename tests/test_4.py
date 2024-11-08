from aioresponses import aioresponses
from status_code import make_requests
import os

async def test_make_requests(tmp_path):
    url = "https://example.com/"
    total_requests = 5
    limit = 2
    output_file = tmp_path / "responses.txt"

    with aioresponses() as mocked:
        for _ in range(total_requests):
            mocked.get(url, status=200)

        await make_requests(url, total_requests, limit, str(output_file))

    assert os.path.exists(output_file)

    with open(output_file, 'r') as f:
        lines = f.readlines()

    assert len(lines) == total_requests

    for line in lines:
        assert line.strip() == "Status: 200"
