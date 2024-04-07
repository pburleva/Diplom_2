import helper_user
import allure


class TestLogin:

    @allure.title('Логин существующим пользователем')
    @allure.description('Проверяем, что при логине существующим пользователем воозвращается код 200')
    def test_existing_user_login_successful(self, user_fixture):
        response = helper_user.login_user(user_fixture[0], user_fixture[1])
        assert response.status_code == 200

    @allure.title('Логин несуществующим пользователем')
    @allure.description('Проверяем, что при логине несуществующим пользователем'
                        ' воозвращается "email or password are incorrect"')
    def test_not_existing_user_login_unsuccessful(self, user_fixture):
        response = helper_user.login_user('unexisting', 'unexisting')
        assert response.json()['message'] == "email or password are incorrect"

    @allure.title('Логин несуществующим пользователем')
    @allure.description('Проверяем, что при логине несуществующим пользователем возвращается "success": false')
    def test_not_existing_user_login_unsuccessful(self, user_fixture):
        response = helper_user.login_user('unexisting', 'unexisting')
        assert response.json()['success'] == False
