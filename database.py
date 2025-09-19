import aiosqlite

DB_NAME = "data.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS warnings (
            user_id TEXT,
            reason TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.commit()

async def add_warning(user_id, reason):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO warnings (user_id, reason) VALUES (?, ?)",
            (user_id, reason)
        )
        await db.commit()

async def get_warnings(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT reason, timestamp FROM warnings WHERE user_id = ?",
            (user_id,)
        )
        rows = await cursor.fetchall()
        return rows
