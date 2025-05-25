import asyncio
import aiosqlite
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "users.db"

async def async_fetch_users():
    async with aiosqlite.connect(str(DB_PATH)) as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        await cursor.close()
        print("All Users:")
        return rows

async def async_fetch_older_users():
    async with aiosqlite.connect(str(DB_PATH)) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        await cursor.close()
        print("\nUsers older than 40:")
        return rows

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
