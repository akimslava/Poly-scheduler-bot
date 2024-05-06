import asyncio
import json

import httpx

from config import *


async def getData(url: str) -> json:
    async with httpx.AsyncClient() as client:
        return (await client.get(url=url)).json()


def is_groupId_correct(group_id: int) -> bool:
    if group_id <= 0:
        return False

    loop = asyncio.get_event_loop()

    try:
        url = SCHEDULE_URL.format(group_id)
        data = loop.run_until_complete(asyncio.gather(getData(url)))[0]
        return data['error'] is None
    except:
        return True


def is_int(text: str) -> bool:
    try:
        int(text)
        return True
    except:
        return False


if __name__ == "__main__":
    value = is_groupId_correct(38734)
    print(value)
