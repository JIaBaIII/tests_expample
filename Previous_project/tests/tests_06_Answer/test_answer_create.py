""" Создание Answer.
User story -
Docs -
"""

import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_text_field_name, check_element_is_on_page, \
    check_element_text_is_on_page


class TestAnswerCreate:
    """ Answer.
    """

    def test_create_answer_01(self, chrome_browser, create_valid_question_id, fake_answer_text, valid_cookie_new_user):
        """ Публикация нового ответа.

        - Открыть страницу вопроса
        - Нажать кнопку "Ответить"
        - Ввести текст
        - Нажать кнопку опубликовать ответ
        - Подтвердить публикацию
        - Проверить текст в опубликованном посте тексту отображаемом в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :param fake_answer_text: Текст, вводимый в поле Description
        :param valid_cookie_new_user: Куки нового юзера
        :return: OK - если новый ответ опубликован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_answer()
        chrome.write_description(fake_answer_text)
        expected_description_from_editor = chrome.find_all_texts_in_description_blocks()
        chrome.click_post_answers_and_post_answer()
        chrome.click_to_open_answers_page()
        check_field_name(chrome.find_description_text(), expected_description_from_editor)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на сепаратор')
    def test_edit_answer_01(self, chrome_browser, create_valid_question_id):
        """ Редактирование ответа: Добавление сепаратора

        - Открыть вопрос
        - Нажать на *** на ответе
        - Выбрать "Редактировать ответ"
        - Добавить элемент "separator"
        - Нажать кнопку опубликовать ответ
        - Подтвердить публикацию
        - Проверить текст в опубликованном посте тексту отображаемом в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если ответ отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.click_question_page_menu_answer()
        chrome.click_edit()
        chrome.write_advanced_description_add_separator()
        expected_description_from_editor = chrome.find_all_texts_in_description_blocks()
        chrome.click_edit_answer_btn_submit()
        chrome.click_post_answer()
        check_field_name(chrome.find_description_text(), expected_description_from_editor)

    def test_edit_answer_02(self, chrome_browser, create_valid_question_id, valid_cookie_new_user):
        """ Просмотр вопроса со страницы создания ответа.

        - Открыть страницу вопроса
        - Нажать Answer
        - Раскрыть вопрос
        - Сравнить текст с вопросом

        :param chrome_browser:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_answer()
        expected_question_text = chrome.find_post_question_page_title_description()
        chrome.click_answer()
        chrome.find_create_answer_page_show_question()
        chrome.click_create_answer_page_show_question()
        check_text_field_name(chrome.find_create_answer_question_page_title_description(), expected_question_text)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на кнопку изображения')
    def test_edit_answer_03(self, chrome_browser, create_valid_question_id):
        """ Редактирование ответа, с добавлением изображения.

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Создать пустую строку, для того, что бы отобразился toolbar
        - Загрузить .gif через блок "Images"
        - Опубликовать
        - Сравнить текст, написанный в эдиторе с опубликованным текстом
        ----

        Expected:
            Опубликованный текст точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если статья отредактирована
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.click_question_page_menu_answer()
        chrome.click_edit()
        expected_text = chrome.find_all_texts_in_description_blocks()
        chrome.make_upload_image_in_editor_answer()
        chrome.click_edit_answer_btn_submit()
        chrome.click_post_answer()
        check_field_name(chrome.find_post_article_page_title_description(), expected_text)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на кнопку формулы')
    def test_edit_answer_04(self, chrome_browser, my_formula, create_valid_question_id):
        """ Редактирование ответа: Добавление формулы.

        - Открыть страницу вопроса
        - На ответе нажать на ***
        - Выбрать "редактировать ответ"
        - Через "+" добавить формулу
        - Нажать кнопку опубликовать ответ
        - Подтвердить публикацию
        - Проверить отображение формулы в эдиторе и на опубликованном ответе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param my_formula: Формула, добавляемая через "+"
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если ответ отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.click_question_page_menu_answer()
        chrome.click_edit()
        chrome.make_block_function(my_formula)
        expected_formula_text_from_editor = chrome.find_text_of_formula()
        chrome.click_edit_answer_btn_submit()
        chrome.click_post_answer()
        check_text_field_name(chrome.find_text_of_formula(), expected_formula_text_from_editor)

    def test_answer_count_feed(self, chrome_browser, valid_cookie_new_user):
        """ Просмотр кол-ва ответов с feed.

        - Открыть страницу feed
        - Найти наш вопрос с 1 ответом

        :param chrome_browser:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        check_field_name(chrome.find_on_feed_count_answers(), '1 answers')

    def test_answer_count_question_page(self, chrome_browser, valid_cookie_new_user):
        """ Просмотр кол-ва ответов со страницы вопроса.

        - Открыть страницу feed
        - Найти наш вопрос с 1 ответом

        :param chrome_browser:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        check_field_name(chrome.find_question_page_count_answers(), '1answers')

    def test_delete_answer(self, chrome_browser, create_valid_question_id):
        """ Удаление ответа.

        - Открыть страницу вопросаэ
        - На ответе нажать на ***
        - Выбрать "Удалить ответ"
        - Подтвердить удаление
        - Проверить, что ответ удален

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если ответ удален
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.click_to_open_answers_page()
        chrome.click_btn_menu_answer_page()
        chrome.click_menu_item_delete_answer()
        chrome.click_btn_blue()
        chrome.find_question_page_container()
        check_element_is_on_page('AnswerItem_removed__GP-f_', chrome)

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
