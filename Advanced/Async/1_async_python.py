import asyncio
import time
import aiohttp
import requests
import certifi
import ssl

# Define the URLs for making requests.
URLS = [
    'https://google.com',
    'https://www.youtube.com/',
    'https://www.djangoproject.com/',
    'https://www.python.org/',
    'https://www.wikipedia.org/'
]

# Create an SSL context using certifi to ensure up-to-date CA certificates.
ssl_context = ssl.create_default_context(cafile=certifi.where())


def time_tracker(func):
    """Decorator for measuring execution time of both sync and async functions."""

    async def async_wrapper(*args, **kwargs):
        start = time.time()
        await func(*args, **kwargs)
        end = time.time() - start
        print(f'Function {func.__name__} completed in {end} seconds.')

    def sync_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start
        print(f'Function {func.__name__} completed in {end} seconds.')

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper


async def make_async_request(idx, url, session: aiohttp.ClientSession) -> None:
    """Asynchronous request to URL."""
    async with session.get(url, ssl=ssl_context) as response:
        status = 'success' if 200 <= response.status < 300 else 'failure'
        print(f'{idx} | {url}: {status}')


def make_sync_request(idx, url) -> None:
    """Synchronous request to URL."""
    response = requests.get(url, verify=certifi.where())
    status = 'success' if 200 <= response.status_code < 300 else 'failure'
    print(f'{idx} | {url}: {status}')


async def async_run(count: int) -> None:
    """Send count asynchronous requests."""
    tasks = []
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        for i in range(count):
            task = make_async_request(i, URLS[i % len(URLS)], session)
            tasks.append(task)
        await asyncio.gather(*tasks)


def sync_run(count: int) -> None:
    """Send count synchronous requests."""
    for i in range(count):
        make_sync_request(i, URLS[i % len(URLS)])


@time_tracker
async def async_main() -> None:
    """Main async function."""
    await async_run(100)


@time_tracker
def sync_main() -> None:
    """Main sync function."""
    sync_run(30)


if __name__ == '__main__':
    # Run async_main or sync_main based on your testing preference.
    # asyncio.run(async_main())
    sync_main()
