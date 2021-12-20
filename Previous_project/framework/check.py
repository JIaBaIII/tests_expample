import time

from hamcrest import *


def check_field_name(element, expected_text):
	time.sleep(0.005)
	assert_that(element.text, equal_to(expected_text))


def check_text_field_name(elem_text, expected_text):
	time.sleep(0.005)
	assert_that(elem_text, equal_to(expected_text))


def check_expected_text_is_in_element(element, expected_text):
	time.sleep(0.005)
	assert_that(expected_text, is_in(element.text))


def check_element_text_is_on_page(elem, expected_element):
	time.sleep(0.005)
	page_source = expected_element.driver.page_source
	assert_that(elem.text, is_in(page_source))


def check_element_is_on_page(elem, expected_element):
	time.sleep(0.005)
	page_source = expected_element.driver.page_source
	assert_that(elem, is_in(page_source))


def check_string_is_on_page(elem, expected_element):
	time.sleep(0.005)
	page_source = expected_element.driver.page_source
	assert_that(page_source, contains_string(elem))


def check_tag_name(element, expected_text):
	time.sleep(0.005)
	assert_that(element.tag_name, equal_to(expected_text))


def check_elem_is_enable(element):
	time.sleep(0.005)
	assert_that(element.is_enabled(), equal_to(True))


def check_elem_is_disable(element):
	time.sleep(0.005)
	assert_that(element.is_enabled(), equal_to(False))


def check_elements_texts_fields_are_empty(*elements):
	time.sleep(0.005)
	for elem in elements:
		assert_that(elem.get_property("value"), equal_to(''))


def check_for_missing_elem(text, expected_element):
	time.sleep(0.005)
	page_source = expected_element.driver.page_source
	if text in page_source:
		raise AssertionError('Неудача. Элемент присутствует на странице')  # findme придумал такое решение
	else:
		assert text not in page_source
