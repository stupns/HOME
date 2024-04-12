import asyncio
import httpx
from PIL import Image
from io import BytesIO


async def download(query, current_page):
    header = {'Authorization': '563492ad6f9170000100000126aed25ca48640d39996f7dcf69fdc59'}
    params = {'query': query, 'per_page': 1, 'page': current_page}
    url = f'https://api.pexels.com/v1/search'

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get('photos'):
                # print(f"{item.get('src').get('original')}")
                _img_url = item.get('src').get('original')

                resp = await client.get(_img_url)
                image = Image.open(BytesIO(resp.content))
                image.save(f"media/{query}_{current_page}.{_img_url.split('.')[-1]}")
        else:
            print(r.status_code)
    print(f'{query} = {current_page}')


async def main() -> None:
    queue = asyncio.Queue()

    query = input('Search: ')
    page_count = int(input('Count page: '))

    current_page = 0
    task_list = []
    while current_page < page_count:
        current_page += 1
        # await download(query, current_page)
        task = asyncio.create_task(download(query, current_page))
        task_list.append(task)

    await queue.join()
    await asyncio.gather(*task_list, return_exceptions=True)

    print('done')


asyncio.run(main())
