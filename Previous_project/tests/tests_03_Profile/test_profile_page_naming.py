""" Тестирование наименований страницы профиля.
User story -
"""

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name


class TestProfilePage:
	""" Тесты на соответствие наименований элементов на странице профиля.
	"""

	def test_elem_profile_01(self, chrome_browser):
		""" Кнопка 'profile see more info'.

		- Открыть главную страницу
		- Открыть страницу чужого профиля
		- Проверить текст в элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)
		
		chrome.go_to_site('/profile/4jR9vM2NFAQ')
		check_field_name(chrome.find_profile_see_more_info(), 'See more information')

	def test_elem_profile_02(self, chrome_browser, valid_cookie_new_user):
		""" Шапка страницы редактирования: редактирования профиля.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в шапке страницы

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.make_add_cookies(valid_cookie_new_user)
		chrome.click_on_my_avatar()
		chrome.click_edit()
		check_field_name(chrome.find_edit_profile_title(), 'Edit profile/ Anonymous')

	def test_elem_profile_03(self, chrome_browser):
		""" Вкладка редактирования профиля: Настройки аккаунта.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке перехода на вкладку

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.click_on_my_avatar()
		chrome.click_edit()
		chrome.click_profile_account_settings()
		check_field_name(chrome.find_profile_account_settings(), 'Account settings')

	def test_elem_profile_04(self, chrome_browser):
		""" Шапка страницы редактирования: Настройки аккаунта.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Перейти на вкладку "настройки аккаунта"
		- Проверить текст в шапке страницы

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		chrome.click_profile_account_settings()
		check_field_name(chrome.find_profile_account_settings_title(), 'Account settings')

	def test_elem_profile_05(self, chrome_browser):
		""" Вкладка редактирования профиля: Безопасность.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке перехода на вкладку

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_profile_security(), 'Security')

	def test_elem_profile_06(self, chrome_browser):
		""" Шапка страницы редактирования: Безопасность.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Перейти на вкладку "безопасность"
		- Проверить текст в шапке страницы

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		chrome.click_profile_security()
		check_field_name(chrome.find_profile_security_title(), 'Security')

	def test_elem_profile_07(self, chrome_browser):
		""" Вкладка редактирования профиля: Приватность.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке перехода на вкладку

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_profile_privacy(), 'Privacy')

	def test_elem_profile_08(self, chrome_browser):
		""" Шапка страницы редактирования: Приватность.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Перейти на вкладку "приватность"
		- Проверить текст в шапке страницы

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		chrome.click_profile_privacy()
		check_field_name(chrome.find_profile_privacy_title(), 'Privacy')

	def test_elem_profile_09(self, chrome_browser):
		""" Вкладка редактирования профиля: Уведомления.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке перехода на вкладку

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_profile_notification(), 'Notification')

	def test_elem_profile_10(self, chrome_browser):
		""" Шапка страницы редактирования: Уведомления.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Перейти на вкладку "Уведомленияа"
		- Проверить текст в шапке страницы

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		chrome.click_profile_notification()
		check_field_name(chrome.find_profile_notification_title(), 'Notification')

	def test_elem_profile_11(self, chrome_browser):
		""" Вкладка редактирования профиля: Действия.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке перехода на вкладку

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_profile_actions(), 'Actions')

	def test_elem_profile_12(self, chrome_browser):
		""" Шапка страницы редактирования: Действия.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Перейти на вкладку "Действия"
		- Проверить текст в шапке страницы

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		chrome.click_profile_actions()
		check_field_name(chrome.find_profile_actions_title(), 'Actions')

	def test_elem_profile_13(self, chrome_browser):
		""" Вкладка редактирования профиля: Статистика.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке перехода на вкладку

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_profile_statistics(), 'Statistics')

	def test_elem_profile_14(self, chrome_browser):
		""" Кнопка save changes.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке "save changes"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_profile_btn_save_changes(), 'Save changes')

	def test_elem_profile_15(self, chrome_browser):
		""" Кнопка reset.

		- Открыть главную страницу
		- Открыть свою страницу профиля
		- Нажать кнопку "редактировать профилья"
		- Проверить текст в кнопке "Reset"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site('/profile-edit/')
		check_field_name(chrome.find_btn_reset(), 'Reset')

	def test_delete_all_cookies(self, chrome_browser):
		""" Удалить использованные в этом классе куки.

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если использованные в этом классе куки удалены
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome_browser.delete_all_cookies()
