""" Registration.
User story - https://www.notion.so/hipasus/c3f35090668c4044875e29e5d58f3c91
Docs - https://www.notion.so/hipasus/1a5fa44804644017a977caa5ccdd921b
"""

from framework.BrowsersHelper import Chrome
from framework.check import check_for_missing_elem, check_field_name

# findme fixme Есть одна проблемка, нельзя со списка справа двойноым лкм перейти на сам тест...


class TestSignUpUser:
	""" Регистрация.
	"""

	def test_sign_up_01(self, chrome_browser, sign_up_login_3_password):
		""" Зарегистрировать нового пользователя Login 3 символа.

		- Открыть главную страницу Toci
		- Нажать на кнопку регистрации (Sign up)
		- Закрыть окно регистрации
		- Открыть попап регистрации
		- В всплывающем окне ввести валидный Логин (3 символа) и валидный Пароль.
		- Нажать кнопку подтверждения

		----

		Expected:
			Новый пользователь зарегистрирован

		Неявные проверки:

		- Появляется всплывающее окно с полями для ввода логина и пароля
		- Окно регистрации закрылось. Пользователь видит главную страницу toci
		- Регистрация нового пользователя

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param sign_up_login_3_password: фикстура - генератор логина и пароля
		:return: OK - если регистрация прошла успешно
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_btn_sign_up()
		chrome.click_close_popup()
		chrome.click_btn_sign_up()
		chrome.enter_login(sign_up_login_3_password['Login'])
		chrome.enter_password(sign_up_login_3_password['Password'])
		chrome.click_btn_continue()
		chrome.find_my_avatar()
		check_for_missing_elem('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_logout_01(self, chrome_browser):
		""" Сделать Log out.

		- Log out
		- Проверка успешного выхода из аккаунта

		----

		Expected: Log out успешно выполнен

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если  log out успешно выполнен
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_on_my_avatar()
		chrome.click_log_out()
		check_field_name(chrome.find_btn_sign_in(), 'Sign in')

	def test_sign_up_02(self, chrome_browser, sign_up_login_10_password):
		""" Зарегистрировать нового пользователя Login 10 символов.

		- Открыть главную страницу Toci
		- Нажать на кнопку регистрации (Sign up)
		- В всплывающем окне ввести валидный Логин (10 символов) и валидный Пароль.
		- Нажать кнопку подтверждения

		----

		Expected:
			Новый пользователь зарегистрирован

		Неявные проверки:

		- Появляется всплывающее окно с полями для ввода логина и пароля
		- Регистрация нового пользователя

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param sign_up_login_10_password: фикстура - генератор логина и пароля
		:return: OK - если регистрация прошла успешно
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_btn_sign_up()
		chrome.enter_login(sign_up_login_10_password['Login'])
		chrome.enter_password(sign_up_login_10_password['Password'])
		chrome.click_btn_continue()
		chrome.find_my_avatar()
		check_for_missing_elem('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_logout_02(self, chrome_browser):
		""" Сделать Log out.

		- Log out
		- Проверка успешного выхода из аккаунта

		----

		Expected: Log out успешно выполнен

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если  log out успешно выполнен
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_on_my_avatar()
		chrome.click_log_out()
		check_field_name(chrome.find_btn_sign_in(), 'Sign in')

	def test_sign_up_03(self, chrome_browser, sign_up_login_20_password):
		""" Зарегистрировать нового пользователя Login 20 символов.

		- Открыть главную страницу Toci
		- Нажать на кнопку регистрации (Sign up)
		- В всплывающем окне ввести валидный Логин (3 символа) и валидный Пароль.
		- Нажать кнопку подтверждения

		----

		Expected:
			Новый пользователь зарегистрирован

		Неявные проверки:

		- Появляется всплывающее окно с полями для ввода логина и пароля
		- Регистрация нового пользователя

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param sign_up_login_20_password: фикстура - генератор логина и пароля
		:return: OK - если регистрация прошла успешно
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_btn_sign_up()
		chrome.enter_login(sign_up_login_20_password['Login'])
		chrome.enter_password(sign_up_login_20_password['Password'])
		chrome.click_btn_continue()
		chrome.find_my_avatar()
		check_for_missing_elem('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_logout_03(self, chrome_browser):
		""" Сделать Log out.

		- Log out
		- Проверка успешного выхода из аккаунта

		----

		Expected: Log out успешно выполнен

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если  log out успешно выполнен
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_on_my_avatar()
		chrome.click_log_out()
		check_field_name(chrome.find_btn_sign_in(), 'Sign in')
