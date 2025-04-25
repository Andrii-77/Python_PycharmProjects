import time
import requests
import uuid
import asyncio
import httpx


def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(time_end - time_start)

    return wrapper


# def get_res(url):
#     return requests.get(url=url, allow_redirects=True)
#
#
# def write_file(res: requests.Response):
#     file_name = str(uuid.uuid4()) + ".jpg"
#     with open(file_name, "wb") as f:
#         f.write(res.content)
#
#
# @time_decorator
# def main():
#     url = 'https://loremflickr.com/320/240/dog'
#     for _ in range(50):
#         write_file(get_res(url))
#
#
# main()


def write_file(data):
    file_name = str(uuid.uuid4()) + ".jpg"
    with open(file_name, "wb") as f:
        f.write(data)


async def get_res(url, client: httpx.AsyncClient):
    res = await client.get(url, follow_redirects=True)
    write_file(res.read())


async def start():
    url = 'https://loremflickr.com/320/240/dog'
    tasks = []
    async with httpx.AsyncClient() as client:
        for _ in range(50):
            task = asyncio.create_task(get_res(url, client))
            tasks.append(task)
        await asyncio.gather(*tasks)


@time_decorator
def main():
    asyncio.run(start())


main()
