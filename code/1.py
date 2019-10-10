#!/usr/bin/env python
# -*-coding:utf-8-*-
# File Name     : 1.py
# Description   :
# Author        :
# Creation Date : 2019-10-09
# Last Modified : Wed 09 Oct 2019 02:58:47 PM CST
# Created By    : lsl


import asyncio
import aioredis

async def go(key, value):
    redis = await aioredis.create_redis_pool(
        'redis://localhost')
    await asyncio.sleep(1)
    await redis.set(key, value)
    val = await redis.get(key, encoding='utf-8')
    print(val)
    redis.close()
    await redis.wait_closed()



async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
            go('name1','lsl'),
            go('name2','lsl'),
            go('name3','lsl'),
    )

asyncio.run(main())
