""" Pin & Unpin элемент на странице профиля.
User story -
Docs -
"""
import time

from framework.BrowsersHelper import Chrome
from framework.check import check_for_missing_elem, check_text_field_name, check_element_text_is_on_page, \
	check_string_is_on_page


class TestPinnedArticle:
	""" Отображение Pin & Unpin Article в профиле.
	"""

	def test_profile_pin_article(self, chrome_browser, create_valid_article_id, valid_cookie_new_user):
		""" Закрепить статью.

		- Нажать *** и закрепить публикацию, по средством "Pin".
		- Зайти в профиль для проверки закрепленных публикаций.

		----

		Expected:
			Публикация закреплена на странице профиля в разделе "Pinned"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:param valid_cookie_new_user: Куки нового юзера
		:return: OK - если статья удачно закреплена на странице профиля
		"""

		chrome = Chrome(chrome_browser)
		
		chrome.go_to_site(f'/article/{create_valid_article_id}')
		article_title = chrome.find_article_page_title().text
		chrome.make_add_cookies(valid_cookie_new_user)
		chrome.click_btn_icon_more1()
		chrome.click_menu_pin_post()
		chrome_browser.refresh()
		chrome.go_to_site('/profile/')
		check_text_field_name(f'{article_title}\nAnonymous\narticle', chrome.find_profile_first_pinned_card().text)

	def test_profile_unpin_and_restore_article(self, chrome_browser):
		""" Открепить и воосстановить статью в течении 5 секунд.

		- Открепить публикацию
		- Подождпть 5 секунд
		- Восстановить публикацию кнопкой "Restore"
		- Проверить, что публикация осталась закрепленной на странице профиля

		----

		Expected:
			Публикация не откреплена со страницы профиля

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если статья осталась закрепелнной на страницы профиля
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.go_to_site('/profile/')
		chrome.click_profile_unpin_first_postcard()
		time.sleep(5)
		chrome.click_profile_restore_unpinned_first_postcard()
		check_string_is_on_page('PinnedCard_card__3EryD', chrome)

	def test_profile_unpin_article(self, chrome_browser):
		""" Открепить статью за 11 сек.

		- Открепить публикацию
		- Проверить, что публикация откреплена на странице профиля

		----

		Expected:
			Публикация откреплена со страницы профиля

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если статья удачно откреплена со страницы профиля
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.go_to_site('/profile/')
		chrome.click_profile_unpin_first_postcard()
		chrome.staleness_of_element(chrome.find_profile_first_pinned_card(), 11)
		check_for_missing_elem('PinnedCard_card__3EryD', chrome)

	def test_delete_article(self, chrome_browser):
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

		chrome.go_to_site()
		chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
		chrome.click_btn_icon_more1()
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
