from app.db import get_connection

def test_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()


def test_insert():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES ('Test User') RETURNING id;")
    user_id = cur.fetchone()[0]

    conn.commit()
    assert user_id is not None

    cur.close()
    conn.close()


def test_select():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    data = cur.fetchall()

    assert isinstance(data, list)

    cur.close()
    conn.close()


def test_update_delete():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES ('Temp') RETURNING id;")
    user_id = cur.fetchone()[0]

    cur.execute("UPDATE users SET name='Updated' WHERE id=%s;", (user_id,))
    cur.execute("DELETE FROM users WHERE id=%s;", (user_id,))

    conn.commit()

    cur.close()
    conn.close()