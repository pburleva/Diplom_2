import requests
import allure
import urls
from faker import Faker


def create_authorization_header(access_token):
    header = {"authorization": access_token}
    return header


@allure.step('Создаем пользователя')
def create_user(email, password, name):
    payload = {'email': email, 'password': password, 'name': name}
    response = requests.post(urls.BASE_URL + urls.USER_REGISTRATION, payload)
    return response


@allure.step('Логин пользователя')
def login_user(email, password):
    payload = {'email': email, 'password': password}
    response = requests.post(urls.BASE_URL + urls.USER_LOGIN, payload)
    return response


def get_access_token(response):
    access_token = response.json()['accessToken']
    return access_token


@allure.step('Изменение email пользователя')
def patch_user_email(access_token, email):
    header = create_authorization_header(access_token)
    payload = {'email': email}
    response = requests.patch(urls.BASE_URL + urls.USER_AUTH_USER, headers=header, data=payload)
    return response


@allure.step('Изменение password пользователя')
def patch_user_password(access_token, password):
    header = create_authorization_header(access_token)
    payload = {'password': password}
    response = requests.patch(urls.BASE_URL + urls.USER_AUTH_USER, headers=header, data=payload)
    return response


@allure.step('Изменение name пользователя')
def patch_user_name(access_token, name):
    header = create_authorization_header(access_token)
    payload = {'name': name}
    response = requests.patch(urls.BASE_URL + urls.USER_AUTH_USER, headers=header, data=payload)
    return response


def create_user_with_unique_data():
    user_data_list = []
    fake = Faker()
    email = fake.first_name() + "@yandex.ru"
    password = fake.last_name()
    name = fake.first_name()
    response = create_user(email, password, name)
    if response.status_code == 200:
        user_data_list.append(email)
        user_data_list.append(password)
        user_data_list.append(name)
        user_data_list.append(get_access_token(response))
    return user_data_list


def delete_user(access_token):
    header = create_authorization_header(access_token)
    response = requests.delete(urls.BASE_URL + urls.USER_AUTH_USER, headers=header)
    return response






