""" Тестипование наименований элементов.
User story -
Docs -
"""
import time

from framework.BrowsersHelper import Chrome
from framework.check import check_text_field_name, \
    check_element_text_is_on_page, check_field_name, check_element_is_on_page


class TestAnswerPage:
    """ Тесты на соответствие наименований элементов на странице Answer.
    """

    def test_elem_answer_page_01(self, chrome_browser, create_another_question_with_answer):
        """ Пожаловаться на ответ.

        - Открыть страницу вопроса
        - Открыть страницу вотета
        - Нажать на ***
        - Найти "Пожаловаться"

        :param chrome_browser:
        :param create_another_question_with_answer:
        :return: OK - если на кнопке пожаловаться написано "Complain"
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_another_question_with_answer}')
        chrome.click_to_open_answers_page()
        chrome.click_btn_menu_answer()
        check_text_field_name(chrome.find_menu_item_complain(), 'Complain')

    def test_elem_answer_page_02(self, chrome_browser, valid_cookie_new_user, create_another_question_with_answer):
        """ Кол-во upvote на ответе.

        - Открыть страницу вопроса
        - Нажать Upvote

        :param chrome_browser:
        :param create_another_question_with_answer:
        :return: OK - если на кнопке пожаловаться написано "Complain"
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_another_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_article_or_question_page_icon_upvote()
        chrome_browser.refresh()
        time.sleep(0.3)
        check_field_name(chrome.find_article_or_question_page_upvote_fill(), '1 likes')

    def test_elem_answer_page_03(self, chrome_browser, valid_cookie_third_user, create_another_question_with_answer):
        """ Кол-во upvote на ответе, на странице ответа.

        - Открыть страницу вопроса
        - Открыть страницу ответа

        :param chrome_browser:
        :param create_another_question_with_answer:
        :return: OK - если на кнопке пожаловаться написано "Complain"
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_third_user)
        chrome.go_to_site(f'/question/{create_another_question_with_answer}')
        chrome.click_to_open_answers_page()
        chrome.click_answer_page_upvote_count()
        chrome_browser.refresh()
        time.sleep(0.3)
        check_field_name(chrome.find_answer_page_upvote_count(), '2')

    def test_from_answer_to_question_page(self, chrome_browser, create_another_question_with_answer):
        """ Вернуться на страницу вопроса со страницы ответа.

        - Открыть страницу feed
        - Открыть вопрос с ответом
        - Открыть ответ
        - Вернуться на страницу вопроса

        :param chrome_browser:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'/question/{create_another_question_with_answer}')
        chrome.click_to_open_answers_page()
        chrome.click_question_title_answer_page()
        chrome.find_question_page_container()
        check_element_is_on_page('QuestionCard_card__EQR8e', chrome)

    def test_delete_created_posts(self, chrome_browser, valid_cookie_new_user, create_another_question_with_answer):
        """ Удаление созданного вопроса.

        - Открыть страницу вопроса
        - Удалить вопрос
        - Открыть страницу профиля
        - Проверить, что вопрос удален

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :param create_another_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если вопрос удален
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site(f'/question/{create_another_question_with_answer}')
        chrome.make_click_delete_question()
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
