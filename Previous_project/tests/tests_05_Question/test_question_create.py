""" Создание Question.
User story -
"""
import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from framework.BrowsersHelper import Chrome
from framework.check import check_element_text_is_on_page, check_field_name, check_text_field_name


class TestCreateQuestion:
    """ Question.
    """

    def test_create_question_01(self, chrome_browser, fake_question_text, valid_cookie_new_user):
        """ Публикация нового вопроса.

        - Открыть главную страницу
        - Нажать на "+" (создание поста)
        - Выбрать Question
        - На странице создания вопроса вписать Title и Description
        - Нажать кнопку опубликовать
        - Сравнить текст в эдиторе и на опубликованной странице

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param fake_question_text:
        :param valid_cookie_new_user: Куки нового юзера
        :return: OK - если новый вопрос опубликован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.make_pre_steps_for_question_create()
        chrome.write_title()
        chrome.write_description(fake_question_text)
        expected_description_from_editor = chrome.find_all_texts_in_description_blocks()
        chrome.click_btn_dark()
        chrome.write_tag()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_question_page_title_description(), expected_description_from_editor)
        # FIXME СУЧИЙ ВОПРОС!!!!!!БЕСИТ ППЦ
    # Ну уже не так сильно бесит)))

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на сепаратор')
    def test_edit_question_01(self, chrome_browser):
        """ Отредактировать вопрос: добавить сепаратор.

        - Открыть главную страницу
        - Открыть страницу вопроса
        - Нажать *** и выбрать редактировать вопрос
        - В поле description вписать текст
        - Добавить несколько элементов "separator"
        - Нажать опубликовать
        - Нажать опубликовать
        - Сравнить контент в эдиторе и на опубликованном посте

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если вопрос отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_edit()
        chrome.write_advanced_description_add_separator()
        expected_description_from_editor = chrome.find_all_texts_in_description_blocks()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_question_page_title_description(), expected_description_from_editor)
        # FIXME СУЧИЙ ВОПРОС!!!!!!БЕСИТ ППЦ
    # Ну уже не так сильно бесит)))

    def test_edit_question_02(self, chrome_browser):
        """ Отредактировать вопрос: Изменить title

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Удалить Вписанный ранее Title
        - Написать новый Title
        - Нажать опубликовать пост
        - Сравнить title, написанный в эдиторе с title на опубликованном вопросе

        ----

        Expected:
            Опубликованный заголовок точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если вопрос отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_edit()
        chrome.make_delete_content_in_title()
        chrome.write_another_title()
        expected_new_title = chrome.find_editors_title_text()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_field_name(chrome.find_title_question(), expected_new_title)

    def test_edit_question_03(self, chrome_browser):
        """ Отредактировать вопрос: ctrl+z

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Кликнуть мышью в поле description
        - Нажать Ctrl+a
        - Нажать Delete
        - Нажать Ctrl+z
        - Опубликовать
        - Сравнить текст, написанный в эдиторе с опубликованным текстом
        ----

        Expected:
            Опубликованный текст точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если вопрос отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_edit()
        expected_text = chrome.find_all_texts_in_description_blocks()
        chrome.make_delete_content_in_description()
        chrome.ctrl_z()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_question_page_title_description(), expected_text)

    def test_edit_question_04(self, chrome_browser):
        """ Отредактировать вопрос: удалить description и опубликовать

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Удалить вписанный ранее description
        - Нажать опубликовать пост
        - Сравнить вид вопроса в эдиторе с опубликованным вопросе

        ----

        Expected:
            Опубликованный пост содержит только Title

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если вопрос отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_edit()
        chrome.make_delete_content_in_description()
        chrome.write_another_title()
        expected_text = chrome.find_all_texts_in_description_blocks()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_field_name(chrome.find_title_question(), expected_text)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на кнопку изображений')
    def test_edit_question_05(self, chrome_browser, fake_question_text):
        """ Редактирование вопроса, с добавлением изображения.

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
        :return: OK - если статья отредактирована
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_edit()
        chrome.write_description(fake_question_text)
        chrome.write_description(fake_question_text)
        expected_text = chrome.find_all_texts_in_description_blocks()
        chrome.make_upload_image_in_editor()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        chrome.find_btn_show_description()
        chrome.click_btn_show_more()
        check_field_name(chrome.find_post_question_page_title_description(), expected_text)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на кнопку формулы')
    def test_edit_question_06(self, chrome_browser, my_formula):
        """ Редактирование опубликованного вопроса, с добавлением формулы.

        - Открыть главную страницу
        - Открыть страницу вопроса
        - Нажать *** и выбрать редактировать вопрос
        - В поле description добавить блочную формулу
        - Нажать опубликовать
        - Нажать опубликовать
        - Сравнить контент в эдиторе и на опубликованном вопросе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param my_formula: Текст формулы
        :return: OK - если вопрос отредактирован
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_more_question()
        chrome.click_edit()
        chrome.make_block_function(my_formula)
        exp = chrome.find_editors_text().text
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        chrome.find_btn_show_description()
        chrome.click_btn_show_more()
        check_text_field_name(chrome.find_post_question_page_title_description(), exp)

    def test_delete_question(self, chrome_browser):
        """ Удаление вопроса.

        - Открыть главную страницу
        - Открыть страницу вопроса
        - Нажать *** и выбрать "удалить вопрос"
        - Подтвердить удаление вопроса
        - Открыть страницу профиля
        - Проверить отсутствие вопроса в профиле

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если вопрос удален
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
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
