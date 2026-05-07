import allure
from app.db import get_connection

@allure.feature("Database connection")
def test_connection():
    with allure.step("Connect to database"):
        conn = get_connection()

    with allure.step("Check connection is not None"):
        assert conn is not None

    conn.close()

@allure.feature("Insert user")
def test_insert():
    conn = get_connection()
    cur = conn.cursor()

    with allure.step("Insert new user"):
        cur.execute("INSERT INTO users (name) VALUES ('Test User') RETURNING id;")
        user_id = cur.fetchone()[0]

    with allure.step("Commit transaction"):
        conn.commit()

    with allure.step("Verify user id created"):
        assert user_id is not None

    cur.close()
    conn.close()

@allure.feature("Select users")
def test_select():
    conn = get_connection()
    cur = conn.cursor()

    with allure.step("Select all users"):
        cur.execute("SELECT * FROM users;")
        data = cur.fetchall()

    with allure.step("Verify result is list"):
        assert isinstance(data, list)

    cur.close()
    conn.close()

@allure.feature("Update and delete user")
def test_update_delete():
    conn = get_connection()
    cur = conn.cursor()

    with allure.step("Insert temp user"):
        cur.execute("INSERT INTO users (name) VALUES ('Temp') RETURNING id;")
        user_id = cur.fetchone()[0]

    with allure.step("Update user"):
        cur.execute("UPDATE users SET name='Updated' WHERE id=%s;", (user_id,))

    with allure.step("Delete user"):
        cur.execute("DELETE FROM users WHERE id=%s;", (user_id,))

    with allure.step("Commit changes"):
        conn.commit()

    cur.close()
    conn.close()