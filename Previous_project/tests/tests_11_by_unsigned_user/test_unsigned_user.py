""" Взаимодействие с TOCI незарегистрированным пользователем.
User story -
"""
import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_element_text_is_on_page, check_string_is_on_page


class TestUnsignedUser:
	""" Взаимодействие с TOCI незарегистрированным пользователем.
	"""

	def test_popup_unsigned_user_01(self, chrome_browser, create_valid_article_id):
		""" Попап регистрации, кликая кнопку 'Save'.

		- Открыть главную страницу
		- Нажать на кнопку "сохранить Article"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.click_on_feed()
		chrome.find_btn_sign_up()
		chrome.click_feed_save_article_btn()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_02(self, chrome_browser, create_valid_article_id):
		""" Попап регистрации, кликая кнопку 'Save' в статье внизу.

		- Открыть страницу Article
		- Нажать на кнопку "сохранить Article" (внизу)

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.click_article_page_save_btn_below()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	@pytest.mark.skip(reason="Ждать багфикс по кнопке Save")
	def test_popup_unsigned_user_03(self, chrome_browser, create_valid_article_id):
		""" Попап регистрации, клиая кнопку 'Save' в статье.

		- Открыть страницу Article
		- Нажать на кнопку "сохранить Article"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.click_article_page_save_btn()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	@pytest.mark.skip(reason="Ждать багфикс по кнопке Save")
	def test_popup_unsigned_user_04(self, chrome_browser, create_valid_article_id):
		""" Попап регистрации, кликая кнопку 'Save' в чужом профиле.

		- Открыть страницу чужого Article
		- Перейти на страницу чужого профиля
		- Нажать на кнопку "Сохранить Article"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.click_on_authors_name()
		chrome.click_profile_save_article_btn()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_05(self, chrome_browser, create_valid_article_id):
		""" Попап регистрации, кликая "Пожаловаться на Article".

		- Открыть страницу Article
		- Нажать на ***
		- Выбрать "Пожаловаться"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.click_btn_icon_more1()
		chrome.click_complain()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_06(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая кнопку 'Answer' на вопросе.

		- Открыть страницу вопроса
		- Нажать на кнопку "ответ"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_answer()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_07(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая кнопку 'Follow' на вопросе.

		- Открыть страницу вопроса
		- Нажать на кнопку "подписаться"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_follow_question_unsigned_user()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_08(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "Пожаловаться на вопрос".

		- Открыть страницу вопроса
		- Нажать на ***
		- Выбрать "пожаловаться"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_btn_icon_more1()
		chrome.click_complain()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_09(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "UpVote Answer" со страницы Question.

		- Открыть страницу вопроса с ответом
		- Нажать на кнопку "Upvote" на ответе

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_upvote_answer_from_question_page()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_10(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "DownVote Answer" со страницы Question.

		- Открыть страницу вопроса с ответом
		- На ответе нажать на ***
		- Выбрать "DownVote"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_btn_more_answer()
		chrome.click_menu_item_dont_like()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)
		
	def test_popup_unsigned_user_11(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "Пожаловаться на ответ" со страницы Question.

		- Открыть страницу вопроса с ответом
		- Нажать на ***
		- Выбрать "пожаловаться на ответ"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_btn_more_answer()
		chrome.click_menu_item_complain()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_12(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "UpVote" со страницы Answer.

		- Открыть страницу вопроса с ответом
		- Перейти на страницу ответа
		- Нажать на кнопку "Upvote" 

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_to_open_answers_page()
		chrome.click_upvote_from_answer_page()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_13(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "DownVote" со страницы Answer.

		- Открыть страницу вопроса с ответом
		- Перейти на страницу ответа
		- На ответе нажать на ***
		- Выбрать "DownVote"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_to_open_answers_page()
		chrome.click_btn_menu_answer()
		chrome.click_menu_item_dont_like()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_14(self, chrome_browser, create_question_with_answer):
		""" Попап регистрации, кликая "Пожаловаться на ответ" со страницы Answer.

		- Открыть страницу вопроса с ответом
		- Перейти на страницу ответа
		- Нажать на ***
		- Выбрать "пожаловаться"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_question_with_answer}')
		chrome.click_to_open_answers_page()
		chrome.click_btn_menu_answer()
		chrome.click_menu_item_complain()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_15(self, chrome_browser, create_valid_article_id):
		""" Попап регистрации, кликая "Подписаться на автора" на его странице Article (Author's block).

		- Открыть страницу Article
		- Нажать на кнопку "подписаться на автора"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_article_id}')
		chrome.click_btn_follow_author_in_article()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_16(self, chrome_browser, create_valid_comment_on_article_id):
		""" Попап регистрации, кликая "Пожаловаться на комментарий 1 ур" со страницы Article.

		- Открыть страницу статьи
		- Открыть комментарии
		- Нажать на ***
		- Выбрать "пожаловаться"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_comment_on_article_id: Фикстура, создающая статью, ответом и комментом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_comment_on_article_id}')
		chrome.click_btn_comments()
		chrome.click_btn_menu_comment()
		chrome.click_menu_btn_complain()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_17(self, chrome_browser, create_valid_comment_on_article_id):
		""" Попап регистрации, кликая "Upvote на комментарий 1 ур" со страницы Article.

		- Открыть страницу статьи
		- Открыть комментарии
		- Нажать Upvote

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_comment_on_article_id: Фикстура, создающая статью, ответом и комментом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/article/{create_valid_comment_on_article_id}')
		chrome.click_btn_comments()
		chrome.click_upvote_first_comment_lvl_1()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_18(self, chrome_browser, create_valid_comment_on_answer_id, create_valid_question_id):
		""" Попап регистрации, кликая "Пожаловаться на комментарий 1 ур" со страницы Answer.

		- Открыть страницу статьи
		- Открыть комментарии
		- Нажать на ***
		- Выбрать "пожаловаться"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_comment_on_answer_id: Фикстура, создающая статью, ответом и комментом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_valid_question_id}/{create_valid_comment_on_answer_id}')
		chrome.click_btn_comments_answer_page()
		chrome.click_btn_menu_comment()
		chrome.click_menu_btn_complain()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_popup_unsigned_user_19(self, chrome_browser, create_valid_comment_on_answer_id, create_valid_question_id):
		""" Попап регистрации, кликая "Upvote на комментарий 1 ур" со страницы Answer.

		- Открыть страницу статьи
		- Открыть комментарии
		- Нажать Upvote

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_comment_on_answer_id: Фикстура, создающая статью, ответом и комментом на бэке
		:return: OK - если на совершаемое действие незарегистрированный юзер видит попап авторизации
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_valid_question_id}/{create_valid_comment_on_answer_id}')
		chrome.click_btn_comments_answer_page()
		chrome.click_upvote_first_comment_lvl_1()
		check_string_is_on_page('AuthorizationPopup_wrapper__2lQQs', chrome)

	def test_delete_created_posts(
			self, chrome_browser, valid_cookie_new_user, create_valid_article_id, create_question_with_answer):
		""" Удаление созданных выше постов.

		- Открыть главную страницу
		- Открыть страницу Article
		- Нажать на ***
		- Выбрать "Удалить"
		- Открыть главную страницу
		- Открыть страницу Question
		- Нажать на ***
		- Выбрать "Удалить"
		- Перейти на страницу своего профиля
		- Проверить отсутствие статьи и вопроса

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param valid_cookie_new_user: Куки нового юзера
		:param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
		:param create_question_with_answer: Фикстура, создающая вопрос с ответом на бэке
		:return: OK - если созданные статья и вопрос в этом классе удалены
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
