import pytest
from main import async_number

def get_all_divisors(number):
    divisors = []
    for n in range(1, int(number ** 0.5) + 1):
        if number % n == 0:
            divisors.append(n)
            if n != number // n:
                divisors.append(number // n)
    return sorted(divisors)

async def test_async_number():
    test_cases = [
        (10, [1, 2, 5, 10]),
        (15, [1, 3, 5, 15]),
        (1, [1]),
        (28, [1, 2, 4, 7, 14, 28]),
        (1000, get_all_divisors(1000)),           # Используем 1000 для теста
        (1_000_000, get_all_divisors(1_000_000))  # Вычисляем ожидаемые делители автоматически
    ]

    for number, expected_divisors in test_cases:
        divisors = await async_number(number)
        assert sorted(divisors) == expected_divisors

if __name__ == "__main__":
    pytest.main()

#
# from main import async_number
# import asyncio
# from memory_profiler import profile
# import cProfile
# import pstats
# import io
#
#
# def get_all_divisors(number):
#     divisors = []
#     for n in range(1, int(number ** 0.5) + 1):
#         if number % n == 0:
#             divisors.append(n)
#             if n != number // n:
#                 divisors.append(number // n)
#     return sorted(divisors)
#
#
# async def test_async_number():
#     test_cases = [
#         (10, [1, 2, 5, 10]),
#         (15, [1, 3, 5, 15]),
#         (1, [1]),
#         (28, [1, 2, 4, 7, 14, 28]),
#         (1000, get_all_divisors(1000)),
#         (1_000_000, get_all_divisors(1_000_000))
#     ]
#
#     for number, expected_divisors in test_cases:
#         divisors = await async_number(number)
#         assert sorted(divisors) == expected_divisors
#
#
# @profile
# def run_profiled_test():
#     asyncio.run(test_async_number())
#
#
# def run_test_with_profiling():
#     pr = cProfile.Profile()
#     pr.enable()
#
#     run_profiled_test()
#
#     pr.disable()
#     s = io.StringIO()
#     ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
#     ps.print_stats()
#     print(s.getvalue())
#
#
# if __name__ == "__main__":
#     run_test_with_profiling()