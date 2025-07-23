from pydantic import ValidationError

from utils.database import PostresDB
from utils.api_client import UserApiClient
from utils.data_provider.users import get_users_create_payload
from utils.data_provider.posts import get_user_post_create_payload
from utils.data_models.response_user import User
from utils.data_models.response_user_post import UserPost
from requests import Response
from utils.api_client import UserPostApiClient


class TestUsersAndPostsCreation:

    def test_user_created_in_api_and_db(self, db_client: PostresDB, user_api_client):
        user_dict: dict = get_users_create_payload()
        response: Response = user_api_client.create_user(data=user_dict)
        response_dict: dict = response.json()

        # assert response.status_code in (201, 204, 200)
        assert response.ok  # (201,200,204)
        keys = [key for key in get_users_create_payload().keys()]
        keys.append("id")
        try:
            User.model_validate(response.json())
        except ValidationError as e:
            print(f"Validation schema has been failed {e}")

        query: str = user_api_client.get_query_for_user_insert(username=user_dict["name"], gender=user_dict["gender"], email=user_dict["email"])

        db_client.mutation(query=query)

        assert len(db_client.select(f"SELECT * FROM users WHERE username = '{user_dict['name']}' and email = '{user_dict['email']}'")), \
            f"Not found record in db.users with username={user_dict['name']} and email={user_dict['email']}"

    def test_create_post_for_user_in_api_db(self, db_client: PostresDB, user_api_client, user_post_api_client):
        # creating a user in api
        user_dict: dict = get_users_create_payload()
        response: Response = user_api_client.create_user(data=user_dict)
        response_dict: dict = response.json()

        # assert response.status_code in (201, 204, 200)
        assert response.ok  # (201,200,204)
        try:
            User.model_validate(response.json())
        except ValidationError as e:
            print(f"Validation schema has been failed {e}")

        # creating same user in db.users
        query: str = user_api_client.get_query_for_user_insert(username=user_dict["name"], gender=user_dict["gender"], email=user_dict["email"])
        db_client.mutation(query=query)
        user_id_in_db = db_client.select(f"SELECT id FROM users WHERE username = '{user_dict['name']}' and email = '{user_dict['email']}'")[0][0]

        # creating user post in api
        user_post_data: dict = get_user_post_create_payload()
        response: Response = user_post_api_client.create_user_post(user_id=response_dict["id"], data=user_post_data)
        assert response.ok  # (201,200,204)
        try:
            UserPost.model_validate(response.json())
        except ValidationError as e:
            print(f"Validation schema has been failed {e}")

        query: str = user_post_api_client.get_query_for_user_post_insert(user_id_db=user_id_in_db,
                                                              title=user_post_data["title"],
                                                              body=user_post_data["body"])
        db_client.mutation(query=query)

        assert len(db_client.select(
            f"SELECT * FROM posts WHERE user_id='{user_id_in_db}' AND title='{user_post_data['title']}' AND body='{user_post_data['body']}'"
        ))














