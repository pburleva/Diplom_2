import helper_order
import allure
import data


class TestCreateOrder:
    @allure.title('Создание заказа с ингридиентами авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет код 200 для пользователя с авторизацией')
    def test_create_order_with_authorization_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert response.status_code == 200

    @allure.title('Создание заказа с ингридиентами пользователем без авторизации')
    @allure.description('Проверяем что создание заказа вернет код 200 для пользователя без авторизации')
    def test_create_order_without_authorization_successful(self):
        response = helper_order.create_order('', data.INGREDIENTS)
        assert response.status_code == 200

    @allure.title('Создание заказа без ингридиентов и авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет код 400 если список ингридиентов пуст')
    def test_create_order_without_ingredients_unsuccessful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], '')
        assert response.status_code == 400

    @allure.title('Создание заказа без ингридиентов и авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет "Ingredient ids must be provided"'
                        ' сообщение если список ингридиентов пуст')
    def test_create_order_without_ingredients_unsuccessful_message_check(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], '')
        assert "Ingredient ids must be provided" in response.text

    @allure.title('Создание заказа с ингридиентами с некорректным хэшем и авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет код 500 хэш ингридиентов некорректный')
    def test_create_order_with_incorrect_ingredients_hash_unsuccessful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS_INCORRECT_HASH)
        assert response.status_code == 500
