""" Создание Answer, незавершенные действия, незаполненные поля.
User story -
Docs -
"""
import time

from framework.BrowsersHelper import Chrome
from framework.check import check_element_text_is_on_page, check_elem_is_disable, check_field_name


class TestUnfinishedActions:
    """ Answer, unfinished actions.
    """

    def test_answer_unfinished_actions_01(
            self, chrome_browser, valid_cookie_new_user, create_valid_question_id, fake_answer_text):
        """ В процессе создания ответа вернуться в профиль.

        Предшаги:
        - Открыть главную страницу TOCI
        - Зарегистрироваться новым юзером

        Шаги:
        - Открыть страницу вопроса без ответов
        - Нажать Answer
        - Вписать ответ
        - Вернуться на страницу вопроса

        ----

        Expected:
            Ответ не опубликован

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return: OK - если ответ не опубликован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_my_avatar()
        chrome.click_answer()
        chrome.write_description(fake_answer_text)
        chrome.click_editor_btn_back()
        chrome_browser.refresh()
        time.sleep(0.4)
        check_field_name(chrome.find_question_page_count_answers(), '0answers')

    def test_answer_unfinished_actions_02(self, chrome_browser, create_valid_question_id, valid_cookie_new_user):
        """ Опубликовать пустой ответ.

        Шаги:
        - Открыть страницу вопроса без ответов
        - Нажать Answer
        - Оставить поле ввода ответа пустым
        - Опубликовать ответ

        ----

        Expected:
            Ответ не опубликован

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если ответ не опубликован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_my_avatar()
        chrome.click_answer()
        chrome.find_btn_post_answers()
        check_elem_is_disable(chrome.find_btn_post_answers())

    def test_delete_question(self, chrome_browser, valid_cookie_new_user):
        """ Удаление вопроса.

        - Открыть главную страницу
        - Открыть страницу вопроса
        - Нажать *** и выбрать "удалить вопрос"
        - Подтвердить удаление вопроса
        - Открыть страницу профиля
        - Проверить отсутствие вопроса в профиле

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return: OK - если вопрос удален
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_menu_item_delete()
        chrome.click_btn_blue()
        chrome.go_to_site('/profile/')
        check_element_text_is_on_page(chrome.find_profile_no_published_data(), chrome)

    def test_delete_all_cookies(self, chrome_browser):
        """ Удалить использованные в этом классе куки.

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если использованные в этом классе куки удалены
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome_browser.delete_all_cookies()
