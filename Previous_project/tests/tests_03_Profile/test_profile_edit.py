""" Редактирование страницы профиля
User story -
Docs -
"""

from framework.BrowsersHelper import Chrome
from framework.check import check_elem_is_disable, check_elem_is_enable, \
    check_elements_texts_fields_are_empty, check_for_missing_elem, check_field_name


class TestProfilePage:
    """ Edit Profile.
    """

    def test_profile_edit_01(self, chrome_browser, valid_cookie_new_user):
        """ Редактирование профиля: Кнопка "Save changes" без введенных данных не активна.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Нажать на кнопку "Save Changes"

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_on_my_avatar()
        chrome.click_edit()
        check_elem_is_disable(chrome.find_profile_btn_save_changes())

    def test_profile_edit_02(self, chrome_browser):
        """ Редактирование профиля: Кнопка "Save changes" становится активной при вводе данных.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Нажать на кнопку "Save Changes"

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.write_profile_full_name()
        check_elem_is_enable(chrome.find_profile_btn_save_changes())

    def test_profile_edit_03(self, chrome_browser):
        """ Редактирование профиля: Кнопка "Reset" возвращает странице последний сохраненный вид.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Вписать Имя
        - Вписать профессию
        _ вписать место работы
        - Вписать образование
        - Вписать город
        - Выбрать Английский язык
        - Нажать кнопку Reset

        ----

        Expected:
            после нажатия на Reset все поля с данными становятся пустыми


        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.write_profile_full_name()
        chrome.write_profile_profession()
        chrome.write_profile_place_of_work()
        chrome.write_profile_education()
        chrome.make_profile_choose_language_en()
        chrome.click_btn_reset()
        field_name, field_profession, field_place_of_work, field_education, field_language, btn_save_changes = \
            chrome.find_profile_field_full_name(), \
            chrome.find_profile_field_profession(), \
            chrome.find_profile_field_place_of_work(), \
            chrome.find_profile_field_education(), \
            chrome.find_profile_edit_language(), \
            chrome.find_profile_btn_save_changes()
        check_elements_texts_fields_are_empty(field_name, field_profession, field_place_of_work,
                                              field_education)
        check_field_name(field_language, 'English')
        check_elem_is_disable(btn_save_changes)

    def test_profile_edit_04(self, chrome_browser):
        """ Редактирование профиля: Сохранить введенные данные кнопкой "Save changes".

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Нажать на кнопку "Save Changes"

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.write_profile_full_name()
        chrome.click_profile_save_changes()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_profile_edit_05(self, chrome_browser):
        """ Редактирование профиля: Загрузить новую аватарку.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Загрузить новую аватарку
        - Сохранить

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.make_upload_image_on_avatar()
        chrome.click_btn_save_new_image()
        chrome.find_new_notification_popup()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_profile_edit_06(self, chrome_browser):
        """ Редактирование профиля: Удалить загруженную аватарку.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Загрузить новую аватарку
        - Сохранить

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.click_profile_delete_avatar()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_profile_edit_07(self, chrome_browser):  # fixme Заставить ждать ответ
        """ Редактирование профиля: Загрузить новую аватарку ~1mb.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Загрузить новую аватарку
        - Сохранить

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.make_upload_image_on_avatar_1mb()
        chrome.click_btn_save_new_image()
        check_for_missing_elem('NotificationPopup_notification__1TRf9.animating-enter-done', chrome)

    def test_profile_edit_08(self, chrome_browser):  # fixme Заставить ждать ответ
        """ Редактирование профиля: Загрузить новую аватарку ~10mb.

        - Зарегистрированным пользователем открыть страницу редактирпования профиля
        - Загрузить новую аватарку
        - Сохранить

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.click_on_my_avatar()
        chrome.click_edit()
        chrome.make_upload_image_on_avatar_10mb()
        chrome.click_btn_save_new_image()
        check_for_missing_elem('NotificationPopup_notification__1TRf9.animating-enter-done', chrome)

    def test_delete_all_cookies(self, chrome_browser):
        """ Удалить использованные в этом классе куки.

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если использованные в этом классе куки удалены
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome_browser.delete_all_cookies()
