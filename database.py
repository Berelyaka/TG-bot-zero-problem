import sqlite3
from datetime import datetime, timedelta


DB_NAME = "vpn_bot.db"

def has_used_promo(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT promo_used FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return row[0] == 1
    return False


def mark_promo_used(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET promo_used = 1 WHERE user_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()



def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            created_at TEXT,
            promo_used INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            region TEXT,
            expires_at TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, created_at) VALUES (?, ?)",
        (user_id, datetime.utcnow().isoformat())
    )

    conn.commit()
    conn.close()


def add_subscription(user_id: int, region: str, days: int):
    from datetime import datetime, timedelta

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT expires_at FROM subscriptions
        WHERE user_id = ?
        ORDER BY expires_at DESC
        LIMIT 1
    """, (user_id,))

    row = cursor.fetchone()

    now = datetime.utcnow()

    if row:
        current_expiry = datetime.fromisoformat(row[0])
        if current_expiry > now:
            new_expiry = current_expiry + timedelta(days=days)
        else:
            new_expiry = now + timedelta(days=days)
    else:
        new_expiry = now + timedelta(days=days)

    cursor.execute("""
        INSERT INTO subscriptions (user_id, region, expires_at)
        VALUES (?, ?, ?)
    """, (user_id, region, new_expiry.isoformat()))

    conn.commit()
    conn.close()


def get_active_subscription(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT region, expires_at
        FROM subscriptions
        WHERE user_id = ?
        ORDER BY expires_at DESC
        LIMIT 1
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    region, expires_at = row
    expires_dt = datetime.fromisoformat(expires_at)

    if expires_dt > datetime.utcnow():
        formatted_date = expires_dt.strftime("%d.%m.%Y %H:%M")
        return region, formatted_date

    return None