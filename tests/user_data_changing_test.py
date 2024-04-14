import helper_user
import allure
import data


class TestDataChanging:

    @allure.title('Изменение значения email пользователя')
    @allure.description('Проверяем, что возможно изменение полей пользователя с авторизацией')
    def test_email_changing_with_authorization_successful(self, user_fixture):
        response = helper_user.patch_user_email(user_fixture[3], data.EXPECTED_EMAIL)
        assert (response.status_code == 200 and response.json()['success'] == True
                and response.json()['user']['email'] == data.EXPECTED_EMAIL and response.json()['user']['name'] != '')

    @allure.title('Изменение значения password пользователя')
    @allure.description('Проверяем, что возможно изменение полей пользователя с авторизацией')
    def test_password_changing_with_authorization_successful(self, user_fixture):
        response = helper_user.patch_user_password(user_fixture[3], data.EXPECTED_PASSWORD)
        assert (response.status_code == 200 and response.json()['success'] == True
                and response.json()['user']['email'] != '' and response.json()['user']['name'] != '')

    @allure.title('Изменение значения name пользователя')
    @allure.description('Проверяем, что возможно изменение полей пользователя с авторизацией')
    def test_user_name_changing_with_authorization_successful(self, user_fixture):
        response = helper_user.patch_user_name(user_fixture[3], data.EXPECTED_NAME)
        assert (response.status_code == 200 and response.json()['success'] == True
                and response.json()['user']['email'] != '' and response.json()['user']['name'] == data.EXPECTED_NAME)

    @allure.title('Изменение значения email пользователем без авторизации')
    @allure.description('Проверяем, что попытка изменить email без авторизации приведет к ошибке')
    def test_email_changing_with_authorization_unsuccessful(self, user_fixture):
        response = helper_user.patch_user_email('', data.EXPECTED_EMAIL)
        assert (response.status_code == 401 and response.json()['success'] == False
                and response.json()['message'] == data.ERROR_NOT_AUTHORIZED)

    @allure.title('Изменение значения password пользователя')
    @allure.description('Проверяем, что попытка изменить пароль пользователя без авторизации приведет к ошибке')
    def test_password_changing_without_authorization_unsuccessful(self, user_fixture):
        response = helper_user.patch_user_password('', data.EXPECTED_PASSWORD)
        assert (response.status_code == 401 and response.json()['success'] == False
                and response.json()['message'] == data.ERROR_NOT_AUTHORIZED)

    @allure.title('Изменение значения name пользователя')
    @allure.description('Проверяем, что попытка изменить имя пользователя без авторизации приведет к ошибке')
    def test_name_changing_without_authorization_unsuccessful(self, user_fixture):
        response = helper_user.patch_user_name('', data.EXPECTED_NAME)
        assert (response.status_code == 401 and response.json()['success'] == False
                and response.json()['message'] == data.ERROR_NOT_AUTHORIZED)
