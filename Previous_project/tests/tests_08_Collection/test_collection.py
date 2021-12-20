""" Collection create.
User story -
Docs -
"""

import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_element_text_is_on_page


class TestCollection:
    """ Создание коллекции.
    """

    def test_create_collection_01(
            self, chrome_browser, valid_cookie_new_user, fake_collection_name):
        """ Создание новой коллекции (Вписать только название).

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Вписать название коллекции
        - Нажать кнопку "создать коллекцию"

        Expected:
            Карточка новой коллекции создана.

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        expected_collection_name = chrome.write_collection_name(fake_collection_name)
        chrome.click_btn_save_collection()
        chrome_browser.refresh()
        check_field_name(chrome.find_collection_title(), expected_collection_name)

    def test_create_collection_02(
            self, chrome_browser, valid_cookie_new_user, fake_another_collection_name, fake_collection_description):
        """ Создание новой коллекции (Вписать только название и описание).

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Вписать название коллекции
        - Вписать описание коллекции
        - Нажать кнопку "создать коллекцию"

        Expected:
            Карточка новой коллекции создана.

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        expected_collection_name = chrome.write_collection_name(fake_another_collection_name)
        expected_collection_description = chrome.write_collection_description(fake_collection_description)
        chrome.click_btn_save_collection()
        chrome_browser.refresh()
        check_field_name(chrome.find_exactly_collection_title_name(expected_collection_name), expected_collection_name)
        # check_field_name() fixme для description, когда будет

    def test_create_collection_03(
            self, chrome_browser, valid_cookie_new_user, fake_collection_description):
        """ Создание новой коллекции (Вписать название, описание, добавить обложку).

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Вписать название коллекции
        - Вписать описание коллекции
        - Загрузить обложку коллекции
        - Нажать кнопку "создать коллекцию"

        Expected:
            Карточка новой коллекции создана.

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        expected_collection_name = chrome.write_collection_name('Третья коллекция, с картинкой и описанием))')
        expected_collection_description = chrome.write_collection_description(fake_collection_description)
        chrome.make_upload_image_on_collection_cover()
        chrome.click_btn_save_collection()
        chrome_browser.refresh()
        check_field_name(chrome.find_exactly_collection_title_name(expected_collection_name), expected_collection_name)
        # check_field_name() fixme для description, когда будет

    def test_create_collection_04(self, chrome_browser, valid_cookie_new_user, fake_collection_name,
                                  create_valid_article_id):
        """ Добавить Article в коллекцию .

        - Открыть Feed
        - Нажать кнопку сохранить в коллекцию Article
        - Выбрать первую коллекцию
        - Открыть страницу коллекций
        - Найти созданную коллекцию

        Expected:
            Статья добавлена в колекцию

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_on_feed()
        chrome.click_feed_save_article_btn()
        chrome.click_feed_select_save_to_exactly_collection(fake_collection_name)
        chrome.click_btn_see_all_collections()
        check_field_name(chrome.find_collection_cards_amount(), '1 cards')

    def test_create_collection_05(self, chrome_browser, valid_cookie_new_user, fake_another_collection_name,
                                  create_valid_article_id):
        """ Добавить Article в несколько коллекций .

        - Открыть Feed
        - Нажать кнопку сохранить в коллекцию Article
        - Выбрать вторую коллекцию
        - Выбрать третью коллекцию
        - Открыть страницу коллекций
        - Найти созданные коллекции

        Expected:
            Статья добавлена в несколько колекций

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_on_feed()
        chrome.click_feed_save_article_btn()
        chrome.click_feed_select_save_to_exactly_collection(fake_another_collection_name)
        # chrome.click_feed_save_article_btn()  # Ждет баг-фикса
        chrome.click_feed_select_save_to_exactly_collection('Третья коллекция, с картинкой и описанием))')
        chrome.click_btn_see_all_collections()
        check_field_name(chrome.find_second_collection_cards_amount(), '1 cards')
        check_field_name(chrome.find_third_collection_cards_amount(), '1 cards')

    @pytest.mark.skip(reason="Пока недостаточно локаторов")
    def test_create_collection_06(
            self, chrome_browser, valid_cookie_new_user,
            fake_collection_name, fake_collection_description, create_question_with_answer):
        """ Добавить Answer в коллекцию .

        - Открыть Feed
        - Отркыть вопрос с ответом
        - Нажать кнопку сохранить в коллекцию Answer
        - Выбрать нескоько коллекций
        - Открыть страницу коллекций
        - Найти Answer в коллекции

        Expected:
            Answer добавлен в коллекцию

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'{create_question_with_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_create_new_collection()
        chrome.find_collection_field_name()
        expected_collection_name = chrome.write_collection_name(fake_collection_name)
        expected_collection_description = chrome.write_collection_description(fake_collection_description)
        chrome.click_btn_save_collection()
        chrome.find_btn_collections()
        chrome.click_btn_see_all_collections()

    @pytest.mark.skip(reason="Пока недостаточно локаторов")
    def test_create_collection_07(
            self, chrome_browser, valid_cookie_new_user, fake_collection_name, fake_collection_description):
        """ Добавить Answer в несколько коллекций .

        - Открыть Feed
        - Нажать кнопку сохранить в коллекцию Article
        - Выбрать несколько коллекций
        - Открыть страницу коллекций
        - Найти коллекции, в которых добавлена статья, проверить

        Expected:
            Answer добавлен в несколько коллекций


        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_on_feed()
        chrome.click_feed_save_article_btn()
        chrome.click_btn_save_collection()
        chrome.click_btn_see_all_collections()

    @pytest.mark.skip(reason="Пока недостаточно локаторов")
    def test_create_collection_08(
            self, chrome_browser, valid_cookie_new_user):
        """ Удаление коллекции.

        - Открыть страницу всех коллекций

        Expected:
            Карточка новой коллекции создана.

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        # Найти *** на нужной коллекции
        # Нажать на контектсное меню, выбрать удалить
        # Попап подтверждения?
        # Проверить, что коллекция удалена (Возможно проверить корзину)

    @pytest.mark.skip(reason="Пока недостаточно локаторов")
    def test_create_collection_09(
            self, chrome_browser, valid_cookie_new_user):
        """ Удаление нескольких коллекций.

        - Открыть страницу всех коллекций

        Expected:
            Карточка новой коллекции создана.

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        # Найти выбор нескольких элементов, нажать
        # Выбрать удалить
        # Попап подтверждения?
        # Проверить, что коллекции удалены (Возможно проверить корзину)

    def test_delete_all_cookies(self, chrome_browser):
        """ Удалить использованные в этом классе куки.

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если использованные в этом классе куки удалены
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome_browser.delete_all_cookies()

    def test_delete_article(self, chrome_browser, valid_cookie_new_user, create_valid_article_id):
        """Удаление добавленной статьи.

        - Открыть главную страницу
        - Открыть страницу Article
        - Нажать на ***
        - Выбрать "Удалить"
        - Подтвердить удаление
        - Перейти на страницу своего профиля
        - Проверить, что Article удален

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья удалена
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.make_click_delete_article()
        chrome.go_to_site('/profile/')
        check_element_text_is_on_page(chrome.find_profile_no_published_data(), chrome)
