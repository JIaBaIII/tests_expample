import pytest
from faker import Faker
from selenium import webdriver

from config import LOCATIONS_DRIVERS, MODERATOR_LOGIN, MODERATOR_PASSWORD
from framework.client import Client
from framework.helper import get_random_letters

client = Client()

fake = Faker()


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    par_doc = par.__doc__.strip().replace('.', ' ::').split('\n')[0]
    node_doc = node.__doc__.strip().replace('.', '').split('\n')[0]
    pref = par_doc if par.__doc__ else par.__class__.__name__
    suf = node_doc if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture(scope="class")
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(f'{LOCATIONS_DRIVERS}chromedriver', options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox_browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def first_feed_post_id():
    first_post = client.get_feed(0, 1).json()['Result'][0]
    return first_post['ElementID']


@pytest.fixture(scope='session')
def valid_token_moderator():
    def sign_in_moder():
        body = {
            "Login": MODERATOR_LOGIN,
            "Password": MODERATOR_PASSWORD
        }
        response = client.post_login(body)
        return response.json()['Credentials']['Token']

    return {
        'Authorization': f'{sign_in_moder()}'
    }


@pytest.fixture(scope='function')
def delete_first_feed_question_by_moder(valid_token_moderator, first_feed_post_id):
    client.delete_question(first_feed_post_id, valid_token_moderator)
    deleted_question_status = client.get_questions(first_feed_post_id).json()['Result']['Question']['Status']
    return deleted_question_status


@pytest.fixture(scope='function')
def delete_first_feed_article_by_moder(valid_token_moderator, first_feed_post_id):
    client.delete_article(first_feed_post_id, valid_token_moderator)
    deleted_article_status = client.get_article(first_feed_post_id).json()['Result']['Article']['Status']
    return deleted_article_status


@pytest.fixture(scope='function')
def delete_article_id_by_moder(valid_token_moderator, create_valid_article_id):
    client.delete_article(create_valid_article_id, valid_token_moderator)
    deleted_article_status = client.get_article(create_valid_article_id).json()['Result']['Article']['Status']
    return deleted_article_status


@pytest.fixture(scope='function')
def delete_another_article_id_by_moder(valid_token_moderator, create_another_valid_article_id):
    client.delete_article(create_another_valid_article_id, valid_token_moderator)
    deleted_article_status = client.get_article(create_another_valid_article_id).json()['Result']['Article']['Status']
    return deleted_article_status


@pytest.fixture(scope='function')
def delete_question_id_by_moder(valid_token_moderator, create_valid_question_id):
    client.delete_question(create_valid_question_id, valid_token_moderator)
    deleted_question_status = client.get_questions(create_valid_question_id).json()['Result']['Question']['Status']
    return deleted_question_status


@pytest.fixture(scope='function')
def delete_answer_id_by_moder(valid_token_moderator, valid_answer):
    client.delete_answer(valid_answer, valid_token_moderator)


@pytest.fixture(scope='function')
def delete_comment_id_article_by_moder(valid_token_moderator, valid_comment_article):
    client.delete_comment(valid_comment_article, valid_token_moderator)


@pytest.fixture(scope='function')
def delete_comment_id_answer_by_moder(valid_token_moderator, valid_comment_answer):
    client.delete_comment(valid_comment_answer, valid_token_moderator)


@pytest.fixture(scope='class')
def create_another_valid_article_id(valid_articles_create_json, valid_token_another_user):
    create_article = client.post_article_create(valid_articles_create_json, valid_token_another_user)
    valid_article_id = create_article.json()['Result']['Article']['ID']
    client.put_article_publish(valid_article_id, headers=valid_token_another_user)
    return valid_article_id


@pytest.fixture(scope='class')
def create_another_question_with_answer(valid_answer_json, valid_token_another_user):
    create_answer = client.post_answer_create(valid_answer_json, valid_token_another_user)
    valid_question_with_answer = create_answer.json()['Result']['Answer']['Answer']['QuestionID']
    client.put_question_publish(valid_question_with_answer, headers=valid_token_another_user)
    return valid_question_with_answer


@pytest.fixture(scope='class')
def signed_up_user_for_sign_in():
    password = fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)
    body = {
        "Login": get_random_letters(10),
        "Password": password,
        "RepeatedPassword": password
    }
    client.post_sign_up_user(body)
    return body


