import pytest
import helper_user


@pytest.fixture
def user_fixture():
    user_data = helper_user.create_user_with_unique_data()
    yield user_data
    helper_user.delete_user(user_data[3])

