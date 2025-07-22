import psycopg2

class TestDocker:
    def test_database_connection(self):
        conn = psycopg2.connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="localhost",
            port="5434"
        )
        assert conn is not None

    def test_data_insertion(self):
        conn = psycopg2.connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="db",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id=1")
        result = cursor.fetchone()
        assert result[1] == 'John'