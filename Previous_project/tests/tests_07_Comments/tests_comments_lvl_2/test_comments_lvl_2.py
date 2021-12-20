""" Создание Comments lvl 2.
User story -
Docs -
"""
import time

import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, \
    check_element_text_is_on_page, check_text_field_name


class TestCommentsLvl2:
    """ Comments lvl 2.
    """

    @pytest.mark.skip(reason='Комментарий публикуется одной строкой, проверить после багфикса')
    def test_create_comments_2_lvl_01(
            self, chrome_browser, create_valid_comment_on_article_id, valid_cookie_another_user):
        """ Создание комментария 2 уровня в Article.

        - Зайти на страницу Article с имеющимися комментариями 1ур
        - Нажать на иконку комментариев
        - Нажать 'Reply', что бы ответить комменту 1ур
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_comment_on_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_another_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_comment_on_article_id}')
        chrome.make_add_cookies(valid_cookie_another_user)
        chrome.click_btn_comments()
        chrome.click_reply_to_first_comment()
        expected_text = chrome.write_a_comment_lvl_2()
        check_text_field_name(chrome.find_first_comment_text_lvl_2(), expected_text)

    @pytest.mark.skip(reason='Неправильный порядок комментариев 2ур, проверить после багфикса')
    def test_create_comments_2_lvl_02(self, chrome_browser, create_valid_comment_on_article_id, valid_cookie_new_user):
        """ Создание комментария 2 уровня на коммент 2ур в Article.

        - Зайти на страницу Article с имеющимися комментариями 1ур
        - Нажать на иконку комментариев
        - Раскрыть комментарии 2ур
        - Нажать 'Reply' на комментарии 2ур, что бы ответить комменту 2ур
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_comment_on_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_comment_on_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_comments_lvl_1()
        chrome.click_reply_to_first_comment_lvl_2()
        expected_text = chrome.write_another_comment_lvl_2()
        check_text_field_name(chrome.find_second_comment_text_lvl_2(), expected_text)

    def test_create_comments_2_lvl_03(self, chrome_browser, create_valid_comment_on_article_id, valid_cookie_new_user):
        """ Создание комментария 2 уровня на свой коммент 1ур в Article.

        - Зайти на страницу Article с имеющимися комментариями 1ур
        - Нажать на иконку комментариев
        - Раскрыть комментарии 2ур
        - Нажать 'Reply' на комментарии 2ур, что бы ответить комменту 2ур
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_comment_on_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_comment_on_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.write_a_comment()
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        chrome.click_reply_to_first_comment()
        expected_text = chrome.write_another_comment()
        check_text_field_name(chrome.find_first_comment_text_lvl_2(), expected_text)

    @pytest.mark.skip(reason='Неправильный порядок комментариев 2ур, проверить после багфикса')
    def test_create_comments_2_lvl_04(self, chrome_browser, create_valid_comment_on_article_id, valid_cookie_new_user):
        """ Создание комментария 2 уровня на свой коммент 2ур в Article.

        - Зайти на страницу Article с имеющимися комментариями 1ур
        - Нажать на иконку комментариев
        - Раскрыть комментарии 2ур
        - Нажать 'Reply' на комментарии 2ур, что бы ответить комменту 2ур
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_comment_on_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_comment_on_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_comments_lvl_1()
        chrome.click_reply_to_first_comment_lvl_2()
        expected_text = chrome.write_another_comment_lvl_2()
        check_text_field_name(chrome.find_second_comment_text_lvl_2(), expected_text)

    def test_create_comments_2_lvl_05(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Создание комментария 2 уровня на свой коммент 1ур в Answer.

        - Зайти на страницу Article с имеющимися комментариями 1ур
        - Нажать на иконку комментариев
        - Раскрыть комментарии 2ур
        - Нажать 'Reply' на комментарии 2ур, что бы ответить комменту 2ур
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.write_a_comment()
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        chrome.click_reply_to_first_comment()
        expected_text = chrome.write_another_comment()
        check_text_field_name(chrome.find_first_comment_text_lvl_2(), expected_text)

    @pytest.mark.skip(reason='Неправильный порядок комментариев 2ур, проверить после багфикса')
    def test_create_comments_2_lvl_06(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Создание комментария 2 уровня на свой коммент 2ур в Answer.

        - Зайти на страницу Article с имеющимися комментариями 1ур
        - Нажать на иконку комментариев
        - Раскрыть комментарии 2ур
        - Нажать 'Reply' на комментарии 2ур, что бы ответить комменту 2ур
        - Написать комментарий
        - Опубликовать комментарий

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_comments_lvl_1()
        chrome.click_reply_to_first_comment_lvl_2()
        expected_text = chrome.write_another_comment_lvl_2()
        check_text_field_name(chrome.find_second_comment_text_lvl_2(), expected_text)

    def test_create_comments_2_lvl_07(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Удаление комментария 1 уровня с сохранением 2-го уровня к Article.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Найти свой комментарий 1-го уровня с коммеентариями 2-го уровня
        - Удалить комментарий 1-го уровня

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_reply_to_first_comment()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(5)
        chrome.click_btn_comments_lvl_1()
        check_field_name(chrome.find_btn_comments_lvl_1(), 'Comments (1)')

    def test_create_comments_2_lvl_08(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Удаление комментария 2 уровня.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Найти свой комментарий 1-го уровня с коммеентариями 2-го уровня
        - Удалить комментарий 1-го уровня

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_comments_lvl_1()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        check_field_name(chrome.find_btn_comments_lvl_1(), 'Comments (0)')

    def test_create_comments_2_lvl_09(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Удаление комментария 1 уровня с сохранением 2-го уровня к Answer.

        - Зайти на страницу Article
        - Нажать на иконку комментариев
        - Найти свой комментарий 1-го уровня с коммеентариями 2-го уровня
        - Удалить комментарий 1-го уровня

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_reply_to_first_comment()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(5)
        chrome.click_btn_comments_lvl_1()
        check_field_name(chrome.find_btn_comments_lvl_1(), 'Comments (1)')

    def test_create_comments_2_lvl_10(self, chrome_browser, create_question_with_answer, valid_cookie_new_user):
        """ Удаление комментария 2 уровня к Answer.

        - Зайти на страницу Answer
        - Нажать на иконку комментариев
        - Найти свой комментарий 1-го уровня с коммеентариями 2-го уровня
        - Удалить комментарий 1-го уровня

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_comments_lvl_1()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        time.sleep(5)
        chrome.click_btn_comments_lvl_1()
        check_field_name(chrome.find_btn_comments_lvl_1(), 'Comments (0)')

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
