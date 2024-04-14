import helper_user
import allure
from faker import Faker


class TestUserCreation:

    @allure.title('Создание пользователя проходит успешно')
    @allure.description('Проверяем, что после создания пользователя возвращается код 200')
    def test_user_creation(self):
        fake = Faker()
        email = fake.first_name() + "@yandex.ru"
        password = fake.last_name()
        name = fake.first_name()
        response = helper_user.create_user(email, password, name)
        access_token = helper_user.get_access_token(response)
        helper_user.delete_user(access_token)
        assert (response.status_code == 200
                and response.json()['success'] == True
                and response.json()['user']['email'] == email.lower()
                and response.json()['user']['name'] == name
                and response.json()['accessToken'] != ''
                and response.json()['refreshToken'] != '')

    @allure.title('Создание пользователя который уже зарегестрирован')
    @allure.description('Проверяем, что после повторного создания возвращается код 403')
    def test_user_creation(self):
        fake = Faker()
        email = fake.first_name() + "@yandex.ru"
        password = fake.last_name()
        name = fake.first_name()
        response = helper_user.create_user(email, password, name)
        access_token = helper_user.get_access_token(response)
        response = helper_user.create_user(email, password, name)
        helper_user.delete_user(access_token)
        assert (response.status_code == 403
                and response.json()['success'] == False and response.json()['message'] == "User already exists")

    @allure.title('Создание пользователя с пустым обязательным полем Email приводит к ошибке')
    @allure.description(
        'Проверяем, что при пустом поле Email покажется сообщение "Email, password and name are required fields"')
    def test_user_creation_with_empty_email(self):
        response = helper_user.create_user('', '123456789', 'name')
        assert (response.status_code == 403 and response.json()['success'] == False
                and response.json()['message'] == "Email, password and name are required fields")

    @allure.title('Создание пользователя с пустым обязательным полем password приводит к ошибке')
    @allure.description(
        'Проверяем, что при пустом поле password покажется сообщение "Email, password and name are required fields"')
    def test_user_creation_with_empty_password(self):
        response = helper_user.create_user('pb@gmail.com', '', 'name')
        assert (response.status_code == 403 and response.json()['success'] == False
                and response.json()['message'] == "Email, password and name are required fields")

    @allure.title('Создание пользователя с пустым обязательным полем Name приводит к ошибке')
    @allure.description(
        'Проверяем, что при пустых обязательных полях сообщение "Email, password and name are required fields"')
    def test_user_creation_with_empty_name(self):
        response = helper_user.create_user('pb@gmail.com', '123456789', '')
        assert (response.status_code == 403 and response.json()['success'] == False
                and response.json()['message'] == "Email, password and name are required fields")
