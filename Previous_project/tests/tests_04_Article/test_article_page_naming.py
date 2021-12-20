""" Тестипование наименований элементов.
User story -
"""

from selenium.webdriver import ActionChains

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_text_field_name


class TestArticlePage:
	""" Article page - Тесты на соответствие наименований элементов.
	"""

	def test_elem_article_page_01(self, chrome_browser, create_another_valid_article_id, valid_cookie_new_user):
		""" Кнопка "Follow" в тултипе.

		- Открыть страницу Article
		- Навести курсор мышки на аватарку автора для вызова тултипа
		- Найти в тултипе кнопку "подписаться"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_another_valid_article_id:
		:param valid_cookie_new_user: Куки нового юзера
		:return: OK - если на кнопке подписаться в тултипе написано "Follow"
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.make_add_cookies(valid_cookie_new_user)
		chrome.go_to_site(f'/article/{create_another_valid_article_id}')
		ActionChains(chrome_browser).move_to_element(chrome.find_author_avatar()).perform()
		ActionChains(chrome_browser).move_to_element(chrome.find_author_avatar()).perform()
		check_field_name(chrome.find_tooltip_btn_follow(), 'Follow')

	def test_elem_article_page_02(self, chrome_browser, create_valid_article_id):
		""" Кнопка "Comments".

		- Открыть страницу Article
		- Сравнить текст на элементе "комментарии"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на кнопке комментарии написано 'Comments'
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		check_field_name(chrome.find_comments_btn(), '0 comments')

	def test_elem_article_page_03(self, chrome_browser, create_valid_article_id):
		""" Тип созданной статьи.

		- Открыть страницу Article
		- Сравнить текст на элементе "Статья"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если тип созданной статьи 'Article'
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		check_field_name(chrome.find_content_authors_topic(), 'article')

	def test_delete_created_article(self, chrome_browser, delete_article_id_by_moder, delete_another_article_id_by_moder):
		""" Удаление статьи модератором.

		- Открыть главную страницу
		- Удалить статью мадератором
		- Проверить отсутствие статьи на платформе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param delete_article_id_by_moder: Фикстура для удаления статьи модератором
		:param delete_another_article_id_by_moder: Фикстура для удаления другой статьи модератором
		:return: OK - если статьи удалены модератором
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		check_text_field_name(delete_article_id_by_moder, 'REMOVED_BY_MODERATOR')
		check_text_field_name(delete_another_article_id_by_moder, 'REMOVED_BY_MODERATOR')

	def test_delete_all_cookies(self, chrome_browser):
		""" Удалить использованные в этом классе куки.

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если использованные в этом классе куки удалены
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome_browser.delete_all_cookies()
