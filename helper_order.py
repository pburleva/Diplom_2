import requests
import allure
import urls
import helper_user


@allure.step('Создаем заказ')
def create_order(access_token, ingredients_list):
    header = helper_user.create_authorization_header(access_token)
    payload = {'ingredients': ingredients_list}
    response = requests.post(urls.BASE_URL + urls.ORDERS, headers=header, data=payload)
    return response


@allure.step('Получаем заказ пользователя')
def get_order_of_user(access_token):
    header = helper_user.create_authorization_header(access_token)
    response = requests.get(urls.BASE_URL + urls.ORDERS, header)
    return response
