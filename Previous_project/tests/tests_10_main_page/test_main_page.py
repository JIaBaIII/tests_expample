""" Тестипование наименований главной страницы TOCI.
User story -
"""
from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_expected_text_is_in_element, \
	check_element_text_is_on_page


class TestMainPage:
	""" Тесты на соответствие наименований элементов на главной странице.
	"""

	# def test_elem_chrome_01(self, chrome_browser):
	# 	""" Кнопка "TOCI".
	#
	# 	- Открыть главную страницу
	# 	- Найти хеддер "ТОСИ"
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_header_toci(), 'TOCI')  # Логотип ТОСИ

	def test_elem_chrome_02(self, chrome_browser):
		""" Кнопка "Sign up".

		- Открыть главную страницу
		- Найти кнопку "зарегистрироваться"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		check_field_name(chrome.find_btn_sign_up(), 'Sign up')

	def test_elem_chrome_03(self, chrome_browser):
		""" Кнопка "Sign in".

		- Открыть главную страницу
		- Найти кнопку "авторизоваться"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		check_field_name(chrome.find_btn_sign_in(), 'Sign in')

	def test_elem_chrome_04(self, chrome_browser):
		""" Вкладка рекомендаций.

		- Открыть главную страницу
		- Найти вкладку "рекомендации"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		check_field_name(chrome.find_header_recommendations(), 'Interesting')

	def test_elem_chrome_05(self, chrome_browser):
		""" Вкладка топики.

		- Открыть главную страницу
		- Найти вкладку "топики"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		check_field_name(chrome.find_header_topics(), 'Topics')

	def test_elem_chrome_06(self, chrome_browser):
		""" Вкладка "Feed".

		- Открыть главную страницу
		- Найти вкладку "лента"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		check_field_name(chrome.find_header_feed(), 'Feed')

	# def test_elem_chrome_07(self, chrome_browser):
	# 	""" Блок с предложенным контентом 'Top of the week'.
	#
	# 	- Открыть главную страницу
	# 	- Найти блок "You may be interested"
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	#
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_what_may_be_interested(), 'Top of the week')  # Блок с топами недели

	def test_elem_chrome_08(self, chrome_browser, create_question_with_answer):
		""" Кнопка "Answers" на карточке Question.

		- Открыть главную страницу
		- Открыть страницу вопроса
		- Найти кнопку  "ответы"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_on_feed()
		check_expected_text_is_in_element(chrome.find_on_feed_count_answers(), 'answers')

	def test_elem_chrome_09(self, chrome_browser, create_valid_question_id):
		""" Карточка вопроса, с типом поста 'question'.

		- Открыть главную страницу
		- Открыть страницу вопроса
		- Найти тип "поста"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_valid_question_id}')
		chrome.click_on_feed()
		check_field_name(chrome.find_content_authors_topic(), 'question')

	def test_elem_chrome_10(self, chrome_browser, create_valid_article_id):
		""" Карточка статьи, с типом поста 'article'.

		- Открыть главную страницу
		- Открыть страницу статьи
		- Найти тип "поста"
		- Сравнить текст на элементе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.go_to_site()
		check_expected_text_is_in_element(chrome.find_content_authors_topic(), 'article')

	# def test_elem_chrome_11(self, chrome_browser):
	# 	""" Сайдбар: вкладка 'My questions'.
	#
	# 	- Открыть главную страницу
	# 	- Открыть сайдбар
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	#
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_feed_sidebar_my_questions(), 'My questions')
	#
	# def test_elem_chrome_12(self, chrome_browser):
	# 	""" Сайдбар: вкладка 'Quotes'.
	#
	# 	- Открыть главную страницу
	# 	- Открыть сайдбар
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	#
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_feed_sidebar_quotes(), 'Quotes')
	#
	# def test_elem_chrome_13(self, chrome_browser):
	# 	""" Сайдбар: вкладка 'Recent'.
	#
	# 	- Открыть главную страницу
	# 	- Открыть сайдбар
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	#
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_feed_sidebar_resent(), 'Recent')
	#
	# def test_elem_chrome_14(self, chrome_browser):
	# 	""" Сайдбар: вкладка 'Trash'.
	#
	# 	- Открыть главную страницу
	# 	- Открыть сайдбар
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	#
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_feed_sidebar_trash(), 'Trash')
	#
	# def test_elem_chrome_15(self, chrome_browser):
	# 	""" Сайдбар: вкладка 'Settings'.
	#
	# 	- Открыть главную страницу
	# 	- Открыть сайдбар
	# 	- Сравнить текст на элементе
	#
	# 	:param chrome_browser: Браузер, на котором делаем автотесты
	# 	:return: OK - если текст соответствует
	# 	"""
	#
	# 	chrome = Chrome(chrome_browser)
	#
	# 	chrome.go_to_site()
	# 	check_field_name(chrome.find_feed_sidebar_settings(), 'Settings')  # Сайдбар

	def test_delete_created_posts(
			self, chrome_browser, valid_cookie_new_user, create_valid_article_id, create_question_with_answer):
		""" Удаление созданных постов.

		- Открыть главную страницу
		- Открыть созданную ранее статью
		- Удалить статью
		- Открыть станицу вопроса
		- Удалить вопрос
		- Открыть страницу профиля
		- Проверить отсутствие статьи и вопроса на странице профиля автора

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param valid_cookie_new_user: Куки нового юзера
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке

		:return: OK - статья и вопрос удалены
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.make_add_cookies(valid_cookie_new_user)
		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.make_click_delete_article()
		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.make_click_delete_question()
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
