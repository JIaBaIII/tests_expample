""" Тестипование наименований в попапе Sign up.
User story -
Docs -
"""
from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_elem_is_disable


class TestPopupSignUp:
    """ Тесты на соответствие наименований элементов в попапе Sign up.
    """

    def test_elem_popup_sign_up_01(self, chrome_browser):
        """ Текст в попапе 'Welcome to TOCI'.

        - Открыть главную страницу
        - Открыть попап "регистрация"
        - Проверить текст в шапке попапа

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.find_pop_up_text_welcome(), 'Welcome to TOCI!')

    def test_elem_popup_sign_up_02(self, chrome_browser):
        """ Поле ввода 'Login'.

        - Открыть главную страницу
        - Открыть попап "регистрация"
        - Проверить название поля ввода логина

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.find_pop_up_text_login(), 'Name')

    def test_elem_popup_sign_up_03(self, chrome_browser):
        """ Поле ввода 'Password'.

        - Открыть главную страницу
        - Открыть попап "регистрация"
        - Проверить название поля ввода пароля

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.find_pop_up_text_password(), 'Password')

    def test_elem_popup_sign_up_04(self, chrome_browser):
        """ Кнопка 'Continue'.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.find_btn_red(), 'Continue')

    def test_elem_popup_sign_up_05(self, chrome_browser):
        """ Кнопка 'Sign in'.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.find_pop_up_btn_sign_in(), 'Sign in')

    def test_elem_popup_sign_up_06(self, chrome_browser):
        """ Текст в попапе о приватности.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Проверить текст в элементе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.find_pop_up_text_privacy(),
                         "By signing up, I agree to Terms of Service and Privacy Policy.\nTOCI can send me personalized"
                         " newsletters by email. To find out more or opt out of these communications at any time, "
                         "see the Privacy PolicyPrivacy Policy.")

    def test_elem_popup_sign_up_07(self, chrome_browser):
        """ Ошибка пользователя: под полем 'Login' - 'This field is required'.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Вписать только пароль
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_required_login(), 'This field is required') \
            and check_elem_is_disable(chrome.find_btn_red())

    def test_elem_popup_sign_up_08(self, chrome_browser):
        """ Ошибка пользователя: под полем 'Password' - 'This field is required'.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Вписать только логин
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_required_password(), 'This field is required') \
            and check_elem_is_disable(chrome.find_btn_red())

    def test_elem_popup_sign_up_09(self, chrome_browser):
        """ Ошибка пользователя, Логин < 3 символов: 'does not match pattern "^[0-9a-zA-Z_]{3,20}$"'.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Вписать не валидный логин и валидный пароль
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_login_pattern(), 'Must be at least 3 characters long') \
            and check_elem_is_disable(chrome.find_btn_red())

    def test_elem_popup_sign_up_10(self, chrome_browser):
        """ Ошибка пользователя, Логин > 20 символов: 'does not match pattern "^[0-9a-zA-Z_]{3,20}$"'.

        - Открыть главную страницу
        - Открыть попап "регистрации"
        - Вписать не валидный логин и валидный пароль
        - Нажать на кнопку подтверждения регистрации
        - Проверить текст в ошибке

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_login_pattern_21(), 'does not match pattern "^[0-9a-zA-Z_]{3,20}$"')

    def test_elem_popup_sign_up_11(self, chrome_browser):
        """ Ошибка пользователя: под полем 'Password' - 'Must be at least 6 characters long'.

        - Вести валидный Login
        - Ввести не валидный пароль из 1-5 знаков

        ----

        Expected:
            Кнопка подтверждения регистрации не нажимается.

            Надпись под полем ввода пароля "Must be at least 6 characters long"

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_count_password_len(), 'Must be at least 6 characters long')

    def test_elem_popup_sign_up_12(self, chrome_browser):
        """ Ошибка пользователя: Логин и пароль одинаковы.

        - Ввести валидный логин
        - В качестве пароля использоваться тот же логин

        ----

        Expected:
            Не должна происходить регистрация.

            Под окном регистрации появляется ошибка:

            "password: error The password can not be used because the password is too similar to the user identifier."

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_similar(),
                         'The password can not be used because the password is too similar to the user identifier.')

    def test_elem_popup_sign_up_13(self, chrome_browser):
        """ Ошибка пользователя: Простой пароль (6 цифр).

        - Ввести валидный логин
        - Ввести простой пароль

        ----

        Expected:
            Не должна происходить регистрация.

            Под окном регистрации появляется ошибка

            "The password can not be used because the password
            has been found in data breaches and must no longer be used."

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_simple_password(),
                         'The password can not be used because the password '
                         'has been found in data breaches and must no longer be used.')

    def test_elem_popup_sign_up_14(self, chrome_browser):
        """ Ошибка пользователя: Простой пароль (6 маленьких букв).

        - Ввести валидный логин
        - Ввести простой пароль

        ----

        Expected:
            Не должна происходить регистрация.

            Под окном регистрации появляется ошибка

            "The password can not be used because the password
            has been found in data breaches and must no longer be used."

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_simple_password_down_letter(),
                         'The password can not be used because the password '
                         'has been found in data breaches and must no longer be used.')

    def test_elem_popup_sign_up_15(self, chrome_browser):
        """ Ошибка пользователя: Простой пароль (6 больших букв).

        - Ввести валидный логин
        - Ввести простой пароль

        ----

        Expected:
            Не должна происходить регистрация.

            Под окном регистрации появляется ошибка

            "The password can not be used because the password
            has been found in data breaches and must no longer be used."

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если текст соответствует
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_btn_sign_up()
        check_field_name(chrome.make_pop_up_warning_simple_password_down_letter(),
                         'The password can not be used because the password '
                         'has been found in data breaches and must no longer be used.')
