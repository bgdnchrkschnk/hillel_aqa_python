from unittest import main, TestCase
from lesson_09.func import add, danger_zone



class TestMathUtils(TestCase):

    def test_add(self):
        self.assertEqual(5, add(2, 4))
        self.assertEqual(add(-1, 1), 2)
        self.assertEqual(add(0, 0), 0)


    def test_new_user_in_db(self, selenium_obj, db_client):
        """
        Creating a user and checking if it exists in db
        """
        user_data: dict = {"name": "Bohdan",
                           "email": "test@gmail.com"}
        selenium_obj.new_user(**user_data)
        db_users: list[dict] = db_client.get_users_in_db()
    #
    #     self.assertTrue(user_data in db_users) # user_data in db_users

    def test_upper(self):
        name = "bohdan"
        # self.assertEqual("bhjebchjbN", name.upper()) # "BOHDAN", name.upper()
        assert name.upper() != "saadsadsa"
        assert "a" in "angel"
        self.assertIsNone(None, None)
        users = db.get_users()
        assert users is None


    # def test_true(self):
    #     first_number: int = 9
    #     second_number: int = 2
    #     # self.assertTrue(first_number < second_number)
    #     assert first_number < second_number, f"{first_number} not less than {second_number}"
    #
    def test_false(self):
        self.assertFalse(3 < 2)
        assert not 3 < 2

    # def test_in(self):
    #     self.assertIn("a", "plum", msg="'a' is not in obj")
    #     assert "a" in "apple", f"a not in apple"

    def test_not_in(self):
        self.assertNotIn("a", "plum")
        assert "a" not in "plum"


    def test_addition(self):
        result = 0.1 + 0.2
        expected = 0.3
        print(f"result = {result}")  # виведе 0.30000000000000004

        # Звичайна перевірка не пройде:
        # self.assertEqual(result, expected)  # Це впаде!

        # А ось ця працює:
        self.assertAlmostEqual(result, expected, places=6)

    def test_is_none(self):
        self.assertIsNone(None)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            result: float = 1 / 0
        with self.assertRaises(TypeError):
            result = "abc" - 22

    # def test_warning_logged(self):
    #     with self.assertLogs('logger_module', level='WARNING') as cm:
    #         danger_zone()

        # self.assertIn("⚠️ Увага! Ви входите в небезпечну зону!", cm.output[0])

if __name__ == '__main__':
    main(verbosity=1)