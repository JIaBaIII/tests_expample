""" Создание Article, незавершенные действия, незаполненные поля.
User story -
Docs -
"""
import time

import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_element_text_is_on_page, check_elem_is_disable


class TestUnfinishedActions:
    """ Article, unfinished actions.
    """

    def test_article_unfinished_actions_01(self, chrome_browser, valid_cookie_new_user, fake_article_text):
        """ В процессе создания статьи вернуться в профиль.

        Предшаги:
        - Открыть главную страницу TOCI
        - Зарегистрироваться новым юзером

        Шаги:
        - Открыть страницу профиля
        - Убедиться, что в профиле нет опубликованных постов
        - Открыть страницу создания статьи
        - Вписать title и description
        - Вернуться на страницу профиля

        ----

        Expected:
            Статья не опубликована

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :param fake_article_text: Текст, вводимый в поле Description
        :return: OK - если статья не опубликована
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile/')
        chrome.find_my_avatar()
        chrome.make_pre_steps_for_article_create()
        chrome.write_title()
        chrome.write_description(fake_article_text)
        chrome.click_editor_btn_back()
        chrome_browser.refresh()
        time.sleep(0.4)
        check_element_text_is_on_page(chrome.find_profile_no_published_data(), chrome)

    @pytest.mark.xfail(reason='Ожидаю фейл. Проверить когда починят баг'
                              'https://www.notion.so/hipasus/Title-a699f426500841afa2a9e122379f01dd')
    def test_article_unfinished_actions_02(self, chrome_browser):
        """ Создавая статью вписать только Title.

        Предшаги:
        - Открыть главную страницу TOCI
        - Зарегистрироваться новым юзером

        Шаги:
        - Открыть страницу профиля
        - Убедиться, что в профиле нет опубликованных постов
        - Открыть страницу создания статьи
        - Вписать только title
        - Опубликовать

        ----

        Expected:
            Статья не опубликована

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья не опубликована
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site('/profile/')
        chrome.find_my_avatar()
        chrome.make_pre_steps_for_article_create()
        chrome.write_title()
        check_elem_is_disable(chrome.find_btn_dark())

    def test_article_unfinished_actions_03(self, chrome_browser, fake_article_text):
        """ Создавая статью вписать только description.

        Предшаги:
        - Открыть главную страницу TOCI
        - Зарегистрироваться новым юзером

        Шаги:
        - Открыть страницу профиля
        - Убедиться, что в профиле нет опубликованных постов
        - Открыть страницу создания статьи
        - Вписать только description
        - Опубликовать

        ----

        Expected:
            Статья не опубликована

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья не опубликована
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site('/profile/')
        chrome.find_my_avatar()
        chrome.make_pre_steps_for_article_create()
        chrome.write_description(fake_article_text)
        check_elem_is_disable(chrome.find_btn_dark())

    def test_delete_all_cookies(self, chrome_browser):
        """ Удалить использованные в этом классе куки.

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если использованные в этом классе куки удалены
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome_browser.delete_all_cookies()
