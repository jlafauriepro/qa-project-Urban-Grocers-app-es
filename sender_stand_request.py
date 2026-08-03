import requests
import configuration
import data

def post_new_user(body):
    return requests.post(
        configuration.url_service + configuration.create_user_path,
        json=body
    )

def get_new_user_token():
    return post_new_user(data.user_body).json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    return requests.post(
        configuration.url_service + configuration.kits_path,
        json=kit_body,
        headers={"Authorization": "Bearer " + auth_token}
    )