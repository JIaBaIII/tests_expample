""" Тестипование наименований элементов.
User story -
Docs -
"""
import time

import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_element_text_is_on_page, check_text_field_name


class TestCommentsNaming1:
    """ Соответсввие наименования элементов, связанных с комментариями.
    """

    def test_elem_comments_1_lvl_01(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Кол-вл комментариев в шторке Article (0).

        - Зайти на страницу Article
        - Нажать на иконку комментариев

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        check_field_name(chrome.find_comments_title(), 'Comments (0)')

    def test_elem_comments_1_lvl_02(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Кол-вл комментариев в шторке Article (1).

        - Зайти на страницу Article
        - Нажать на иконку комментариев

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.write_a_comment()
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        check_field_name(chrome.find_comments_title(), 'Comments (1)')

    def test_elem_comments_1_lvl_03(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Кол-вл комментариев в шторке Article (2).

        - Зайти на страницу Article
        - Нажать на иконку комментариев

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.write_a_comment()
        check_field_name(chrome.find_comments_title(), 'Comments (2)')

    @pytest.mark.xfail(reason='Счетчик Article еще не починен')
    def test_elem_comments_1_lvl_04(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Кол-вл комментариев на странице Article (2).

        - Зайти на страницу Article
        - Нажать на иконку комментариев

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome_browser.refresh()
        time.sleep(0.4)
        check_field_name(chrome.find_comments_btn(), '2 Comments')

    def test_elem_comments_1_lvl_05(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Кол-вл комментариев в шторке Article (1) (Удалить 1 коммент).

        - Зайти на страницу Article
        - Нажать на иконку комментариев

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
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        check_field_name(chrome.find_comments_title(), 'Comments (1)')

    @pytest.mark.xfail(reason='Счетчик Article еще не починен')
    def test_elem_comments_1_lvl_06(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
        """ Кол-вл комментариев на странице Article (1) (После удаления 1 коммента).

        - Зайти на страницу Article
        - Нажать на иконку комментариев

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        check_field_name(chrome.find_comments_btn(), '1 Comments')

    @pytest.mark.xfail(reason='Счетчик Article еще не починен')
    def test_elem_comments_1_lvl_07(self, chrome_browser, valid_cookie_new_user):
        """ Кол-вл комментариев на карточке Article в Feed (1).

        - Найти в Feed созданный Article с 1 комментарием

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        check_field_name(chrome.find_on_feed_count_comments(), '1 comments')

    def test_elem_comments_1_lvl_08(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев (0) на Answer (Страница Question).

        - Зайти на страницу Question с Answer
        - Найти комментарии к ответу

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        check_field_name(chrome.find_comments_btn(), '0 comments')

    def test_elem_comments_1_lvl_09(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев (1) на Answer (Страница Question).

        - Зайти на страницу Question с Answer
        - Найти комментарии к ответу

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
        chrome.go_to_site(f'/question/{create_question_with_answer}')
        check_field_name(chrome.find_comments_btn(), '1 comments')

    def test_elem_comments_1_lvl_10(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев (2) на Answer (Страница Question).

        - Зайти на страницу Question с Answer
        - Найти комментарии к ответу

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.write_another_comment()
        chrome_browser.refresh()
        time.sleep(0.4)
        check_field_name(chrome.find_comments_btn(), '2 comments')

    def test_elem_comments_1_lvl_11(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев в шторке (2) на Answer.

        - Зайти на страницу Question с Answer
        - Найти комментарии к ответу

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        check_field_name(chrome.find_comments_title(), 'Comments (2)')

    def test_elem_comments_1_lvl_12(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев (1) на Answer (Страница Question. После удаления 1 коммента).

        - Зайти на страницу Question с Answer
        - Найти комментарии к ответу

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.click_btn_menu_comment()
        chrome.click_menu_btn_delete()
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        check_field_name(chrome.find_comments_title(), 'Comments (1)')

    def test_elem_comments_1_lvl_13(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев в шторке (1) на Answer.

        - Зайти на страницу Question с Answer
        - Найти комментарии к ответу

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        chrome.find_comments_title()
        check_field_name(chrome.find_comments_title(), 'Comments (1)')

    def test_elem_comments_1_lvl_14(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Кол-вл комментариев (1) на странице Answer.

        - Зайти на страницу Question с Answer
        - Открыть страницу Answer
        - Найти комментарии к ответу

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_to_open_answers_page()
        check_field_name(chrome.find_answer_page_comments_count(), '1')

    def test_elem_comments_1_lvl_15(self, chrome_browser, valid_cookie_new_user, create_question_with_answer):
        """ Плейсхолдер поля ввода текста.

        - Зайти на страницу Question с Answer
        - Открыть комментарии

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_question_with_answer: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_comments_btn()
        chrome.click_btn_comments()
        check_text_field_name(chrome.find_comment_placeholder_field_text(), 'Share your thoughts')

    def test_elem_comments_1_lvl_16(self, chrome_browser, valid_cookie_new_user, create_valid_article_id):
        """ Кол-вл комментариев у комментария 1ур (0) на странице Article.

        - Открыть на страницу Article
        - Найти комментарий 1ур
        - Проерить кол-во комментариев 2ур

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_comments()
        check_field_name(chrome.find_btn_comments_lvl_1(), 'Comments (0)')

    @pytest.mark.skip(reason='Сломался счетчик комментов, проверить после багфикса')
    def test_elem_comments_1_lvl_17(self, chrome_browser, valid_cookie_another_user, create_valid_article_id):
        """ Кол-вл комментариев у комментария 1ур (1) на странице Article.

        - Открыть на страницу Article
        - Найти комментарий 1ур
        - Написать к нему комментарий 2ур
        - Перезагрузить страницу
        - Проерить кол-во комментариев 2ур к комментарию 1ур

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_article_id: Фикстура для поолучения QuestionID, созданного бэком
        :param valid_cookie_another_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_another_user)
        chrome.click_btn_comments()
        chrome.click_reply_to_first_comment()
        chrome.write_a_comment_lvl_2()
        chrome_browser.refresh()
        time.sleep(0.4)
        chrome.click_btn_comments()
        check_field_name(chrome.find_btn_comments_lvl_1(), 'Comments (1)')

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
