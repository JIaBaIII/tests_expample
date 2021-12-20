""" Авторизация.
User story -
Docs - https://www.notion.so/hipasus/1709ee951ef74149ae3bbd19344d6f2b
"""
from framework.BrowsersHelper import Chrome
from framework.check import check_for_missing_elem


class TestSignIn:
	""" Авторизация.
	"""

	def test_sign_in_01(self, chrome_browser, signed_up_user_for_sign_in):
		""" Авторизация уже зарегистрированного пользователя.

		Предшаги:

		- Зарегистрировать пользователя (В тесте это делает фикстура signed_up_user_for_sign_in)

		----

		- Открыть главную страницу TOCI
		- Нажать на кнопку "Sign_in"
		- Ввести валидный Login
		- Ввести валидный Password
		- Нажать кнопку подтверждения авторизации

		----

		Expected:
			Авторизация прошла успешно

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param signed_up_user_for_sign_in: Специально зареганный юзер, для проверки Sign in
		:return: OK - если авторизация прошла успешно
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_btn_sign_in()
		chrome.enter_login(signed_up_user_for_sign_in['Login'])
		chrome.enter_password(signed_up_user_for_sign_in['Password'])
		chrome.click_btn_red()
		chrome.find_my_avatar()
		check_for_missing_elem('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_delete_all_cookies(self, chrome_browser):
		""" Удалить использованные в этом классе куки.

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если использованные в этом классе куки удалены
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome_browser.delete_all_cookies()
