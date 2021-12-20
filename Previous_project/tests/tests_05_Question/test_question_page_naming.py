""" Тестирование наименований страницы вопроса.
User story -
"""
import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_element_text_is_on_page, check_expected_text_is_in_element


class TestQuestionPage:
	""" Тесты на соответствие наименований элементов на странице Question.
	"""

	def test_elem_question_page_01(self, chrome_browser, create_valid_question_id):
		""" Кнопка "Answer".

		- Открыть страницу вопроса
		- Проверить текст на кнопке "ответ"

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_valid_question_id}')
		check_field_name(chrome.find_btn_answer_by_unsigned_user(), 'Write answer')

	@pytest.mark.skip(reason='ждёт баг-фикса')
	def test_elem_question_page_02(self, chrome_browser, create_valid_question_id):
		""" Тип созданного вопроса.

		- Открыть страницу вопроса
		- Проверить текст на типе поста

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
		:return: OK - если текст соответствует
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site(f'/question/{create_valid_question_id}')
		check_expected_text_is_in_element(chrome.find_question_card_name(), 'question')

	def test_delete_created_posts(self, chrome_browser, valid_cookie_new_user, create_valid_question_id):
		""" Удаление созданного вопроса.

		- Открыть страницу вопроса
		- Удалить вопрос
		- Открыть страницу профиля
		- Проверить, что вопрос удален

		:param chrome_browser: Браузер, на котором делаем автотесты
		:param valid_cookie_new_user: Куки нового юзера
		:param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
		:return: OK - если вопрос удален
		"""

		chrome = Chrome(chrome_browser)

		chrome.go_to_site()
		chrome.make_add_cookies(valid_cookie_new_user)
		chrome.go_to_site(f'/question/{create_valid_question_id}')
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
