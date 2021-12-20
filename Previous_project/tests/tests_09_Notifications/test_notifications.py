""" Создание Уведомлений.
User story -
Docs -
"""
import time

import pytest

from framework.BrowsersHelper import Chrome, FireFox
from framework.check import check_elem_is_enable, check_for_missing_elem, check_element_text_is_on_page, \
    check_field_name
from framework.helper import delete_answer_id_by_moder, delete_question_id_by_moder, delete_article_id_by_moder


class TestCreateNotifications:
    """ Notifications.
    """

    def test_notifications_01(self, chrome_browser, firefox_browser, valid_cookie_new_user,
                              valid_id_new_user, valid_id_another_user, valid_cookie_another_user):
        """ Уведомление о подписке на пользователя.

        - Открыть главную страницу Toci
        - Зарегистрироваться
        - Ждать уведомление о подписке на себя

        - В другом браузере зарегистрироваться другом пользователем
        - Перейти на страницу профиля автора
        - Подписаться на пользователя

        ----

        Expected:
            Пользователь 1 получил уведомление о подписке на профиль от пользователя 2

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_id_new_user: id нового бзера
        :param valid_cookie_new_user: Куки нового юзера
        :param valid_cookie_another_user: Куки другого нового юзера
        :return: OK - если пользователь 1 получил уведомление о подписке на профиль от пользователя 2
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        chrome.go_to_site(f'/profile/{valid_id_another_user}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_btn_follow_profile()
        firefox.go_to_site()
        firefox.go_to_site(f'/profile/{valid_id_new_user}')
        firefox.make_add_cookies(valid_cookie_another_user)
        firefox.click_btn_follow_profile()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_02(self, firefox_browser, chrome_browser, valid_cookie_new_user,
                              valid_cookie_another_user, fake_question_text):
        """ Уведомление о публикации нового вопроса от пользователя на которого я подписан.

        - В другом браузере авторизоваться другом пользователем, подписанным на профиль пользователя
        - Ждать уведомление о публикации нового вопроса от пользователя на которого я подписан

        - Открыть главную страницу Toci
        - Авторизоваться
        - Опубликовать Question пользователем 1

        ----

        Expected:
            Пользователь 2 получил уведомление о новом вопросе пользователя 1

        :param firefox_browser: Браузер, используемый, что бы открыть новое окно и зарегистрироовать другого юзера
        :return: OK - если пользователь 2 получил уведомление о новом вопросе пользователя 1
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        firefox.go_to_site()
        firefox.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_another_user)
        chrome.make_pre_steps_for_question_create()
        chrome.write_title()
        chrome.write_description(fake_question_text)
        chrome.click_btn_dark()
        chrome.write_tag()
        chrome.click_save_and_publish()
        check_elem_is_enable(firefox.find_new_notification_popup())

    @pytest.mark.skip(reason='Не приходит уведомление. Пересмотреть тест после нг')
    def test_notifications_03(self, chrome_browser, firefox_browser, valid_cookie_new_user,
                              create_valid_question_id, valid_cookie_another_user):
        """ Уведомление о подписке на вопрос.

        - Открыть главную страницу Toci
        - Зарегистрироваться
        - Опубликовать Question
        - Ждать уведомление о подписке на вопрос

        - В другом браузере зарегистрироваться другом пользователем
        - Перейти на страницу вопроса
        - Подписаться на вопрос

        ----

        Expected:
            Пользователь 1 получил уведомление о подписке на вопрос от пользователя 2

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param firefox_browser: Браузер, используемый, что бы открыть новое окно и зарегистрироовать другого юзера
        :param valid_cookie_new_user: Куки нового юзера
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если пользователь 1 получил уведомление о подписке на вопрос от пользователя 2
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        firefox.go_to_site(f'/question/{create_valid_question_id}')
        firefox.make_add_cookies(valid_cookie_another_user)
        firefox.click_follow_question()
        check_elem_is_enable(chrome.find_new_notification_popup())

    @pytest.mark.skip(reason='Application error на нотификацию об ответе. Пересмотреть тест после нг')
    def test_notifications_04(self, chrome_browser, firefox_browser, valid_cookie_new_user,
                              create_valid_question_id, valid_cookie_another_user, fake_answer_text):
        """ Уведомление о новом ответе на мой вопрос.

        - Открыть главную страницу Toci
        - Зарегистрироваться
        - Опубликовать Question
        - Ждать уведомление о новом ответе на свой вопрос

        - В другом браузере зарегистрироваться другом пользователем
        - Перейти на страницу вопроса
        - Ответить на вопрос

        ----

        Expected:
            Пользователь 1 получил уведомление о новом ответе на вопрос от пользователя 2

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param firefox_browser: Браузер, используемый, что бы открыть новое окно и зарегистрироовать другого юзера
        :param valid_cookie_new_user: Куки нового юзера
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если пользователь 1 получил уведомление о новом ответе на вопрос от пользователя 2
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        firefox.go_to_site(f'/question/{create_valid_question_id}')
        firefox.make_add_cookies(valid_cookie_another_user)
        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.click_answer()
        chrome.write_description(fake_answer_text)
        chrome.click_post_answers_and_post_answer()
        check_elem_is_enable(firefox.find_new_notification_popup())

    @pytest.mark.skip(reason='Application error на нотификацию об ответе. Пересмотреть тест после нг')
    def test_notifications_05(self, chrome_browser, firefox_browser, valid_cookie_third_user,
                              create_valid_question_id, valid_cookie_another_user, fake_answer_text):
        """ Уведомление о новом ответе на вопрос на который я подписан.

        - Открыть главную страницу Toci
        - Зарегистрироваться
        - Найти опубликованный другим пользователем вопрос и подписаться на него
        - Ждать уведомление о новом ответе на вопрос, на который я подписан

        - В другом браузере зарегистрироваться третьим пользователем
        - Перейти на страницу вопроса
        - Ответить на вопрос

        ----

        Expected:
            Пользователь 2 получил уведомление о новом ответе на вопрос от пользователя 3

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param firefox_browser: Браузер, используемый, что бы открыть новое окно и зарегистрироовать другого юзера
        :param valid_cookie_third_user: Куки третьего юзера
        :param create_valid_question_id: Фикстура для поолучения QuestionID, созданного бэком
        :return: OK - если пользователь 2 получил уведомление о новом ответе на вопрос от пользователя 3
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        firefox.go_to_site(f'/question/{create_valid_question_id}')
        firefox.make_add_cookies(valid_cookie_another_user)
        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_third_user)
        chrome.click_answer()
        chrome.write_description(fake_answer_text)
        chrome.click_post_answers_and_post_answer()
        check_elem_is_enable(firefox.find_new_notification_popup())

    @pytest.mark.skip(reason='Не приходит уведомление. Пересмотреть тест после нг')
    def test_notifications_06(self, chrome_browser, firefox_browser, valid_cookie_new_user,
                              create_valid_article_id, valid_cookie_another_user):
        """ Уведомление об Upvote Article.

        - Открыть главную страницу Toci
        - Зарегистрироваться
        - Опубликовать Article
        - Ждать уведомление об Upvote Article

        - В другом браузере зарегистрироваться другом пользователем
        - Перейти на страницу статьи
        - Лайкнуть статью

        ----

        Expected:
            Пользователь 1 получил уведомление о подписке на вопрос от пользователя 2

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param firefox_browser: Браузер, используемый, что бы открыть новое окно и зарегистрироовать другого юзера
        :param valid_cookie_new_user: Куки нового юзера
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :return: OK - если пользователь 1 получил уведомление о подписке на вопрос от пользователя 2
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        firefox.go_to_site(f'/article/{create_valid_article_id}')
        firefox.make_add_cookies(valid_cookie_another_user)
        firefox.click_article_or_question_page_icon_upvote()
        firefox.find_article_or_question_page_upvote_fill()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_07(self, chrome_browser, firefox_browser, valid_cookie_new_user,
                              create_valid_article_id, valid_cookie_another_user):
        """ Отсутствие уведомления о DownVote Article.

        - Открыть главную страницу Toci
        - Зарегистрироваться
        - Опубликовать Article
        - Проверить отсутствие уведомление о Downvote

        - В другом браузере зарегистрироваться другом пользователем
        - Перейти на страницу статьи
        - Downvote статью

        ----

        Expected:
            Пользователь 1 получил уведомление о подписке на вопрос от пользователя 2

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param firefox_browser: Браузер, используемый, что бы открыть новое окно и зарегистрироовать другого юзера
        :param valid_cookie_new_user: Куки нового юзера
        :param create_valid_article_id: Фикстура для поолучения ArticleID, созданного бэком
        :return: OK - если пользователь 1 получил уведомление о подписке на вопрос от пользователя 2
        """

        chrome, firefox = Chrome(chrome_browser), FireFox(firefox_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        firefox.go_to_site(f'/article/{create_valid_article_id}')
        firefox.make_add_cookies(valid_cookie_another_user)
        firefox.click_btn_icon_more1()
        firefox.click_menu_item_dont_like()
        firefox.write_downvote_explanation()
        check_for_missing_elem('NotificationPopup_notification__1TRf9.animating-enter-done', chrome)
        firefox_browser.minimize_window()

    def test_notifications_08(self, chrome_browser, valid_cookie_new_user):
        """ Системные уведомления: сохранение измененной информации в профиле.

        - Зайти в редактирование своего профиля
        - Написать / изменить full name
        - Проверить наличие системного уведомления о сохранении изменений

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile-edit')
        chrome.write_profile_full_name()
        chrome.click_profile_save_changes()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_09(self, chrome_browser, valid_cookie_new_user):
        """ Системные уведомления: сохранение измененной информации в профиле.

        - Зайти в редактирование своего профиля
        - Написать / изменить профессию
        - Проверить наличие системного уведомления о сохранении изменений

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile-edit')
        chrome.write_profile_profession()
        chrome.click_profile_save_changes()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_10(self, chrome_browser, valid_cookie_new_user):
        """ Системные уведомления: сохранение измененной информации в профиле.

        - Зайти в редактирование своего профиля
        - Написать / изменить место работы
        - Проверить наличие системного уведомления о сохранении изменений

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile-edit')
        chrome.write_profile_place_of_work()
        chrome.click_profile_save_changes()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_11(self, chrome_browser, valid_cookie_new_user):
        """ Системные уведомления: сохранение измененной информации в профиле.

        - Зайти в редактирование своего профиля
        - Написать / изменить education
        - Проверить наличие системного уведомления о сохранении изменений

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile-edit')
        chrome.write_profile_education()
        chrome.click_profile_save_changes()
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_12(self, chrome_browser, valid_cookie_new_user):
        """ Системные уведомления: сохранение измененной информации в профиле.

        - Зайти в редактирование своего профиля
        - Написать / изменить язык
        - Проверить наличие системного уведомления о сохранении изменений

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile-edit')
        chrome.make_profile_choose_language_en()
        chrome.click_profile_save_changes()
        check_field_name(chrome.find_profile_edit_language(), 'English')
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_notifications_13(self, chrome_browser, valid_cookie_new_user):
        """ Системные уведомления: сохранение измененной информации в профиле.

        - Зайти в редактирование своего профиля
        - Написать / изменить язык
        - Проверить наличие системного уведомления о сохранении изменений

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param valid_cookie_new_user: Куки нового юзера
        :return:
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site('/profile-edit')
        chrome.make_profile_choose_language_ru()
        chrome.click_profile_save_changes()
        check_field_name(chrome.find_profile_edit_language(), 'Russian')
        check_elem_is_enable(chrome.find_new_notification_popup())

    @pytest.mark.xfail(reason='Пост удаляется модератором, но оповещение может не прийти')
    def test_moder_delete_created_answer(self, chrome_browser,
                                         valid_cookie_new_user, create_valid_question_id, valid_answer,
                                         valid_token_moderator):
        """ Уведомление об удалении ответа модератором.

        - Открыть главную страницу
        - Удалить вопрос мадератором
        - Проверить отсутствие вопроса на платформе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param : Фикстура для удаления статьи модератором
        :param : Фикстура для удаления другой статьи модератором
        :return: OK - если статьи удалены модератором
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}/{valid_answer}')
        chrome.make_add_cookies(valid_cookie_new_user)
        chrome.go_to_site()
        delete_answer_id_by_moder(valid_token_moderator, valid_answer)
        check_elem_is_enable(chrome.find_new_notification_popup())

    @pytest.mark.xfail(reason='Пост удаляется модератором, но оповещения об этом нет')
    def test_moder_delete_created_question(self, chrome_browser, valid_token_moderator,
                                           create_valid_question_id, valid_cookie_new_user):
        """ Уведомление об удалении вопроса модератором.

        - Открыть главную страницу
        - Удалить вопрос мадератором
        - Проверить отсутствие вопроса на платформе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param : Фикстура для удаления статьи модератором
        :param : Фикстура для удаления другой статьи модератором
        :return: OK - если статьи удалены модератором
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/question/{create_valid_question_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        delete_question_id_by_moder(valid_token_moderator, create_valid_question_id)
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_moder_delete_created_article(self, chrome_browser, valid_token_moderator,
                                          create_valid_article_id, valid_cookie_new_user):
        """ Уведомление об удалении статьи модератором.

        - Открыть главную страницу
        - Удалить вопрос мадератором
        - Проверить отсутствие вопроса на платформе

        :param chrome_browser: Браузер, на котором делаем автотесты
        :param : Фикстура для удаления статьи модератором
        :param : Фикстура для удаления другой статьи модератором
        :return: OK - если статьи удалены модератором
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site(f'/article/{create_valid_article_id}')
        chrome.make_add_cookies(valid_cookie_new_user)
        time.sleep(2)
        delete_article_id_by_moder(valid_token_moderator, create_valid_article_id)
        check_elem_is_enable(chrome.find_new_notification_popup())

    def test_delete_question(self, chrome_browser, valid_cookie_another_user):
        """ Удаление вопроса.

        - Открыть главную страницу
        - Открыть страницу вопроса
        - Нажать *** и выбрать "удалить вопрос"
        - Подтвердить удаление вопроса
        - Открыть страницу профиля
        - Проверить отсутствие вопроса в профиле

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если вопрос удален
        """

        chrome = Chrome(chrome_browser)

        chrome.go_to_site()
        chrome.go_to_site(f'{chrome.find_href_endpoint_open_feed_first_post()}')
        chrome.make_add_cookies(valid_cookie_another_user)
        chrome.click_btn_more_question()
        chrome.click_menu_item_delete()
        chrome.click_btn_blue()
        chrome.go_to_site('/profile/')
        elem = chrome.find_profile_no_published_data()
        check_element_text_is_on_page(elem, chrome)

    def test_delete_all_cookies(self, chrome_browser, firefox_browser):
        """ Удалить из обоих браузеров использованные в этом классе куки.

        :param chrome_browser: Браузер, на котором делаем автотесты
        :return: OK - если использованные в этом классе куки удалены
        """

        chrome = Chrome(chrome_browser)
        firefox = FireFox(firefox_browser)

        chrome.go_to_site()
        chrome_browser.delete_all_cookies()
        firefox.go_to_site()
        firefox_browser.delete_all_cookies()
