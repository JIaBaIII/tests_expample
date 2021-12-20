import os
import random
import string

from framework.client import Client

client = Client()


def get_random_letters(how_many_letters):
    def random_char(y):
        letters_and_digits = string.ascii_letters + string.digits + '_'
        return ''.join(random.choice(letters_and_digits) for _ in range(y))
    return random_char(how_many_letters)


def get_random_gif():
    gif_dir = os.listdir(os.getcwd() + '/Gifs/')
    random_index = random.randint(0, len(gif_dir) - 1)
    return os.getcwd() + f'/Gifs/{gif_dir[random_index]}'


def get_random_avatar():
    image_dir = os.listdir(os.getcwd() + '/Images_avatar/')
    random_index = random.randint(0, len(image_dir) - 1)
    return os.getcwd() + f'/Images_avatar/{image_dir[random_index]}'


def get_avatar_1mb():
    image_dir = os.listdir(os.getcwd() + '/Images_about_1mb/')
    random_index = random.randint(0, len(image_dir) - 1)
    return os.getcwd() + f'/Images_about_1mb/{image_dir[random_index]}'


def get_avatar_10mb():
    image_dir = os.listdir(os.getcwd() + '/Images_about_10mb/')
    random_index = random.randint(0, len(image_dir) - 1)
    return os.getcwd() + f'/Images_about_10mb/{image_dir[random_index]}'


def get_screenshot(driver):
    num = 0
    num += num + 1
    filename = f'screenshot#{num}.png'
    driver.save_screenshot(filename)


def delete_question_id_by_moder(valid_token_moderator, question_id):
    client.delete_question(question_id, valid_token_moderator)
    deleted_question_status = client.get_questions(question_id).json()['Result']['Question']['Status']
    return deleted_question_status


def delete_article_id_by_moder(valid_token_moderator, article_id):
    client.delete_article(article_id, valid_token_moderator)
    deleted_article_status = client.get_article(article_id).json()['Result']['Article']['Status']
    return deleted_article_status


def delete_answer_id_by_moder(valid_token_moderator, answer_id):
    client.delete_answer(answer_id, headers=valid_token_moderator)
    deleted_answer_status = client.get_answers(answer_id).json()['Result']['Answer']['Answer']['Status']
    return deleted_answer_status


def delete_comment_id_by_moder(valid_token_moderator, comment_id):
    client.delete_comment(comment_id, headers=valid_token_moderator)
