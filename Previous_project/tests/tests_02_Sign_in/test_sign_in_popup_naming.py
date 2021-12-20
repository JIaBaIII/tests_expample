""" Тестирование наименований попапа "Sign in".
User story -
"""
from framework.BrowsersHelper import Chrome
from framework.check import check_field_name


class TestPopupSignIn:
    """ Тесты на соответствие наименований элементов в попапе Sign in.
    """

    def test_elem_popup_sign_in_01(self, chrome_browser):
        """ Текст в попапе 'Welcome to TOCI'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Сравнить текст в шапке попапа

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_pop_up_text_welcome(), 'Login on TOCI')

    def test_elem_popup_sign_in_02(self, chrome_browser):
        """ Поле ввода 'Name'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Проверить название поля ввода логина

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_pop_up_text_login(), 'Name')

    def test_elem_popup_sign_in_03(self, chrome_browser):
        """ Поле ввода 'Password'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Проверить название поля ввода пароля

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_pop_up_text_password(), 'Password')

    def test_elem_popup_sign_in_04(self, chrome_browser):
        """ Кнопка 'Forgot password?'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_pop_up_text_forgot_password(), 'Forgot password?')

    def test_elem_popup_sign_in_05(self, chrome_browser):
        """ Чек-бокс 'Require code at login'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_pop_up_text_checkbox_require_at_login(), 'Require code at login')

    def test_elem_popup_sign_in_06(self, chrome_browser):
        """ Кнопка 'Sign in TOCI'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_btn_red(), 'Sign in TOCI')

    def test_elem_popup_sign_in_07(self, chrome_browser):
        """ Кнопка 'Sign up now'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.find_pop_up_btn_create_account(), 'Sign up now')

    def test_elem_popup_sign_in_08(self, chrome_browser):
        """ Ошибка пользователя: под полем 'Login' - 'This field is required'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Вписать только пароль
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.make_pop_up_warning_required_login(), 'This field is required')

    def test_elem_popup_sign_in_09(self, chrome_browser):
        """ Ошибка пользователя: под полем 'Password' - 'This field is required'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Вписать только логин
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.make_pop_up_warning_required_password(), 'This field is required')

    def test_elem_popup_sign_in_10(self, chrome_browser):
        """ Ошибка пользователя: 'The provided credentials are invalid...'.

        - Открыть главную страницу
        - Открыть попап "авторизации"
        - Вписать не валидные логин и пароль
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_in()
        check_field_name(chrome.make_pop_up_warning_invalid(),
                         'The provided credentials are invalid, check for spelling '
                         'mistakes in your password or username, email address, or phone number.')
