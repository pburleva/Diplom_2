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
        assert (response.status_code == 200 and response.json()['success'] == True
                and response.json()['orders'][0]['_id'] == "6605886e9ed280001b3d3cb9"
                and response.json()['orders'][0]['ingredients'][1] == "61c0c5a71d1f82001bdaaa6d"
                and response.json()['orders'][0]['ingredients'][2] == "61c0c5a71d1f82001bdaaa6f"
                and response.json()['orders'][0]['status'] == "done"
                and response.json()['orders'][0]['name'] == "Бессмертный флюоресцентный бургер"
                and response.json()['orders'][0]['createdAt'] == "2024-03-28T15:10:38.125Z"
                and response.json()['orders'][0]['updatedAt'] == "2024-03-28T15:10:38.437Z"
                and response.json()['number'][0]['updatedAt'] == "2024-03-28T15:10:38.437Z")

    @allure.title('Получение заказов неавторизованного пользователя')
    @allure.description('Проверяем статус получения заказов пользователя без авторизации')
    def test_get_orders_of_user_with_authorization_successful(self):
        response = helper_order.get_order_of_user('')
        assert response.status_code == 401 and response.json()['message'] == "You should be authorised"
