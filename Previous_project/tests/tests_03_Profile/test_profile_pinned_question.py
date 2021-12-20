""" Pin & Unpin элемент на странице профиля.
User story -
Docs -
"""
import time

from framework.BrowsersHelper import Chrome
from framework.check import check_for_missing_elem, check_text_field_name, check_element_text_is_on_page, \
	check_string_is_on_page


class TestPinnedQuestion:
	""" Отображение Pin & Unpin Question в профиле.
	"""

	def test_profile_pin_question(self, chrome_browser, create_valid_question_id, valid_cookie_new_user):
		""" Закрепить вопрос.

		- Нажать *** и закрепить публикацию, по средством "Pin".
		- Зайти в профиль для проверки закрепленных публикаций.

		----

		Expected:
			Публикация закреплена на странице профиля в разделе "Pinned"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
		:param valid_cookie_new_user: Куки нового юзера
		:return: OK - если вопрос удачно закреплен на странице профиля
		"""

		chrome = Chrome(chrome_browser)
		
		chrome.go_to_site(f'/question/{create_valid_question_id}')
		question_title = chrome.find_question_page_title().text
		chrome.make_add_cookies(valid_cookie_new_user)
		chrome.click_btn_icon_more1()
		chrome.click_menu_pin_post()
		chrome_browser.refresh()
		chrome.go_to_site('/profile/')
		chrome.find_profile_first_pinned_card()
		check_text_field_name(f'{question_title}\nAnonymous\nquestion', chrome.find_profile_first_pinned_card().text)

	def test_profile_unpin_and_restore_question(self, chrome_browser):
		""" Открепить и воосстановить вопрос в течении 5 секунд.

		- Открепить публикацию
		- Подождпть 5 секунд
		- Восстановить публикацию кнопкой "Restore"
		- Проверить, что публикация осталась закрепленной на странице профиля

		----

		Expected:
			Публикация не откреплена со страницы профиля

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если вопрос остался закрепелнным на страницы профиля
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.go_to_site('/profile/')
		chrome.click_profile_unpin_first_postcard()
		time.sleep(5)
		chrome.click_profile_restore_unpinned_first_postcard()
		check_string_is_on_page('PinnedCard_card__3EryD', chrome)

	def test_profile_unpin_question(self, chrome_browser):
		""" Открепить вопрос за 11 сек.

		- Открепить публикацию
		- Проверить, что публикация откреплена на странице профиля

		----

		Expected:
			Публикация откреплена со страницы профиля

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если вопрос удачно откреплен со страницы профиля
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.go_to_site('/profile/')
		chrome.click_profile_unpin_first_postcard()
		chrome.staleness_of_element(chrome.find_profile_first_pinned_card(), 11)
		check_for_missing_elem('PinnedCard_card__3EryD', chrome)

	def test_delete_question(self, chrome_browser):
		"""Удаление добавленного вопроса.

		- Открыть главную страницу
		- Открыть страницу Question
		- Нажать на ***
		- Выбрать "Удалить"
		- Подтвердить удаление
		- Перейти на страницу своего профиля
		- Проверить, что Question удален

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если вопрос удалена
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