@pytest.fixture(scope='class')
def valid_token_new_user():
    def sign_up_user():
        password = fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)
        body = {
            "Login": get_random_letters(10),
            "Password": password,
            "RepeatedPassword": password
        }
        response = client.post_sign_up_user(body)
        return response.json()['Credentials']['Token']
    return {
        'Authorization': f'{sign_up_user()}'
    }


@pytest.fixture(scope='class')
def valid_cookie_new_user(valid_token_new_user):
    return {
        'name': 'Token',
        'value': f"Bearer%20{valid_token_new_user['Authorization']}"
    }


@pytest.fixture(scope='class')
def valid_id_new_user(valid_token_new_user):
    user_info = client.get_info(valid_token_new_user)
    user_id = user_info.json()['User']['ID']
    return user_id


@pytest.fixture(scope='class')
def valid_token_another_user():
    def sign_up_another_user():
        password = fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)
        body = {
            "Login": get_random_letters(10),
            "Password": password,
            "RepeatedPassword": password
        }
        response = client.post_sign_up_user(body)
        return response.json()['Credentials']['Token']
    return {
        'Authorization': f'{sign_up_another_user()}'
    }


@pytest.fixture(scope='class')
def valid_cookie_another_user(valid_token_another_user):
    return {
        'name': 'Token',
        'value': f"Bearer%20{valid_token_another_user['Authorization']}"
    }


@pytest.fixture(scope='class')
def valid_id_another_user(valid_token_another_user):
    user_info = client.get_info(valid_token_another_user)
    user_id = user_info.json()['User']['ID']
    return user_id


@pytest.fixture(scope='class')
def valid_token_third_user():
    def sign_up_third_user():
        password = fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)
        body = {
            "Login": get_random_letters(10),
            "Password": password,
            "RepeatedPassword": password
        }
        response = client.post_sign_up_user(body)
        return response.json()['Credentials']['Token']
    return {
        'Authorization': f'{sign_up_third_user()}'
    }


@pytest.fixture(scope='class')
def valid_cookie_third_user(valid_token_third_user):
    return {
        'name': 'Token',
        'value': f"Bearer%20{valid_token_third_user['Authorization']}"
    }


@pytest.fixture(scope='class')
def valid_id_third_user(valid_token_third_user):
    user_info = client.get_info(valid_token_third_user)
    user_id = user_info.json()['User']['ID']
    return user_id


@pytest.fixture(scope='class')
def valid_articles_create_json():
    return {
        "Data": f'Авто описание статьи. Багдата готоворит что я еще жив)) # {fake.pystr()}',
        "Title": f'Auto-title Article #{fake.pystr()}',
        "Tags": [
            {
                "Name": 'auto_spelling_tag_of_doom'
            }
        ]
    }


@pytest.fixture(scope='class')
def create_valid_article_id(valid_articles_create_json, valid_token_new_user):
    create_article = client.post_article_create(valid_articles_create_json, valid_token_new_user)
    valid_article_id = create_article.json()['Result']['Article']['ID']
    client.put_article_publish(valid_article_id, headers=valid_token_new_user)
    return valid_article_id


@pytest.fixture(scope='class')
def valid_questions_create_json():
    return {
        "Data": f'Авто описание вопроса. Багдата готоворит что я текст)) # {fake.pystr()}',
        "Title": f'Auto-title Question #{fake.pystr()}',
        "Tags": [
            {
                "Name": 'auto_spelling_tag_of_doom'
            }
        ]
    }


@pytest.fixture(scope='class')
def create_valid_question_id(valid_questions_create_json, valid_token_new_user):
    create_question = client.post_question_create(valid_questions_create_json, valid_token_new_user)
    valid_question_id = create_question.json()['Result']['Question']['ID']
    client.put_question_publish(valid_question_id, headers=valid_token_new_user)
    return valid_question_id


@pytest.fixture(scope='class')
def valid_answer_json(create_valid_question_id):
    return {
        "QuestionID": create_valid_question_id,
        "Text": f' Авто описание ответа. Багдата готоворит что я вубл!)) # {fake.pystr()}'
    }


@pytest.fixture(scope='class')
def valid_answer(valid_answer_json, valid_token_new_user):
    create_answer_id = client.post_answer_create(valid_answer_json, valid_token_new_user)
    valid_answer_id = create_answer_id.json()['Result']['Answer']['Answer']['ID']
    return valid_answer_id


@pytest.fixture(scope='class')
def create_question_with_answer(valid_answer_json, valid_token_new_user):
    create_answer = client.post_answer_create(valid_answer_json, valid_token_new_user)
    valid_question_with_answer = create_answer.json()['Result']['Answer']['Answer']['QuestionID']
    return valid_question_with_answer


