import sqlite3, os
from roles import INITIAL_USERS

DB_PATH = os.environ.get('DB_PATH', 'reports.db')

def init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            rank        TEXT DEFAULT '',
            department  TEXT NOT NULL,
            role        TEXT NOT NULL,
            is_active   INTEGER DEFAULT 1,
            created_at  TEXT DEFAULT (datetime('now','localtime'))
        );

        CREATE TABLE IF NOT EXISTS weeks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date  TEXT NOT NULL UNIQUE,
            end_date    TEXT NOT NULL,
            label       TEXT
        );

        CREATE TABLE IF NOT EXISTS reports (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            week_id     INTEGER NOT NULL,
            data        TEXT NOT NULL DEFAULT '{}',
            submitted_at TEXT,
            updated_at  TEXT,
            UNIQUE(user_id, week_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (week_id) REFERENCES weeks(id)
        );
    ''')

    # Seed users if table is empty
    count = c.execute('SELECT COUNT(*) FROM users').fetchone()[0]
    if count == 0:
        for name, rank, dept, role in INITIAL_USERS:
            c.execute(
                'INSERT INTO users (name, rank, department, role) VALUES (?,?,?,?)',
                (name, rank, dept, role)
            )
        print(f'✓ {len(INITIAL_USERS)} алба хаагч нэмэгдлээ')

    conn.commit()
    conn.close()
    print('✓ Мэдээллийн сан бэлэн')

if __na