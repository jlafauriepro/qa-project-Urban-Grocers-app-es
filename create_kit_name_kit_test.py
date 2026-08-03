import sender_stand_request
import data

def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body

def get_new_user_token():
    return sender_stand_request.get_new_user_token()

def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == name

def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_1_create_kit_1_letter_in_name():
    positive_assert("a")

def test_2_create_kit_511_letters_in_name():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_3_create_kit_0_letters_in_name():
    negative_assert_code_400("")

def test_4_create_kit_512_letters_in_name():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_5_create_kit_special_chars_in_name():
    positive_assert("\"№%@\",")

def test_6_create_kit_spaces_in_name():
    positive_assert(" A Aaa ")

def test_7_create_kit_numbers_in_name():
    positive_assert("123")

def test_8_create_kit_no_name_parameter():
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit({}, auth_token)
    assert response.status_code == 400

def test_9_create_kit_number_type_in_name():
    auth_token = get_new_user_token()
    kit_body = {"name": 123}
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400