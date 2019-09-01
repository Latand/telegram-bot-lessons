import asyncio
import asyncpg
import logging


async def create_db():
    create_db_command = open("create_db.sql", "r").read()

    conn: asyncpg.Connection = await asyncpg.connect(user='postgres', password='example',
                                                     host='localhost')
    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table users created")


async def create_pool():
    return await asyncpg.create_pool(user='postgres', password='example',
                                     host='localhost')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
