""" Создание Comments lvl 1.
User story -
Docs -
"""
import time

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_element_text_is_on_page
from framework.helper import delete_comment_id_by_moder


class TestCommentsLvl1:
    """ Comments lvl 1.
    """

    def test_create_comments_1_lvl_01(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Создание комментария 1 уровня к Article.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        expected_text = chrome.write_a_comment()
        check_field_name(chrome.find_comment_text(), expected_text)

    def test_create_comments_1_lvl_02(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Удаление и возвращение комментария 1 уровня к Article.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий
        - Удалить комментарий
        - Через 4 секунды назать вернуть комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        expected_text = chrome.find_comment_text().text
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(3.5)
        chrome.click_btn_menu_comment()
        check_field_name(chrome.find_comment_text(), expected_text)

    def test_create_comments_1_lvl_03(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Удаление комментария 1 уровня к Article.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий
        - Удалить комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(5)
        check_field_name(chrome.find_deleted_comment_text(), 'Comment deleted by user')

    def test_create_comments_1_lvl_04(
            self, chrome_browser, create_valid_article_id, valid_cookie_new_user, valid_token_moderator,
            valid_comment_article):
        """ Удаление модератором комментария 1 уровня к Article.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий
        - Удалить комментарий модератором

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        delete_comment_id_by_moder(valid_token_moderator, valid_comment_article)
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        check_field_name(chrome.find_deleted_comment_text(), 'deleted')

    def test_create_comments_1_lvl_05(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Создание комментария 1 уровня к Answer.

        - Зайти на страницу Answer
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        expected_text = chrome.write_a_comment()
        check_field_name(chrome.find_comment_text(), expected_text)

    def test_create_comments_1_lvl_06(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Удаление и возвращение комментария 1 уровня к Answer.

        - Зайти на страницу Answer
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий
        - Удалить комментарий
        - Через 4 секунды назать вернуть комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.find_comment_text()
        expected_text = chrome.find_comment_text().text
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(3.5)
        chrome.click_btn_menu_comment()
        check_field_name(chrome.find_comment_text(), expected_text)

    def test_create_comments_1_lvl_07(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Удаление комментария 1 уровня к Answer.

        - Зайти на страницу Answer
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий
        - Удалить комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(5)
        check_field_name(chrome.find_deleted_comment_text(), 'Comment deleted by user')

    def test_create_comments_1_lvl_08(
            self, chrome_browser, create_question_with_answer, valid_cookie_new_user, valid_token_moderator,
            valid_comment_answer):
        """ Удаление модератором комментария 1 уровня к Answer.

        - Зайти на страницу Answer
        - Нажать на иконку комментариев
        - Написать комментарий
        - Опубликовать комментарий
        - Удалить комментарий модератором

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        delete_comment_id_by_moder(valid_token_moderator, valid_comment_answer)
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        check_field_name(chrome.find_deleted_comment_text(), 'deleted')

    def test_delete_created_posts(
            self, chrome_browser, valid_cookie_new_user, create_question_with_answer, create_valid_article_id):
        """ Удаление созданного вопроса и статьи.

        - Открыть страницу вопроса
        - Удалить вопрос
        - Открыть страницу профиля
        - Проверить, что вопрос удален

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если вопрос удален
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_click_delete_question()
        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_click_delete_article()
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
