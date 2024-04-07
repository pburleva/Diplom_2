import helper_order
import helper_user
import allure
import data


class TestGetOrder:
    @allure.title('Получение заказов авторизованного пользователя')
    @allure.description('Проверяем статус получения заказов пользователя с авторизацией')
    def test_get_orders_of_user_with_authorization_successful(self):
        response = helper_user.login_user(data.EMAIL_OF_USER_WITH_ORDERS, data.PASSWORD_OF_USER_WITH_ORDERS)
        access_token = helper_user.get_access_token(response)
        response = helper_order.get_order_of_user(access_token)
        assert response.status_code == 200

    @allure.title('Получение заказов неавторизованного пользователя')
    @allure.description('Проверяем статус получения заказов пользователя без авторизации')
    def test_get_orders_of_user_with_authorization_successful(self):
        response = helper_order.get_order_of_user('')
        assert response.status_code == 401

