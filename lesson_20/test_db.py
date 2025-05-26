from lesson_20.database import PostresDB
import faker
fake = faker.Faker()


class TestUsers:

    db_client = PostresDB()

    def test_create_user_is_successful(self):
        try:
            last_id: int = self.db_client.select("SELECT id FROM users ORDER BY id DESC LIMIT 1")[0][0]
            user_name: str = fake.user_name()
            self.db_client.mutation(query=f"INSERT INTO users (name) VALUES ('{user_name}')")
            actual_result = self.db_client.select(query=f"SELECT * FROM users WHERE name='{user_name}'")
            assert actual_result[0] == last_id + 1
        finally:
            self.db_client.close()
