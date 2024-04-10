import helper_order
import allure
import data


class TestCreateOrder:
    @allure.title('Создание заказа с ингридиентами авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет код 200 для пользователя с авторизацией')
    def test_create_order_with_authorization_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert response.status_code == 200

    @allure.title('Создание заказа и проверка имени')
    @allure.description('Проверяем что создан заказ с ожидаемым именем')
    def test_name_of_created_order_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert response.json()['name'] == "Био-марсианский метеоритный бургер"

    @allure.title('Создание заказа и проверка успешности')
    @allure.description('Проверяем что создан заказ успешно Success параметр = true')
    def test_success_parameter_of_created_order_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert response.json()['success'] == True

    @allure.title('Создание заказа и проверяем что number есть')
    @allure.description('Проверяем что у заказа есть параметр number')
    def test_number_parameter_of_created_order_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа и проверяем что number не пуст')
    @allure.description('Проверяем что создан заказ и параметр number не пустой')
    def test_success_parameter_of_created_order_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert response.json()['order']['number'] != ''

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
