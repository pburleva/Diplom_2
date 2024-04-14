import helper_order
import allure
import data


class TestCreateOrder:
    @allure.title('Создание заказа с ингридиентами авторизованным пользователем')
    @allure.description('Проверяем что создание заказа успешно и возвращает ожидаемые поля')
    def test_create_order_with_authorization_successful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS)
        assert (response.status_code == 200
                and response.json()['name'] == "Био-марсианский метеоритный бургер"
                and response.json()['success'] == True
                and 'number' in response.json()['order']
                and response.json()['order']['number'] != ''
                and response.json()['order']['ingredients'][0]['_id'] == '61c0c5a71d1f82001bdaaa70'
                and response.json()['order']['ingredients'][0]['name'] == 'Говяжий метеорит (отбивная)'
                and response.json()['order']['ingredients'][1]['_id'] == '61c0c5a71d1f82001bdaaa71'
                and response.json()['order']['ingredients'][1]['name'] == 'Биокотлета из марсианской Магнолии')

    @allure.title('Создание заказа с ингридиентами пользователем без авторизации')
    @allure.description('Проверяем что создание заказа успешно и возвращает ожидаемые поля для пользователя'
                        'без авторизации')
    def test_create_order_without_authorization_successful(self):
        response = helper_order.create_order('', data.INGREDIENTS)
        assert (response.status_code == 200
                and response.json()['name'] == "Био-марсианский метеоритный бургер"
                and response.json()['success'] == True
                and 'number' in response.json()['order'] and response.json()['order']['number'] != '')

    @allure.title('Создание заказа без ингридиентов и авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет код 400 и ожидаемое сообщение'
                        ' если список ингридиентов пуст')
    def test_create_order_without_ingredients_unsuccessful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], '')
        assert (response.status_code == 400
                and response.json()['success'] == False
                and response.json()['message'] == "Ingredient ids must be provided")

    @allure.title('Создание заказа с ингридиентами с некорректным хэшем и авторизованным пользователем')
    @allure.description('Проверяем что создание заказа вернет код 500 хэш ингридиентов некорректный')
    def test_create_order_with_incorrect_ingredients_hash_unsuccessful(self, user_fixture):
        response = helper_order.create_order(user_fixture[3], data.INGREDIENTS_INCORRECT_HASH)
        assert response.status_code == 500
