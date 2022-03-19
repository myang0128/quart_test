import asyncio

import aiohttp
import uvicorn as uvicorn
from quart import Quart

from config import appConfig

app = Quart(__name__)

urls = [appConfig.TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL,
        appConfig.PERFORMANCE_CHART_DATA_URL,
        appConfig.OPPORTUNITIES_BOOKED_URL]


async def call_url(session, url):
    async with session.get(url) as resp:
        r = await resp.json()
        return r


@app.route('/test')
async def test():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(call_url(session, url)))
        result = await asyncio.gather(*tasks)
        for r in result:
            print(r)
        return {'a': result}


if __name__ == '__main__':
    uvicorn.run(app, debug=True, port=int(appConfig.PORT), host='127.0.0.1')