@pytest.fixture(scope='class')
def valid_comment_answer_json(valid_answer):
    return {
        "Data": f'Авто коммент в Answer. Багдата готоворит что я пупырка!)) # {fake.pystr()}',
        "ParentElementID": valid_answer
    }


@pytest.fixture(scope='class')
def valid_comment_article_json(create_valid_article_id):
    return {
        "Data": f'Авто коммент в Article. Багдата готоворит что я пупырка!)) # {fake.pystr()}',
        "ParentElementID": create_valid_article_id
    }


@pytest.fixture(scope='class')
def valid_comment_answer(valid_comment_answer_json, valid_token_new_user):
    create_comment_id = client.post_comment(valid_comment_answer_json, valid_token_new_user)
    valid_comment_id = create_comment_id.json()['Result']['Comment']['ID']
    return valid_comment_id


@pytest.fixture(scope='class')
def create_valid_comment_on_answer_id(valid_comment_answer_json, valid_token_new_user):
    create_comment_id = client.post_comment(valid_comment_answer_json, valid_token_new_user)
    valid_comment_answer_id = create_comment_id.json()['Result']['Comment']['ParentElementID']
    return valid_comment_answer_id


@pytest.fixture(scope='class')
def valid_comment_article(valid_comment_article_json, valid_token_new_user):
    create_comment_id = client.post_comment(valid_comment_article_json, valid_token_new_user)
    valid_comment_id = create_comment_id.json()['Result']['Comment']['ID']
    return valid_comment_id


@pytest.fixture(scope='class')
def create_valid_comment_on_article_id(valid_comment_article_json, valid_token_new_user):
    create_comment_id = client.post_comment(valid_comment_article_json, valid_token_new_user)
    valid_comment_article_id = create_comment_id.json()['Result']['Comment']['ParentElementID']
    return valid_comment_article_id


@pytest.fixture(scope='function')
def sign_up_login_3_password():
    password = fake.password(length=16, digits=True, upper_case=True, lower_case=True)
    return {
        "Login": get_random_letters(3),
        "Password": password
    }


@pytest.fixture(scope='function')
def sign_up_login_10_password():
    password = fake.password(length=16, digits=True, upper_case=True, lower_case=True)
    return {
        "Login": get_random_letters(10),
        "Password": password
    }


@pytest.fixture(scope='function')
def sign_up_login_20_password():
    password = fake.password(length=16, digits=True, upper_case=True, lower_case=True)
    return {
        "Login": get_random_letters(20),
        "Password": password
    }


@pytest.fixture(scope='function')
def fake_article_text():
    return f'Авто описание статьи # {fake.pystr()}'


@pytest.fixture(scope='function')
def fake_question_text():
    return f'Авто описание вопроса # {fake.pystr()}'


@pytest.fixture(scope='function')
def fake_answer_text():
    return f'Авто описание ответа # {fake.pystr()}'


@pytest.fixture(scope='function')
def fake_comment_1_text():
    return f'Авто описание коммента 1 уровня # {fake.pystr()}'


@pytest.fixture(scope='function')
def fake_comment_2_text():
    return f'Авто описание коммента 2 уровня # {fake.pystr()}'


@pytest.fixture(scope='session')
def my_formula():
    return r'\prod_a^b\frac{ab}{cd}\lim_{a \rightarrow b}\lambda\tanh\sec\underbrace ' \
        r'{ab}\bigwedge_a^b\overrightarrow{ab}\pm\frac{\text{d}x}{\text{d}y}\left(\begin'\
        r'{array}{c}a\\ b\end{array}\right)\begin{cases}a & x = 0\\b & x > 0\end{cases}\begin'\
        r'{bmatrix}a & b \\c & d \end{bmatrix}\coprod_a^b\frac{-b\pm\sqrt{b^2-4ac}}'\
        r'{2a}\frac{-b\pm\sqrt{b^2-4ac}}{2a}'


@pytest.fixture(scope='class')
def fake_collection_name():
    return f'Моя авто коллекция # {fake.pystr()}'


@pytest.fixture(scope='class')
def fake_collection_description():
    return f'Авто описание коллекции # {fake.pystr()}'


@pytest.fixture(scope='class')
def fake_another_collection_name():
    return f'Новое авто название # {fake.pystr()}'


@pytest.fixture(scope='class')
def fake_another_collection_description():
    return f'Новое авто описание # {fake.pystr()}'
