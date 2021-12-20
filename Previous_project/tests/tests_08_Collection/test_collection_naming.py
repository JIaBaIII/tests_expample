""" Тестипование наименований в попапе Collection create.
User story -
Docs -
"""

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_text_field_name, check_expected_text_is_in_element, \
    check_elem_is_disable


class TestCollectionPopupNaming:
    """ Тесты на соответствие наименований элементов в попапе создания коллекции.
    """

    def test_collection_popup_naming_01(self, chrome_browser, valid_cookie_new_user):
        """ Create new collection.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти заголовок попапа создания коллекции

        Expected:
            'Create new collection'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_field_name(chrome.find_create_new_collection_popup_title(), 'Create new collection')

    def test_collection_popup_naming_02(self, chrome_browser, valid_cookie_new_user):
        """ Create new collection button.

        - Открыть страницу всех коллекций
        - Найти кнопку "Создать новую коллекцию"

        Expected:
            'Create new collection'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        check_field_name(chrome.find_create_new_collection_btn(), 'Create new collection')

    def test_collection_popup_naming_03(self, chrome_browser, valid_cookie_new_user):
        """ Create new collection card.

        - Открыть страницу всех коллекций
        - Найти карточку "Создать новую коллекцию"

        Expected:
            'Create new collection'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        check_field_name(chrome.find_create_new_collection_card(), 'Create new collection')

    def test_collection_popup_naming_04(self, chrome_browser, valid_cookie_new_user):
        """ My collections tab.

        - Открыть страницу всех коллекций
        - Найти вкладку "мои коллекции"

        Expected:
            'My collections'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        check_expected_text_is_in_element(chrome.find_my_collection_tab(), 'My collections')

    def test_collection_popup_naming_05(self, chrome_browser, valid_cookie_new_user):
        """ Subscriptions tab.

        - Открыть страницу всех коллекций
        - Найти вкладку "Subscriptions"

        Expected:
            'Subscriptions'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        check_expected_text_is_in_element(chrome.find_subscriptions_collection_tab(), 'Subscriptions')

    def test_collection_popup_naming_06(self, chrome_browser, valid_cookie_new_user):
        """ Quotes tab.

        - Открыть страницу всех коллекций
        - Найти вкладку "Quotes"

        Expected:
            'Quotes'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        check_expected_text_is_in_element(chrome.find_quotes_tab(), 'Quotes')

    def test_collection_popup_naming_07(self, chrome_browser, valid_cookie_new_user):
        """ Liked tab.

        - Открыть страницу всех коллекций
        - Найти вкладку "Liked"

        Expected:
            'Liked'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        check_expected_text_is_in_element(chrome.find_liked_tab(), 'Liked')

    def test_collection_popup_naming_08(self, chrome_browser, valid_cookie_new_user):
        """ Collection name.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти надпись "Имя коллекции"

        Expected:
            'Name'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_field_name(chrome.find_create_new_collection_popup_name(), 'Name')

    def test_collection_popup_naming_09(self, chrome_browser, valid_cookie_new_user):
        """ Collection field name.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти надпись поля ввода для названия коллекции

        Expected:
            'New collection'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_text_field_name(chrome.find_collection_field_name().get_attribute('placeholder'),
                              'New collection')

    def test_collection_popup_naming_10(self, chrome_browser, valid_cookie_new_user):
        """ Collection Description.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти надпись "Описание коллекции"

        Expected:
            'Description'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_field_name(chrome.find_create_new_collection_popup_description(), 'Description')

    def test_collection_popup_naming_11(self, chrome_browser, valid_cookie_new_user):
        """ Collection field description.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти надпись поля ввода для описания коллекции

        Expected:
            'Brief description of the collection...'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_text_field_name(chrome.find_collection_field_description().get_attribute('placeholder'),
                              'Brief description of the collection...')

    def test_collection_popup_naming_12(self, chrome_browser, valid_cookie_new_user):
        """ Кнопка 'Create a new collection'.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти кнопку 'Create a new collection'

        Expected:
            'Create a new collection'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_field_name(chrome.find_create_new_collection_popup_btn_save(), 'Create a new collection')

    def test_collection_popup_naming_13(self, chrome_browser, valid_cookie_new_user):
        """ Неитерабельность кнопки 'Save'.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти кнопку 'Save'

        Expected:
            'Save'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_elem_is_disable(chrome.find_create_new_collection_popup_btn_save())

    def test_collection_popup_naming_14(self, chrome_browser, valid_cookie_new_user):
        """ Кнопка 'Cancel'.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти кнопку 'Cancel'

        Expected:
            'Cancel'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_field_name(chrome.find_create_new_collection_popup_btn_cancel(), 'Cancel')

    def test_collection_popup_naming_15(self, chrome_browser, valid_cookie_new_user):
        """ Кнопка 'Добавить обложку'.

        - Открыть страницу всех коллекций
        - Нажать кнопку "Создать коллекцию"
        - Найти кнопку 'Добавить обложку'

        Expected:
            'Add an image for the cover'

        :param chrome_browser:
        :param valid_cookie_new_user:
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_see_all_collections()
        chrome.click_btn_create_new_collection()
        check_field_name(chrome.find_btn_add_picture_to_collection(), 'Add an image for the cover')

    def test_delete_all_cookies(self, chrome_browser):
        """ Удалить использованные в этом классе куки.

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если использованные в этом классе куки удалены
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome_browser.delete_all_cookies()
