""" Создание Article.
User story -
Docs -
"""

import pytest

from framework.BrowsersHelper import Chrome
from framework.check import check_field_name, check_element_is_on_page, \
    check_element_text_is_on_page, check_text_field_name


class TestCreateArticle:
    """ Article.
    """
    
    def test_create_article_01(self, chrome_browser, fake_article_text, valid_cookie_new_user):
        """ Публикация новой статьи.

        - Открыть главную страницу Toci
        - Нажать на "+" (создание поста)
        - Выбрать Article
        - На странице создания статьи вписать Title и Description
        - Нажать кнопку опубликовать
        - В поле ввода для тегов написать тег
        - Нажать опупубликовать
        - Сравнить текст, написанный в эдиторе с опубликованным текстом

        ----

        Expected:
            Опубликованный текст точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param fake_article_text: Текст, вводимый в поле Description
        :param valid_cookie_new_user: Куки нового юзера
        :return: OK - если новая статья опубликована
        """

        chrome = Chrome(chrome_browser)
        
        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.make_pre_steps_for_article_create()
        chrome.write_title()
        chrome.write_description(fake_article_text)
        expected_description_from_editor = chrome.find_all_texts_in_description_blocks()
        chrome.click_btn_dark()
        chrome.write_tag()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_article_page_title_description(), expected_description_from_editor)

    def test_edit_article_01(self, chrome_browser):
        """ Отредактировать статью: Изменить title

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Удалить Вписанный ранее Title
        - Написать новый Title
        - Нажать опубликовать пост
        - Сравнить title, написанный в эдиторе с title на опубликованной статье

        ----

        Expected:
            Опубликованный заголовок точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья отредактирована
        """
        
        chrome = Chrome(chrome_browser)
        
        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_icon_more1()
        chrome.click_edit()
        chrome.make_delete_content_in_title()
        chrome.write_another_title()
        expected_new_title = chrome.find_editors_title_text()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_field_name(chrome.find_article_page_title(), expected_new_title)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на сепаратор')
    def test_edit_article_02(self, chrome_browser):
        """ Отредактировать статью: Добавить separator

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - В поле description вписать ещё текста
        - Добавить несколько элементов "separator"
        - Нажать опубликовать пост
        - Сравнить текст, написанный в эдиторе с опубликованным текстом

        ----

        Expected:
            Опубликованный текст точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья отредактирована
        """

        chrome = Chrome(chrome_browser)
        
        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_icon_more1()
        chrome.click_edit()
        chrome.write_advanced_description_add_separator()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_element_is_on_page('ArticleCard_card__145U7', chrome)

    def test_edit_article_03(self, chrome_browser):
        """ Отредактировать статью: ctrl+z

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Кликнуть мышью в поле description
        - Нажать Ctrl+a
        - Нажать Delete
        - Нажать Ctrl+z
        - Опубликовать
        - Сравнить текст, написанный в эдиторе с опубликованным текстом
        ----

        Expected:
            Опубликованный текст точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья отредактирована
        """
        
        chrome = Chrome(chrome_browser)
        
        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_icon_more1()
        chrome.click_edit()
        expected_text = chrome.find_all_texts_in_description_blocks()
        chrome.make_delete_content_in_description()
        chrome.ctrl_z()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_article_page_title_description(), expected_text)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на кнопку изображеня')
    def test_edit_article_04(self, chrome_browser):
        """ Редактирование статьи, с добавлением изображения.

        - Открыть главную страницу Toci
        - Открыть страницу своего поста
        - Нажать ***
        - В меню выбрать пункт "Редактировать"
        - Создать пустую строку, для того, что бы отобразился toolbar
        - Загрузить .gif через блок "Images"
        - Опубликовать
        - Сравнить текст, написанный в эдиторе с опубликованным текстом
        ----

        Expected:
            Опубликованный текст точно такой же, каким пользователь видел его в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если статья отредактирована
        """
        
        chrome = Chrome(chrome_browser)
        
        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_icon_more1()
        chrome.click_edit()
        expected_text = chrome.find_all_texts_in_description_blocks()
        chrome.make_upload_image_in_editor()
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_article_page_title_description(), expected_text)

    @pytest.mark.skip(reason='Придумать стабильный локатор на "+" и на кнопку формулы')
    def test_edit_article_05(self, chrome_browser, my_formula):
        """ Редактирование статьи, с добавлением формулы.

        - Открыть главную страницу
        - Открыть страницу Article
        - Нажать на ***
        - Выбрать "редактирование"
        - Добавить формулу через "+"
        - Опубликовать пост
        - Опубликовать пост
        - Проверить, что вид опубликованной формулы не отличается от вида в эдиторе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param my_formula: Текст формулы
        :return: OK - если статья отредактирована
        """
        
        chrome = Chrome(chrome_browser)
        
        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.click_btn_icon_more1()
        chrome.click_edit()
        chrome.make_block_function(my_formula)
        exp = chrome.find_editors_text().text
        chrome.click_btn_dark()
        chrome.click_save_and_publish()
        check_text_field_name(chrome.find_post_article_page_title_description(), exp)

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
