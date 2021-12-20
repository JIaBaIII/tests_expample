""" Collection create.
User story -
Docs -
"""
import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_elem_is_disable, check_elem_is_enable, \
    check_elements_texts_fields_are_empty, check_for_missing_elem


@pytest.mark.skip(reason="Пока недостаточно локаторов")
class TestCollectionEdit:
    """ Редактирование коллекции.
    """

    def test_edit_collection_01(
            self, chrome_browser, valid_cookie_new_user, fake_another_collection_name):
        """ Редактирование колекции, изменить название.


        - Открыть страницу коллекций
        - Найти созданную коллекцию
        - Нажать кнопку Edit

        Expected:
            Открывается попап с заполненными данными названия,описания и обложки карточки коллекции

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Навестись на созданную коллекцию, нажать ***
        chrome.click_edit()
        chrome.find_collection_field_name()
        chrome.make_delete_collection_name()
        expected_collection_name = chrome.write_collection_name(fake_another_collection_name)
        chrome.click_btn_save_collection()
        chrome.find_btn_collections()
        # Сравнить название коллекции с ожидаемым названием

    def test_edit_collection_02(
            self, chrome_browser, valid_cookie_new_user, fake_another_collection_description):
        """ Редактирование колекции, изменить название.


        - Открыть страницу коллекций
        - Найти созданную коллекцию
        - Нажать кнопку Edit

        Expected:
            Открывается попап с заполненными данными названия,описания и обложки карточки коллекции

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Навестись на созданную коллекцию, нажать ***
        chrome.click_edit()
        chrome.find_collection_field_name()
        expected_collection_description = chrome.write_collection_description(fake_another_collection_description)
        chrome.click_btn_save_collection()
        chrome.find_btn_collections()
        # Сравнить описание коллекции с ожидаемым описанием

    def test_edit_collection_03(
            self, chrome_browser, valid_cookie_new_user):
        """ Редактирование колекции, изменить обложку.


        - Открыть страницу коллекций
        - Найти созданную коллекцию
        - Нажать кнопку Edit
        - Загрузить новую обложку
        - Сохранить изменения

        Expected:
            Обложка коллекции изменена

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Навестись на созданную коллекцию, нажать ***
        chrome.click_edit()
        chrome.find_collection_field_name()
        # expected_collection_cover = chrome.make_upload_image_on_collection_cover() - Когда будет инпут
        chrome.click_btn_save_collection()
        chrome.find_btn_collections()
        # Сравнить обложку коллекции с ожидаемой обложкой

    def test_edit_collection_04(self, chrome_browser, valid_cookie_new_user):
        """ Редактирование колекции, сделать коллекцию публичной.


        - Открыть страницу коллекций
        - Найти созданную коллекцию
        - Нажать кнопку Edit
        - Сделать коллекцию публичной
        - Сохранить изменения

        Expected:
            Коллекция стала публичной

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Навестись на созданную коллекцию, нажать ***
        chrome.click_edit()
        chrome.find_collection_field_name()
        chrome.click_collection_checkbox_make_it_publish()
        chrome.click_btn_save_collection()
        chrome.find_btn_collections()
        # Подтвердить, что коллекция стала публичной

    def test_edit_collection_05(self, chrome_browser, valid_cookie_new_user,
                                fake_another_collection_description, fake_another_collection_name):
        """ Перейти в редактирование коллекции из страницы самой колеекции.


        - Открыть страницу коллекций
        - Найти созданную коллекцию
        - Открыть коллекцию
        - Нажать кнопку Edit
        - Изменить название и описание коллекции
        - Сохранить изменения

        Expected:
            Название и описание коллекции изменены

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Открыть страницу коллекции
        # Кликнуть ***
        chrome.click_edit()
        chrome.find_collection_field_name()
        chrome.write_collection_name(fake_another_collection_name)
        chrome.write_collection_description(fake_another_collection_description)
        chrome.click_btn_save_collection()
        chrome.find_btn_collections()
        # Подтвердить, что название и описание коллекции изменены

    def test_edit_collection_06(self, chrome_browser, valid_cookie_new_user,
                                fake_another_collection_description, fake_another_collection_name):
        """ Удалить элемент из коллекции.


        - Открыть страницу коллекций
        - Найти созданную коллекцию
        - Открыть коллекцию
        - Нажать кнопку *** на добавленном элементе
        - Удалить элемент
        - Сохранить изменения
        - Проверить отсутствие элемента  в коллекции

        Expected:
            Элемент удален из коллекции

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Открыть страницу коллекции
        # Кликнуть *** на элементе коллекции
        chrome.click_menu_item_delete()
        # Подтвердить удаление ?
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Открыть коллекцию
        # Подтвердить, что элемент удален из коллекции

    def test_edit_collection_07(self, chrome_browser, valid_cookie_new_user,
                                fake_another_collection_description, fake_another_collection_name):
        """ Добавить элемент из одной коллекции в другую.


        - Добавить элемент в коллекцию 1
        - Открыть страницу коллекций
        - Открыть коллекцию 1
        - Нажать кнопку *** на добавленном элементе
        - Выбрать добавление в коллекцию
        - Выбрать коллекцию 2
        - Сохранить изменения
        - Открыть коллекцию 2
        - Проверить наличие элемента в коллекции 2

        Expected:
            элемент находится в коллекции 2

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Открыть страницу коллекции
        # Кликнуть *** на элементе коллекции
        # Выбрать добавить в коллекцию
        # Выбрать коллекцию 2
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Открыть коллекцию 2
        # Подтвердить, что элемент удален из коллекции

    def test_edit_collection_08(self, chrome_browser, valid_cookie_new_user,
                                fake_another_collection_description, fake_another_collection_name):
        """ Изменить расположение элементов в коллекции.


        - Добавить элемент A, B, C в коллекцию
        - Открыть страницу коллекций
        - Открыть коллекцию 1
        - ?
        - Передвинуть элементы так, что бы расположение было : C, B, A
        - Сохранить изменения
        - Проверить расположение элементов

        Expected:
            элементы в коллекции находятся в новом поряжке: C, B, A

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        # Предшаги: Добавить в коллекцию 3 элемента
        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Открыть страницу коллекции с 3-мя элементами
        # ?
        # Передвинуть элементы так, что бы расположение было : C, B, A
        # Сохранить изменения
        # Проверить расположение элементов
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        # Подтвердить расположение элементов
