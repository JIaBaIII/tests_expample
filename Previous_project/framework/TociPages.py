import time

from selenium import webdriver

from config import URL
from framework.BaseApp import BasePage
from selenium.webdriver.common.by import By
from framework.helper import get_random_letters, get_random_gif, get_random_avatar, get_avatar_1mb, get_avatar_10mb
from selenium.webdriver.common.keys import Keys


class TociFieldsLocators:
    LOCATOR_SEARCH = (By.CLASS_NAME, 'Search_input__1uL5k')
    LOCATOR_LOGIN = (By.NAME, "Login")
    LOCATOR_PASSWORD = (By.NAME, "Password")
    LOCATOR_FIELD_SOURCE_URL = (By.NAME, "SourceURL")  # Поп-ап с линком на первоисточник
    LOCATOR_TITLE = (By.TAG_NAME, 'h1')
    LOCATOR_DESCRIPTION = (By.CLASS_NAME, 'ProseMirror')
    LOCATOR_WRITE_COMMENT = (By.CLASS_NAME, 'FieldTextarea_input__2K6cF')
    LOCATOR_ADD_TAG = (By.ID, 'react-select-2-input')  # todo нужно..
    LOCATOR_EDIT_PROFILE_FULL_NAME = (By.NAME, 'FirstName')
    LOCATOR_EDIT_PROFILE_DESCRIPTION = (By.NAME, 'description')
    LOCATOR_EDIT_PROFILE_PROFESSION = (By.NAME, 'Profession')
    LOCATOR_EDIT_PROFILE_PLACE_OF_WORK = (By.NAME, 'PlaceOfWork')
    LOCATOR_EDIT_PROFILE_EDUCATION = (By.NAME, 'Education')
    LOCATOR_ACCOUNT_SETTINGS_PHONE_NUMBER = (By.NAME, 'phone')
    LOCATOR_ACCOUNT_SETTINGS_EMAIL = (By.NAME, 'email')
    LOCATOR_ACCOUNT_SETTINGS_DATE_OF_BIRTH = (By.NAME, 'date')
    LOCATOR_SECURITY_OLD_PASSWORD = (By.NAME, 'Old passwords')
    LOCATOR_SECURITY_NEW_PASSWORD = (By.NAME, 'New password')
    LOCATOR_SECURITY_CONFIRM_NEW_PASSWORD = (By.NAME, 'Confirm password')
    LOCATOR_EDITOR_INPUT_FILE = (By.CLASS_NAME, 'css.file')
    LOCATOR_TAG_MENU = (By.CLASS_NAME, 'react-select__menu')
    LOCATOR_EDITOR_IMAGE_BLOCK = (By.CLASS_NAME, 'EditStyles_img_wrap__3Gfx0')
    LOCATOR_HIDDEN_INPUT_UPLOAD_AVATAR = (
        By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/section/div/div[2]/div/div[2]/div/div[2]/label/input')
    LOCATOR_COLLECTION_HIDDEN_INPUT_ADD_IMAGE = (
        By.XPATH, '/html/body/div[3]/div/div/div/form/div/div[1]/div[1]/section/div/input')
    LOCATOR_COLLECTION_NAME = (By.NAME, 'Name')
    LOCATOR_COLLECTION_DESCRIPTION = (By.NAME, 'Description')


class TociTextLocators:
    LOCATOR_SIGN_UP_WELCOME = (By.CLASS_NAME, 'AuthorizationPopup_pageName__1vUGb')
    LOCATOR_SIGN_UP_LOGIN = (By.CLASS_NAME, 'input_label__2dh1b')
    LOCATOR_SIGN_UP_PASSWORD = (By.CLASS_NAME, 'inputPassword_label__4z1L3')
    LOCATOR_SIGN_UP_PRIVACY = (By.CLASS_NAME, 'AuthorizationPopup_agreement__3ICVG')
    LOCATOR_SIGN_UP_LOGIN_WARNING = (By.CLASS_NAME, 'input_text__13WbU')
    LOCATOR_SIGN_UP_PASSWORD_WARNING = (By.CLASS_NAME, 'inputPassword_text__22zme')
    LOCATOR_POPUP_USER_ERROR = (By.CLASS_NAME, 'AuthorizationPopup_error__2_bvY')
    LOCATOR_POPUP_USER_ERROR_LEN_LOGIN = (By.CLASS_NAME, 'FieldSmallText_text__2om9x.'
                                                         'FieldSmallText_warning__Ibr5O.input_text__13WbU')
    LOCATOR_SIGN_IN_FORGOT_PASSWORD = (By.CLASS_NAME, 'AuthorizationPopup_recovery__2OvJp')
    LOCATOR_SIGN_IN_CHECKBOX_REQUIRE_AT_LOGIN = (By.CLASS_NAME, 'mt-26')
    LOCATOR_ASIDE_BLOCK_INTERESTING = (By.CLASS_NAME, 'AsideBlock_title__1CJgY')
    LOCATOR_COUNT_ANSWERS_ON_FEED = (By.CLASS_NAME, 'ml-auto.FeedListCard_countStyle__I5cBE')
    LOCATOR_COUNT_COMMENTS_ON_FEED = (By.CLASS_NAME, 'FeedListCard_countStyle__I5cBE.ml-auto')
    LOCATOR_FEED_SIDEBAR_BTNS_MENU = (By.CLASS_NAME, 'btn_text.MainSidebar_btnMenu__1jgjY')
    LOCATOR_PROFILE_BUTTONS_CONTENT_BY_TYPE = (By.CLASS_NAME, 'Tabs_tab_link__15w1-')
    LOCATOR_EDIT_PROFILE_INTERESTS = (By.CLASS_NAME, 'EditProfileContainer_labelInterests__17jFx')
    LOCATOR_EDIT_PROFILE_TITLE = (By.CLASS_NAME, 'EditProfileContainer_personName__3Kmnv')
    LOCATOR_PROFILE_ACCOUNT_SETTINGS_TITLE = (By.CLASS_NAME, 'EditProfileAccountContainer_title__1bpRl')
    LOCATOR_PROFILE_SECURITY_TITLE = (By.CLASS_NAME, 'EditProfileSecurityContainer_titlePage__2w0zr')
    LOCATOR_PROFILE_PRIVACY_TITLE = (By.CLASS_NAME, 'EditProfilePrivacyContainer_titlePage__1aT6M')
    LOCATOR_PROFILE_NOTIFICATION_TITLE = (By.CLASS_NAME, 'EditProfileNotificationContainer_titlePage__hE8Nt')
    LOCATOR_PROFILE_ACTIONS_TITLE = (By.CLASS_NAME, 'EditProfileActionsContainer_titlePage__1M760')
    LOCATOR_PROFILE_FIRST_PINNED_CARD = (By.CLASS_NAME, 'PinnedCard_card__3EryD')
    LOCATOR_PROFILE_SAVE_CHANGES = (By.CLASS_NAME, 'btn_red_gradient.btn_main-round.mr-8')
    LOCATOR_CONTENT_PAGE_AUTHORS_TOPIC = (By.CLASS_NAME, 'Author_topic__1T331')
    LOCATOR_QUESTION_PAGE_CARD_NAME = (By.CLASS_NAME, 'QuestionShortInfo_top__w1Bnv')
    LOCATOR_QUESTION_PAGE_ANSWERS_DESCRIPTION = (By.XPATH, '/html/body/div[1]/div[1]/div/div/'
                                                           'section/div/div[2]/div[2]/div/div[2]/div/div')  # todo id?
    LOCATOR_QUESTION_PAGE_TITLE = (By.CLASS_NAME, 'QuestionShortInfo_title__22xAa')
    LOCATOR_EDITOR_BLOCK_FORMULA_DESCRIPTION = (By.XPATH,
                                                '//*[@id="root"]/div[3]/div/div/div/div[1]/div[1]/div/textarea')
    LOCATOR_PROFILE_FIRST_PUBLISHED_CARD = (By.CLASS_NAME, 'd-flex.align-start')
    # todo id для поля ввода формулы
    LOCATOR_POST_PAGE_DESCRIPTION_TEXT = (By.CLASS_NAME, 'EditorMarkdown_markdown__bu2RU')
    LOCATOR_POST_PAGE_DESCRIPTION_TEXT_XPATH = (
        By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/section/div/div[2]/div/div[3]')
    LOCATOR_EDITORS_DESCRIPTION_BLOCK = (By.CLASS_NAME, 'ProseMirror')
    LOCATOR_TEXT_OF_FORMULA = (By.TAG_NAME, 'annotation')
    LOCATOR_ARTICLE_PAGE_TITLE = (By.CLASS_NAME, 'ArticleCard_title__2o3wX')
    LOCATOR_EDITORS_KATEX_BLOCK = (By.CLASS_NAME, 'katex')
    LOCATOR_EDITORS_CONTAINER = (By.CLASS_NAME, 'Editor_container__1H-2a.w-100')
    LOCATOR_QUESTION_CONTAINER_PAGE = (By.CLASS_NAME, 'QuestionCard_container__36c87')
    LOCATOR_CREATE_NEW_COLLECTION_POPUP_TITLE = (By.CLASS_NAME, 'CollectionPage_btnNewCollectionHover__22xFP')
    LOCATOR_CREATE_NEW_COLLECTION_POPUP_NAME = (By.CLASS_NAME, 'input_label__2dh1b')
    LOCATOR_CREATE_NEW_COLLECTION_POPUP_DESCRIPTION = (By.CLASS_NAME, 'input_label__2dh1b')
    LOCATOR_COLLECTION_TITLE = (By.CLASS_NAME, 'CardForCollections_title__2ghsN')
    LOCATOR_COLLECTION_CARDS_AMOUNT = (By.CLASS_NAME, 'CardForCollections_cardInfo__nXCVj')
    LOCATOR_QUESTION_PAGE_COUNT_ANSWERS = (By.CLASS_NAME, 'Answers_title__2tTs9')
    LOCATOR_CREATE_ANSWER_PAGE_QUESTION_TITLE = (By.CLASS_NAME, 'CreateAnswerPage_contentTitle__UMdwM')
    LOCATOR_COMMENT_TEXT = (By.CLASS_NAME, 'mb-5.Comment_context__1oLDx')
    LOCATOR_COMMENT_TEXT_DELETED = (By.CLASS_NAME, 'mb-5.Comment_context__1oLDx')
    LOCATOR_COMMENTS_TITLE = (By.CLASS_NAME, 'Comments_title__kGN3N')
    LOCATOR_ANSWER_PAGE_COMMENTS_COUNT = (By.CLASS_NAME, 'AnswerPage_btnAction__3c2ka.ml-30')
    LOCATOR_ANSWER_PAGE_UPVOTE_COUNT = (By.CLASS_NAME, 'AnswerPage_btnAction__3c2ka')


class TociButtonsLocators:
    LOCATOR_TOCI = (By.CLASS_NAME, 'Header_logo__38Ufx')
    LOCATOR_SIGN_UP = (By.CLASS_NAME, "ml-8")
    LOCATOR_SIGN_IN = (By.CLASS_NAME, "mr-5")
    LOCATOR_LOG_OUT = (By.CLASS_NAME, "ri-logout-box-r-fill")
    LOCATOR_CLOSE_POPUP = (By.CLASS_NAME, 'AuthorizationPopup_btnClose__2y6lY.btn_count')
    LOCATOR_CLOSE_POPUP_CREATE_COLLECTION = (By.CLASS_NAME, 'ModalWrapper_btn__2ecvL')
    LOCATOR_SEE_PASSWORD = (By.CLASS_NAME, 'ri-eye-off-fill')
    LOCATOR_HEADER_FEED = (By.XPATH, '/html/body/div[1]/div[1]/header/section/div/div[1]/a[1]')
    # todo id? Идентичные классы топики, рекомендации
    LOCATOR_HEADER_RECOMMENDATIONS = (By.XPATH, '/html/body/div[1]/div[1]/header/section/div/div[1]/a[2]')
    # todo id? Идентичные классы топики, фид
    LOCATOR_HEADER_TOPICS = (By.XPATH, '/html/body/div[1]/div[1]/header/section/div/div[1]/a[3]')
    # todo id? Идентичные классы фида, рекомендации
    LOCATOR_MY_AVATAR = (By.CLASS_NAME, "Header_avatar__16zYu")
    LOCATOR_POST_PAGE_AUTHOR_AVATAR = (By.CLASS_NAME, 'Author_avatar__2t4Wa')
    LOCATOR_PROFILE_INPUT_FILE = (By.TAG_NAME, 'input')
    LOCATOR_PROFILE_DELETE_IMAGE = (By.CLASS_NAME, 'UserPanel_btnDelete__2PzBW')
    LOCATOR_PROFILE_SAVE_NEW_IMAGE = (By.CLASS_NAME, 'btn_grey.radius.mr-10')
    LOCATOR_PROFILE_DELETE_AVATAR = (By.CLASS_NAME, 'btn_grey.radius')
    LOCATOR_PROFILE_ACCOUNT_SETTINGS = (By.LINK_TEXT, "Account settings")
    LOCATOR_PROFILE_SECURITY = (By.LINK_TEXT, "Security")
    LOCATOR_PROFILE_PRIVACY = (By.LINK_TEXT, "Privacy")
    LOCATOR_PROFILE_NOTIFICATION = (By.LINK_TEXT, "Notification")
    LOCATOR_PROFILE_ACTIONS = (By.LINK_TEXT, "Actions")
    LOCATOR_PROFILE_STATICS = (By.LINK_TEXT, "Statistics")
    LOCATOR_PROFILE_UNPIN_FIRST_POSTCARD = (By.CLASS_NAME, 'PinnedCard_btn__qF1yR')
    LOCATOR_PROFILE_RESTORE_UNPINNED_FIRST_POSTCARD = (
        By.CLASS_NAME, 'PinnedCard_btn__qF1yR.PinnedCard_restoreBtn__kHAsE')
    LOCATOR_PROFILE_NO_PUBLISHED_DATA = (By.CLASS_NAME, 'ProfilePage_emptyBlock__1faw2')
    LOCATOR_PROFILE_BTN_RESET = (By.CLASS_NAME, 'btn_border.btn_main-round.ml-65')
    LOCATOR_BTN_CONTINUE = (By.CLASS_NAME, 'AuthorizationPopup_sendBtn__1A_eF')
    LOCATOR_BTN_BORDER = (By.CLASS_NAME, "btn_border")  # могут быть разными кнопками (Post Answer, Sign in)
    LOCATOR_BTN_BLUE = (By.CLASS_NAME, "btn_blue")  # могут быть разными кнопками (Все синие кнопки)
    LOCATOR_BTN_GREY = (By.CLASS_NAME, "btn_grey")  # могут быть разными кнопками (Sign up, +-follow question)
    LOCATOR_BTN_RED = (By.CLASS_NAME, 'btn_red')  # могут быть разными кнопками (Unfollow question,
    LOCATOR_MAIN_ROUND = (By.CLASS_NAME, 'btn_main-round')  # могут быть разными кнопками
    LOCATOR_BTN_DARK = (By.CLASS_NAME, 'btn_dark')
    LOCATOR_CIRCLE = (By.CLASS_NAME, "BtnWithMenu_btn__3wqe8.btn_scale.btn_circle")
    LOCATOR_CIRCLE_MENU_ITEM_WRITE_ARTICLE = (By.LINK_TEXT, 'Write article')
    LOCATOR_CIRCLE_MENU_ITEM_ASK_QUESTION = (By.LINK_TEXT, 'Ask a question')
    LOCATOR_CIRCLE_MENU_ITEM_CREATE_NOTE = (By.LINK_TEXT, 'Create note')
    LOCATOR_WITH_MENU_BY_ICON = (By.CLASS_NAME, "icon-More1")  # todo id?
    LOCATOR_WITH_MENU_QUESTION = (By.CLASS_NAME, 'BtnWithMenu_wrap__9QZFC.BtnWithMenu_rectangle__2IsWb.'
                                                 'BtnWithMenu_center__2w4xS')  # todo id?
    LOCATOR_WITH_MENU_ANSWER = (By.CLASS_NAME, 'BtnWithMenu_btn__3wqe8.btn_scale.btn_circle')
    LOCATOR_WITH_MENU_ANSWER_PAGE = (By.CLASS_NAME, 'BtnWithMenu_btn__3wqe8.btn_circle.btn_scale')
    LOCATOR_QUESTION_PAGE_BTN_WITH_MENU_ANSWER = (By.CLASS_NAME, 'BtnWithMenu_btn__3wqe8.btn_count.ml-auto')  # todo id?
    LOCATOR_MENU_ITEMS = (By.CLASS_NAME, "BtnWithMenu__ico__3bSYm")
    LOCATOR_MENU_ITEM_ALL_MENU_OPTIONS = (By.CLASS_NAME, 'BtnWithMenu_menuItem__2lSST')
    LOCATOR_MENU_ITEM_SHARE_ARTICLE = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/"
                                                 "div/section/div/div[1]/div[1]/div[2]/div/div/button[2]")  # todo id?
    LOCATOR_MENU_ITEM_EDIT_QUESTION = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/"
                                                 "div/section/div/div[1]/div[1]/div[2]/div/div/button[1]")  # todo id?
    LOCATOR_MENU_ITEM_SHARE_QUESTION = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/"
                                                  "div/section/div/div[1]/div[1]/div[2]/div/div/button[2]")  # todo id?
    LOCATOR_MENU_ITEM_PINNED_POST = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/"
                                               "div/section/div/div[1]/div[1]/div[2]/div/div/button[3]")  # todo id?
    LOCATOR_QUESTION_MENU_ITEM_DELETE = (By.CLASS_NAME, 'BtnWithMenu__ico__3bSYm.BtnWithMenu__red__C1zH1')
    LOCATOR_MENU_ITEM_COMPLAIN = (By.CLASS_NAME, "BtnWithMenu__ico__3bSYm.BtnWithMenu__red__C1zH1")
    LOCATOR_ANSWER = (By.CLASS_NAME, 'btn_border_dark.btn_main-round')
    LOCATOR_BTNS = (By.CLASS_NAME, 'btn_scale.btn_circle')
    LOCATOR_FOLLOW_PROFILE = (By.CLASS_NAME, 'UserPanel_BtnFollow__2KFs2')
    LOCATOR_ARTICLE_TOOLTIP_BTN_FOLLOW = (By.CLASS_NAME, 'TooltipUserProfile_btnSettingFollow__3QxYR')
    LOCATOR_ARTICLE_FOLLOW_AUTHOR = (By.CLASS_NAME, 'btn_main-round.btn_border')
    LOCATOR_REPLY_ANSWER_0 = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/section/div/div[2]/div[2]/'
                                        'div[1]/div[3]/button[3]')  # todo id?
    LOCATOR_REPLY_ANSWER_1 = (By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/section/div/div[2]/div[2]/'
                                        'div[2]/div[3]/button[3]')  # todo id?
    LOCATOR_OPEN_ANSWERS_PAGE = (By.CLASS_NAME, 'AnswerItem_btnOpen__d6FI6')
    LOCATOR_QUESTION_PAGE_UPVOTE_ANSWER = (
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/section/div/div[3]/div[2]/div/div[3]/button[1]")
    LOCATOR_ANSWER_PAGE_UPVOTE = (By.CLASS_NAME, 'btn_circle.btn_scale')
    # todo id? Как подвязаться именно к этому UpVote
    LOCATOR_ARTICLE_SAVE_BTN = (By.CLASS_NAME, "btn_scale.btn_circle")
    LOCATOR_ARTICLE_SAVE_BTN_BELOW = (By.CLASS_NAME, 'btn_circle.btn_scale.ml-8')
    LOCATOR_BTN_COMMENTS = (By.CLASS_NAME, 'btn_text.ml-20')
    LOCATOR_EDITOR_OPEN_TOOLBAR = (By.CLASS_NAME, "Editor_btnMenu__l5-x1")
    LOCATOR_EDITOR_OPEN_TEXT_EDITOR = (By.CLASS_NAME, 'ml-10.Editor_btnMenu__l5-x1')
    LOCATOR_EDITOR_CLOSE_TOOLBAR = (By.CLASS_NAME, "Editor_openBtnMenu__g5eVA")
    LOCATOR_EDITOR_HIDDEN_INPUT_IMAGE = (
        By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/section/div/form/div[2]/div/div/div[2]/div/div/button[6]/input')
    LOCATOR_EDITOR_HIDDEN_INPUT_IMAGE_ANSWER = (
        By.XPATH,
        '//*[@id="__next"]/div[1]/div/div[2]/section/section/form/div[1]/div/div/div[2]/div/div/button[1]/input')
    LOCATOR_EDITOR_ADD_BLOCK_IMAGE = (By.CLASS_NAME, 'ri-image-line')  # todo id?
    LOCATOR_EDITOR_ADD_BLOCK = (By.CLASS_NAME, 'Editor_btn__1QR6l')
    LOCATOR_EDITOR_ADD_BLOCK_REFERENCE = (By.CLASS_NAME, 'ri-bookmark-3-line')  # todo id?
    LOCATOR_EDITOR_ADD_BLOCK_SEPARATOR = (By.CLASS_NAME, 'ri-separator')  # todo id?
    LOCATOR_EDITOR_ADD_BLOCK_FORMULA = (By.CLASS_NAME, 'ri-superscript')  # todo id?
    LOCATOR_EDITOR_SAVE_AND_PUBLISH = (By.CLASS_NAME, 'AnswerPopup_btnArrow__1rXWb.btn_main-round.btn_border.w-100')
    # todo id?
    LOCATOR_EDITOR_BTN_BACK = (By.CLASS_NAME, 'HeaderEditorNavMenu_btnBack__bHWsn')
    LOCATOR_POST_ANSWER = (By.CLASS_NAME, 'btn_main-round.btn_border.w-100')  # todo id?
    LOCATOR_BTN_POST_ANSWERS = (By.CLASS_NAME, 'CreateAnswerPage_answer__32uok')
    LOCATOR_AUTHORS_NAME = (By.CLASS_NAME, 'Author_name__1G3kk')  # todo id?
    LOCATOR_PROFILE_BTN_SEE_MORE_INFO = (By.CLASS_NAME, 'ProfilePage_btnSeeMore__3WSoq.btn_grey_scale.btn_main-round')
    LOCATOR_BTN_CREATE_ACCOUNT = (By.CLASS_NAME, 'AuthorizationPopup_signUpMow__2M-fA')
    LOCATOR_FEED_OPEN_FIRST_POST = (By.CLASS_NAME, 'FeedListCard_contentDesc__2rUBI')
    LOCATOR_FEED_FIRST_QUESTION_POST = (By.XPATH,
                                        '//*[@id="__next"]/div[1]/div/div/div/section/div/div[1]/div[1]/a/div')
    LOCATOR_FEED_FIRST_ARTICLE_POST = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/section/div/div[2]/div[1]/a/div')
    #                                                                    todo id? как-то определять посты в feed....
    LOCATOR_FEED_ARTICLE_SAVE_BTN = (
        By.XPATH, '/html/body/div[1]/div[1]/div/div/div/section/div/div[1]/div[1]/div[3]/img')  # todo id?
    LOCATOR_PROFILE_ARTICLE_SAVE_BTN = (
        By.XPATH, '/html/body/div[1]/div[1]/div/div/div/section/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[3]/img')
    # todo id?
    LOCATOR_TITLE_QUESTION = (By.CLASS_NAME, 'QuestionShortInfo_title__22xAa')
    LOCATOR_EDIT_ANSWER_BTN_SUBMIT = (By.CLASS_NAME, 'btn_border_grey.btn_main-round.mr-7')
    LOCATOR_ARTICLE_PAGE_RADIUS_BTNS = (By.CLASS_NAME, 'btn_border.radius.mr-8.ArticleCard_btnActionBottom__1t8fI')
    LOCATOR_QUESTION_PAGE_REQUEST = (By.CLASS_NAME, 'btn_border.radius.ml-7.QuestionCard_btnAction__1RO80')
    LOCATOR_SHOW_DESCRIPTION = (By.CLASS_NAME, 'QuestionCard_btnMoreText__C3GQm')
    LOCATOR_NEW_NOTIFICATION_POPUP = (By.CLASS_NAME, 'NotificationPopup_notification__1TRf9.animating-enter-done')
    LOCATOR_COLLECTIONS_ICON = (By.CLASS_NAME, 'btn_scale.btn_circle.ml-10.mt-2')
    LOCATOR_COLLECTION_CREATE_BTN = (By.CLASS_NAME, 'CollectionsLayout_btnCreate__PZ8yD')
    LOCATOR_COLLECTION_CREATE_CARD = (By.CLASS_NAME, 'CollectionPage_btnNewCollectionHover__22xFP')
    LOCATOR_COLLECTION_ADD_PICTURE_BTN = (By.CLASS_NAME, 'CreateCollectionPopup_stub__3xE45')
    LOCATOR_COLLECTION_SAVE_BTN = (By.CLASS_NAME, 'btn_red')
    LOCATOR_COLLECTION_CANCEL_BTN = (By.CLASS_NAME, 'btn_border')
    LOCATOR_COLLECTIONS_TABS = (By.CLASS_NAME, 'CollectionsLayout_link__1ivCB')
    LOCATOR_ARTICLE_OR_QUESTION_PAGE_ICON_UPVOTE = (By.CLASS_NAME, 'btn_text')
    LOCATOR_ARTICLE_OR_QUESTION_PAGE_ICON_UPVOTE_FILL = (By.CLASS_NAME, 'btn_text.ico-red')
    LOCATOR_CREATE_ANSWER_PAGE_SHOW_QUESTION = (By.CLASS_NAME, 'CreateAnswerPage_title__3E6Mv')
    LOCATOR_COLLECTION_CHECKBOX_MAKE_IT_PUBLISH = (By.CLASS_NAME, 'checkbox_ico__17Qf4')
    LOCATOR_BTN_MENU_COMMENT = (By.CLASS_NAME, 'Comment_restoreBtn__2vdcc')
    LOCATOR_UPVOTE_FIRST_COMMENT_LVL_1 = (By.CLASS_NAME, 'Comment_btnName__1Ux2n.ml-auto')
    LOCATOR_REPLY_TO_COMMENT = (By.XPATH, '/html/body/div[3]/div/div/div/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]')
    LOCATOR_REPLY_TO_COMMENT_LVL_2 = (
        By.XPATH, '/html/body/div[3]/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div/div[1]/div[3]/button')
    LOCATOR_BTN_COMMENTS_LVL_1 = (By.CLASS_NAME, 'Comment_comments__2O1Gx')
    LOCATOR_QUESTION_TITLE_ANSWER_PAGE = (By.CLASS_NAME, 'QuestionShortInfo_back__3qhJH')
    LOCATOR_PROFILE_SELECT_LANGUAGE = (By.CLASS_NAME, 'react-select__control')
    LOCATOR_FEED_COLLECTION_SELECT = (By.CLASS_NAME, 'styles_menuItem__1fAuo')


# findme -----------------------------------------  FindHelper  --------------------------------------------------------

class FindHelper(BasePage):

    def find_search_field(self):
        return self.find_element(TociFieldsLocators.LOCATOR_SEARCH)

    def find_header_toci(self):
        return self.find_element(TociButtonsLocators.LOCATOR_TOCI)

    def find_header_feed(self):
        return self.find_element(TociButtonsLocators.LOCATOR_HEADER_FEED)

    def find_header_recommendations(self):
        return self.find_element(TociButtonsLocators.LOCATOR_HEADER_RECOMMENDATIONS)

    def find_header_topics(self):
        return self.find_element(TociButtonsLocators.LOCATOR_HEADER_TOPICS)

    def find_btn_sign_up(self):
        return self.find_element(TociButtonsLocators.LOCATOR_SIGN_UP)

    def find_what_may_be_interested(self):
        return self.find_element(TociTextLocators.LOCATOR_ASIDE_BLOCK_INTERESTING)

    def find_on_feed_count_answers(self):
        return self.find_element(TociTextLocators.LOCATOR_COUNT_ANSWERS_ON_FEED)

    def find_on_feed_count_comments(self):
        return self.find_element(TociTextLocators.LOCATOR_COUNT_COMMENTS_ON_FEED)

    def find_feed_sidebar_collections(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[0])
        return elements[0]

    def find_feed_sidebar_my_questions(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[1])
        return elements[1]

    def find_feed_sidebar_quotes(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[2])
        return elements[2]

    def find_feed_sidebar_resent(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[3])
        return elements[3]

    def find_feed_sidebar_liked(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[4])
        return elements[4]

    def find_feed_sidebar_trash(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[5])
        return elements[5]

    def find_feed_sidebar_settings(self):
        elements = self.find_elements(TociTextLocators.LOCATOR_FEED_SIDEBAR_BTNS_MENU)
        self.highlight(elements[6])
        return elements[6]

    def find_btn_sign_in(self):
        return self.find_element(TociButtonsLocators.LOCATOR_SIGN_IN)

    def find_btn_border(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_BORDER)

    def find_btn_dark(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_DARK)

    def find_btn_blue(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_BLUE)

    def find_btn_red(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_RED)

    def find_pop_up_btn_sign_in(self):
        return self.find_element(TociButtonsLocators.LOCATOR_SIGN_IN)

    def find_pop_up_btn_create_account(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_CREATE_ACCOUNT)

    def find_pop_up_text_welcome(self):
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_WELCOME)

    def find_pop_up_text_login(self):
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_LOGIN)

    def find_pop_up_text_password(self):
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_PASSWORD)

    def find_pop_up_text_privacy(self):
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_PRIVACY)

    def find_pop_up_text_forgot_password(self):
        return self.find_element(TociTextLocators.LOCATOR_SIGN_IN_FORGOT_PASSWORD)

    def find_pop_up_text_checkbox_require_at_login(self):
        return self.find_element(TociTextLocators.LOCATOR_SIGN_IN_CHECKBOX_REQUIRE_AT_LOGIN)

    def find_profile_see_more_info(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_BTN_SEE_MORE_INFO)

    def find_editors_title(self):
        return self.find_element(TociFieldsLocators.LOCATOR_TITLE)

    def find_editors_title_text(self):
        return self.find_element(TociFieldsLocators.LOCATOR_TITLE).text

    def find_comments_btn(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_COMMENTS)

    def find_article_page_title(self):
        return self.find_element(TociTextLocators.LOCATOR_ARTICLE_PAGE_TITLE)

    def find_profile_field_full_name(self):
        return self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_FULL_NAME)

    def find_profile_field_profession(self):
        return self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_PROFESSION)

    def find_profile_field_place_of_work(self):
        return self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_PLACE_OF_WORK)

    def find_profile_field_education(self):
        return self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_EDUCATION)

    def find_profile_edit_interests(self):
        return self.find_element(TociTextLocators.LOCATOR_EDIT_PROFILE_INTERESTS)

    def find_profile_edit_language(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_SELECT_LANGUAGE)

    def find_profile_account_settings(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_ACCOUNT_SETTINGS)

    def find_profile_security(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_SECURITY)

    def find_profile_privacy(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_PRIVACY)

    def find_profile_notification(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_NOTIFICATION)

    def find_profile_actions(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_ACTIONS)

    def find_profile_statistics(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_STATICS)

    def find_edit_profile_title(self):
        return self.find_element(TociTextLocators.LOCATOR_EDIT_PROFILE_TITLE)

    def find_profile_account_settings_title(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_ACCOUNT_SETTINGS_TITLE)

    def find_profile_security_title(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_SECURITY_TITLE)

    def find_profile_privacy_title(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_PRIVACY_TITLE)

    def find_profile_notification_title(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_NOTIFICATION_TITLE)

    def find_profile_actions_title(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_ACTIONS_TITLE)

    def find_profile_first_pinned_card(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_FIRST_PINNED_CARD)

    def find_profile_btn_save_changes(self):
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_SAVE_CHANGES)

    def find_author_avatar(self):
        return self.find_element(TociButtonsLocators.LOCATOR_POST_PAGE_AUTHOR_AVATAR)

    def find_my_avatar(self):
        return self.find_element(TociButtonsLocators.LOCATOR_MY_AVATAR)

    def find_save_publish(self):
        return self.find_element(TociButtonsLocators.LOCATOR_EDITOR_SAVE_AND_PUBLISH)

    def find_profile_no_published_data(self):
        return self.find_element(TociButtonsLocators.LOCATOR_PROFILE_NO_PUBLISHED_DATA)

    def find_btn_follow_profile(self):
        return self.find_element(TociButtonsLocators.LOCATOR_FOLLOW_PROFILE)

    def find_btns_(self):
        return self.find_elements(TociButtonsLocators.LOCATOR_BTNS)

    def find_content_authors_topic(self):
        return self.find_element(TociTextLocators.LOCATOR_CONTENT_PAGE_AUTHORS_TOPIC)

    def find_question_card_name(self):
        return self.find_element(TociTextLocators.LOCATOR_QUESTION_PAGE_CARD_NAME)

    def find_btn_answer(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ANSWER)
        self.highlight(list_of_elements[1])
        return list_of_elements[1]

    def find_btn_answer_by_unsigned_user(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ANSWER)
        self.highlight(list_of_elements[1])
        return list_of_elements[1]

    def find_title_question(self):
        return self.find_element(TociButtonsLocators.LOCATOR_TITLE_QUESTION)

    def find_question_page_first_answers_description(self):
        list_of_elements = self.find_elements(TociTextLocators.LOCATOR_POST_PAGE_DESCRIPTION_TEXT)
        self.highlight(list_of_elements[1])
        return list_of_elements[1]

    def find_question_page_title(self):
        return self.find_element(TociTextLocators.LOCATOR_QUESTION_PAGE_TITLE)

    def find_description(self):
        return self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION)

    def find_description_text(self):
        return self.find_element(TociTextLocators.LOCATOR_POST_PAGE_DESCRIPTION_TEXT)

    def find_create_answer_question_page_title_description(self):
        title_and_description = ''
        title_and_description += self.find_create_answer_page_question_title().text
        title_and_description += '\n'
        title_and_description += self.find_element(TociTextLocators.LOCATOR_POST_PAGE_DESCRIPTION_TEXT).text
        return title_and_description

    def find_post_question_page_title_description(self):
        title_and_description = ''
        title_and_description += self.find_question_page_title().text
        title_and_description += '\n'
        title_and_description += self.find_element(TociTextLocators.LOCATOR_POST_PAGE_DESCRIPTION_TEXT_XPATH).text
        return title_and_description

    def find_post_article_page_title_description(self):
        title_and_description = ''
        title_and_description += self.find_article_page_title().text
        title_and_description += '\n'
        title_and_description += self.find_element(TociTextLocators.LOCATOR_POST_PAGE_DESCRIPTION_TEXT).text
        return title_and_description

    def find_editors_katex_text(self):
        return self.find_element(TociTextLocators.LOCATOR_EDITORS_KATEX_BLOCK)

    def find_editors_text(self):
        return self.find_element(TociTextLocators.LOCATOR_EDITORS_CONTAINER)

    def find_text_of_formula(self):
        return self.find_element(TociTextLocators.LOCATOR_TEXT_OF_FORMULA).text

    def find_tooltip_btn_follow(self):
        return self.find_element(TociButtonsLocators.LOCATOR_ARTICLE_TOOLTIP_BTN_FOLLOW)

    def find_btn_show_description(self):
        return self.find_element(TociButtonsLocators.LOCATOR_SHOW_DESCRIPTION)

    def find_new_notification_popup(self):
        return self.find_element(TociButtonsLocators.LOCATOR_NEW_NOTIFICATION_POPUP)

    def find_article_or_question_page_upvote_fill(self):
        return self.find_element(TociButtonsLocators.LOCATOR_ARTICLE_OR_QUESTION_PAGE_ICON_UPVOTE_FILL)

    def find_question_page_container(self):
        return self.find_element(TociTextLocators.LOCATOR_QUESTION_CONTAINER_PAGE)

    def find_icon_btn_more1(self):
        return self.find_element(TociButtonsLocators.LOCATOR_WITH_MENU_BY_ICON)

    def find_btn_collections(self):
        return self.find_element(TociButtonsLocators.LOCATOR_COLLECTIONS_ICON)

    def find_collection_field_name(self):
        return self.find_element(TociFieldsLocators.LOCATOR_COLLECTION_NAME)

    def find_collection_field_description(self):
        return self.find_element(TociFieldsLocators.LOCATOR_COLLECTION_DESCRIPTION)

    def find_btn_add_picture_to_collection(self):
        return self.find_element(TociButtonsLocators.LOCATOR_COLLECTION_ADD_PICTURE_BTN)

    def find_create_new_collection_popup_title(self):
        return self.find_element(TociTextLocators.LOCATOR_CREATE_NEW_COLLECTION_POPUP_TITLE)

    def find_create_new_collection_popup_name(self):
        return self.find_element(TociTextLocators.LOCATOR_CREATE_NEW_COLLECTION_POPUP_NAME)

    def find_create_new_collection_card(self):
        return self.find_element(TociButtonsLocators.LOCATOR_COLLECTION_CREATE_CARD)

    def find_create_new_collection_btn(self):
        return self.find_element(TociButtonsLocators.LOCATOR_COLLECTION_CREATE_BTN)

    def find_create_new_collection_popup_description(self):
        list_of_elements = self.find_elements(TociTextLocators.LOCATOR_CREATE_NEW_COLLECTION_POPUP_DESCRIPTION)
        for i in range(len(list_of_elements)):
            if 'Description' in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_create_new_collection_popup_btn_save(self):
        return self.find_element(TociButtonsLocators.LOCATOR_COLLECTION_SAVE_BTN)

    def find_collection_title(self):
        return self.find_element(TociTextLocators.LOCATOR_COLLECTION_TITLE)

    def find_exactly_collection_title_name(self, collection_name):
        list_of_elements = self.find_elements(TociTextLocators.LOCATOR_COLLECTION_TITLE)
        for i in range(len(list_of_elements)):
            if collection_name in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_collection_cards_amount(self):
        return self.find_element(TociTextLocators.LOCATOR_COLLECTION_CARDS_AMOUNT)

    def find_second_collection_cards_amount(self):
        list_of_elements = self.find_elements(TociTextLocators.LOCATOR_COLLECTION_CARDS_AMOUNT)
        self.highlight(list_of_elements[1])
        return list_of_elements[1]

    def find_third_collection_cards_amount(self):
        list_of_elements = self.find_elements(TociTextLocators.LOCATOR_COLLECTION_CARDS_AMOUNT)
        self.highlight(list_of_elements[2])
        return list_of_elements[2]

    def find_create_new_collection_popup_btn_cancel(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_COLLECTION_CANCEL_BTN)
        for i in range(len(list_of_elements)):
            if 'Cancel' in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_my_collection_tab(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_COLLECTIONS_TABS)
        for i in range(len(list_of_elements)):
            if 'My collections' in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_subscriptions_collection_tab(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_COLLECTIONS_TABS)
        for i in range(len(list_of_elements)):
            if 'Subscriptions' in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_quotes_tab(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_COLLECTIONS_TABS)
        for i in range(len(list_of_elements)):
            if 'Quotes' in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_liked_tab(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_COLLECTIONS_TABS)
        for i in range(len(list_of_elements)):
            if 'Liked' in list_of_elements[i].text:
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_question_page_count_answers(self):
        return self.find_element(TociTextLocators.LOCATOR_QUESTION_PAGE_COUNT_ANSWERS)

    def find_btn_post_answers(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_POST_ANSWERS)

    def find_create_answer_page_show_question(self):
        return self.find_element(TociButtonsLocators.LOCATOR_CREATE_ANSWER_PAGE_SHOW_QUESTION)

    def find_create_answer_page_question_title(self):
        return self.find_element(TociTextLocators.LOCATOR_CREATE_ANSWER_PAGE_QUESTION_TITLE)

    def find_answer_page_comments_count(self):
        return self.find_element(TociTextLocators.LOCATOR_ANSWER_PAGE_COMMENTS_COUNT)

    def find_answer_page_upvote_count(self):
        return self.find_element(TociTextLocators.LOCATOR_ANSWER_PAGE_UPVOTE_COUNT)

    def find_question_title_answer_page(self):
        return self.find_element(TociButtonsLocators.LOCATOR_QUESTION_TITLE_ANSWER_PAGE)

    def find_comment_text(self):
        return self.find_element(TociTextLocators.LOCATOR_COMMENT_TEXT)

    def find_first_comment_text_lvl_2(self):
        time.sleep(0.3)
        list_of_elem = self.find_elements(TociTextLocators.LOCATOR_COMMENT_TEXT)
        self.highlight(list_of_elem[1])
        return list_of_elem[1].text

    def find_second_comment_text_lvl_2(self):
        time.sleep(0.3)
        list_of_elem = self.find_elements(TociTextLocators.LOCATOR_COMMENT_TEXT)
        self.highlight(list_of_elem[2])
        return list_of_elem[2].text

    def find_deleted_comment_text(self):
        return self.find_element(TociTextLocators.LOCATOR_COMMENT_TEXT_DELETED)

    def find_comment_btn_menu(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_MENU_COMMENT)

    def find_comments_title(self):
        return self.find_element(TociTextLocators.LOCATOR_COMMENTS_TITLE)

    def find_comment_input_field_text(self):
        return self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT).text

    def find_comment_placeholder_field_text(self):
        return self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT).get_attribute('placeholder')

    def find_btn_comments_lvl_1(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_COMMENTS_LVL_1)

    def find_href_endpoint_open_feed_first_post(self):
        href = self.find_element(TociButtonsLocators.LOCATOR_FEED_OPEN_FIRST_POST).get_attribute('href')
        endpoint = href.replace(URL, "")
        return endpoint

    def find_btn_request(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_QUESTION_PAGE_REQUEST)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Request':
                self.highlight(list_of_elements[i])
                return list_of_elements[i]

    def find_menu_item_complain(self):
        self.find_element(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == "Complain":
                self.highlight(list_of_elements[i])
                return list_of_elements[i].text

    def find_all_texts_in_description_blocks(self):
        list_of_elements = self.find_elements(TociTextLocators.LOCATOR_EDITORS_DESCRIPTION_BLOCK)
        final_string = list_of_elements[0].text
        for i in range(1, len(list_of_elements)):
            if list_of_elements[i].text:
                final_string += f'\n{list_of_elements[i].text}'
        return final_string

    def find_btn_reset(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_PROFILE_BTN_RESET)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Reset':
                self.highlight(list_of_elements[i])
                return list_of_elements[i]


# findme -----------------------------------------  ClickHelper  -------------------------------------------------------

class ClickHelper(BasePage):

    def click_on_feed(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_HEADER_FEED)

    def click_btn_sign_up(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_SIGN_UP)

    def click_btn_sign_in(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_SIGN_IN)

    def click_close_popup(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CLOSE_POPUP)

    def click_close_popup_create_new_collection(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CLOSE_POPUP_CREATE_COLLECTION)

    def click_btn_see_password(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_SEE_PASSWORD)  # fixme написать тест?

    def click_on_my_avatar(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_MY_AVATAR)

    def click_log_out(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_LOG_OUT)

    def click_btn_continue(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_CONTINUE)

    def click_btn_border(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_BORDER)

    def click_btn_dark(self):
        return self.find_element(TociButtonsLocators.LOCATOR_BTN_DARK).click()

    def click_btn_blue(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_BLUE)

    def click_btn_grey(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_GREY)

    def click_btn_red(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_RED)

    def click_btn_main_round(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_MAIN_ROUND)

    def click_btn_circle(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE)

    def click_write_article(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE_MENU_ITEM_WRITE_ARTICLE)

    def click_ask_question(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE_MENU_ITEM_ASK_QUESTION)

    def click_create_note(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE_MENU_ITEM_CREATE_NOTE)

    def click_editor_btn_back(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_BTN_BACK)

    def click_question_page_menu_answer(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_WITH_MENU_BY_ICON)
        return self.highlight_click(list_of_elements[1])

    def click_btn_menu_answer(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_WITH_MENU_ANSWER)

    def click_btn_menu_answer_page(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_WITH_MENU_ANSWER_PAGE)
        return self.highlight_click(list_of_elements[1])

    def click_complain(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEM_COMPLAIN)
        return self.highlight_click(list_of_elements[1])

    def click_answer(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ANSWER)
        return self.highlight_click(list_of_elements[1])

    def click_save_and_publish(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_SAVE_AND_PUBLISH)

    def click_to_comments_on_answer_0(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_REPLY_ANSWER_0)

    def click_to_comments_on_answer_1(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_REPLY_ANSWER_1)

    def click_btn_comments(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_COMMENTS)

    def click_btn_comments_answer_page(self):
        return self.click_on_element(TociTextLocators.LOCATOR_ANSWER_PAGE_COMMENTS_COUNT)

    def click_post_answer(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_POST_ANSWER)

    def click_post_answers(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_POST_ANSWERS)

    def click_post_answers_and_post_answer(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_POST_ANSWERS)
        self.click_on_element(TociButtonsLocators.LOCATOR_POST_ANSWER)

    def click_on_authors_name(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_AUTHORS_NAME)
        return self.find_element(TociTextLocators.LOCATOR_PROFILE_FIRST_PUBLISHED_CARD)

    def click_profile_see_more_info(self):  # fixme написать тест когда будет инфа о юзере в профиле
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_BTN_SEE_MORE_INFO)

    def click_btn_follow_profile(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_FOLLOW_PROFILE)

    def click_aside_btn_follow_in_article_tooltip(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_ARTICLE_TOOLTIP_BTN_FOLLOW)

    def click_btn_follow_author_in_article(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_ARTICLE_FOLLOW_AUTHOR)

    def click_upvote_answer_from_question_page(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_QUESTION_PAGE_UPVOTE_ANSWER)

    def click_upvote_from_answer_page(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ANSWER_PAGE_UPVOTE)
        return self.highlight_click(list_of_elements[4])

    def click_to_open_answers_page(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_OPEN_ANSWERS_PAGE)
        time.sleep(0.4)

    def click_create_answer_page_show_question(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_CREATE_ANSWER_PAGE_SHOW_QUESTION)

    def click_btn_save_new_image(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_SAVE_NEW_IMAGE)

    def click_profile_save_changes(self):
        return self.click_on_element(TociTextLocators.LOCATOR_PROFILE_SAVE_CHANGES)

    def click_profile_delete_avatar(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_DELETE_AVATAR)

    def click_profile_account_settings(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_ACCOUNT_SETTINGS)

    def click_profile_security(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_SECURITY)

    def click_profile_privacy(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_PRIVACY)

    def click_profile_notification(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_NOTIFICATION)

    def click_profile_actions(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_ACTIONS)

    def click_profile_statistics(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_STATICS)

    def click_on_feed_first_question_post(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_FEED_FIRST_QUESTION_POST)

    def click_edit_answer_btn_submit(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_EDIT_ANSWER_BTN_SUBMIT)

    def click_editor_add_block_formula(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_ADD_BLOCK_FORMULA)

    def click_profile_unpin_first_postcard(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_UNPIN_FIRST_POSTCARD)

    def click_profile_restore_unpinned_first_postcard(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_RESTORE_UNPINNED_FIRST_POSTCARD)

    def click_btn_show_more(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_SHOW_DESCRIPTION)

    def click_btn_see_all_collections(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_COLLECTIONS_ICON)

    def click_btn_create_new_collection(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_COLLECTION_CREATE_BTN)

    def click_create_new_collection_card(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_COLLECTION_CREATE_CARD)

    def click_btn_save_collection(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_COLLECTION_SAVE_BTN)

    def click_collection_checkbox_make_it_publish(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_COLLECTION_CHECKBOX_MAKE_IT_PUBLISH)

    def click_btn_menu_comment(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_MENU_COMMENT)

    def click_upvote_first_comment_lvl_1(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_UPVOTE_FIRST_COMMENT_LVL_1)

    def click_answer_page_upvote_count(self):
        return self.click_on_element(TociTextLocators.LOCATOR_ANSWER_PAGE_UPVOTE_COUNT)

    def click_question_title_answer_page(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_QUESTION_TITLE_ANSWER_PAGE)

    def click_reply_to_first_comment(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_REPLY_TO_COMMENT)

    def click_reply_to_first_comment_lvl_2(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_REPLY_TO_COMMENT_LVL_2)

    def click_btn_comments_lvl_1(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_BTN_COMMENTS_LVL_1)

    def click_feed_save_article_btn(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_FEED_ARTICLE_SAVE_BTN)

    def click_article_or_question_page_icon_upvote(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ARTICLE_OR_QUESTION_PAGE_ICON_UPVOTE)
        for i in range(len(list_of_elements)):
            if 'likes' in list_of_elements[i].text:
                return self.highlight_click(list_of_elements[i])

    def click_feed_select_save_to_exactly_collection(self, collection_name):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_FEED_COLLECTION_SELECT)
        for i in range(len(list_of_elements)):
            if collection_name in list_of_elements[i].text:
                return self.highlight_click(list_of_elements[i])

    def click_profile_save_article_btn(self):
        return self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_ARTICLE_SAVE_BTN)

    def click_edit(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if 'Edit' in list_of_elements[i].text:
                return self.highlight_click(list_of_elements[i])

    def click_menu_pin_post(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if 'Pinned' in list_of_elements[i].text:
                return self.highlight_click(list_of_elements[i])

    def click_menu_item_edit_answer(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Edit an answer':
                return self.highlight_click(list_of_elements[i])

    def click_menu_item_delete_answer(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Delete':
                return self.highlight_click(list_of_elements[i])

    def click_menu_item_delete(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Delete':
                return self.highlight_click(list_of_elements[i])

    def click_menu_item_dont_like(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == "Don't like":
                return self.highlight_click(list_of_elements[i])

    def click_menu_item_complain(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEMS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == "Complain":
                return self.highlight_click(list_of_elements[i])

    def click_menu_btn_complain(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEM_ALL_MENU_OPTIONS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Complain':
                return self.highlight_click(list_of_elements[i])

    def click_menu_btn_delete(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_MENU_ITEM_ALL_MENU_OPTIONS)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Delete':
                return self.highlight_click(list_of_elements[i])

    def click_btn_reset(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_PROFILE_BTN_RESET)
        for i in range(len(list_of_elements)):
            if list_of_elements[i].text == 'Reset':
                return self.highlight_click(list_of_elements[i])

    def click_follow_question(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_BTNS)
        return self.highlight_click(list_of_elements[6])

    def click_follow_question_unsigned_user(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_BTNS)
        return self.highlight_click(list_of_elements[4])

    def click_btn_icon_more1(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_WITH_MENU_BY_ICON)
        return self.highlight_click(list_of_elements[1])

    def click_btn_more_question(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_WITH_MENU_QUESTION)
        return self.highlight_click(list_of_elements[1])

    def click_btn_more_answer(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_WITH_MENU_ANSWER)
        return self.highlight_click(list_of_elements[2])

    def click_article_page_save_btn(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ARTICLE_SAVE_BTN)
        return self.highlight_click(list_of_elements[6])

    def click_article_page_save_btn_below(self):
        list_of_elements = self.find_elements(TociButtonsLocators.LOCATOR_ARTICLE_SAVE_BTN_BELOW)
        return self.highlight_click(list_of_elements[1])

    def make_click_delete_article(self):
        self.click_btn_icon_more1()
        self.click_menu_item_delete()
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_BLUE)

    def make_click_delete_question(self):
        self.click_btn_icon_more1()
        self.click_menu_item_delete()
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_BLUE)


# findme -----------------------------------------  MakeHelper  --------------------------------------------------------

class MakeHelper(BasePage):

    def clear_text(self):
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        time.sleep(0.1)
        webdriver.ActionChains(self.driver).send_keys("a").perform()
        time.sleep(0.1)
        webdriver.ActionChains(self.driver).key_up(Keys.CONTROL).perform()
        time.sleep(0.1)
        webdriver.ActionChains(self.driver).send_keys(Keys.DELETE).perform()
        time.sleep(0.6)

    def ctrl_z(self):
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('z').key_up(Keys.CONTROL).perform()
        time.sleep(0.2)

    def make_log_out(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_MY_AVATAR)
        self.click_on_element(TociButtonsLocators.LOCATOR_LOG_OUT)

    def make_pop_up_warning_required_login(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(Keys.TAB, get_random_letters(10), Keys.TAB)
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_LOGIN_WARNING)

    def make_pop_up_warning_required_password(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(get_random_letters(3), Keys.TAB, Keys.TAB)
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_PASSWORD_WARNING)

    def make_pop_up_warning_count_password_len(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_PASSWORD)
        search_field.send_keys(1, Keys.TAB)
        return self.find_element(TociTextLocators.LOCATOR_SIGN_UP_PASSWORD_WARNING)

    def make_pop_up_warning_invalid(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(get_random_letters(3), Keys.TAB, get_random_letters(20), Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR)

    def make_pop_up_warning_similar(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(111, Keys.TAB, 111111, Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR)

    def make_pop_up_warning_login_pattern(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(get_random_letters(1), Keys.TAB, 'Jdbjkasg34', Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR_LEN_LOGIN)

    def make_pop_up_warning_login_pattern_21(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(get_random_letters(21), Keys.TAB, 'Jdbjkasg34', Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR)

    def make_pop_up_warning_simple_password(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys('qwe', Keys.TAB, 111111, Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR)

    def make_pop_up_warning_simple_password_down_letter(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys('qwy', Keys.TAB, 'zxcvbn', Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR)

    def make_pop_up_warning_simple_password_up_letter(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys('qwt', Keys.TAB, 'ZXCVBN', Keys.ENTER)
        return self.find_element(TociTextLocators.LOCATOR_POPUP_USER_ERROR)

    def make_pre_steps_for_article_create(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE)
        self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE_MENU_ITEM_WRITE_ARTICLE)
        self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION)

    def make_steps_for_comment_create(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_COMMENTS)
        WriteHelper(self).write_a_comment()

    def make_pre_steps_for_question_create(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE)
        self.click_on_element(TociButtonsLocators.LOCATOR_CIRCLE_MENU_ITEM_ASK_QUESTION)
        return self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION)

    def make_upload_image_in_editor(self):
        self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION).send_keys(
            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
        self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_OPEN_TOOLBAR)
        self.find_element(TociButtonsLocators.LOCATOR_EDITOR_HIDDEN_INPUT_IMAGE). \
            send_keys(get_random_gif())
        self.find_element(TociFieldsLocators.LOCATOR_EDITOR_IMAGE_BLOCK)

    def make_upload_image_in_editor_answer(self):
        self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION).send_keys(
            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
        self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_OPEN_TOOLBAR)
        self.find_element(TociButtonsLocators.LOCATOR_EDITOR_HIDDEN_INPUT_IMAGE_ANSWER). \
            send_keys(get_random_gif())
        self.find_element(TociFieldsLocators.LOCATOR_EDITOR_IMAGE_BLOCK)

    def make_upload_image_on_avatar(self):
        self.find_element(TociFieldsLocators.LOCATOR_HIDDEN_INPUT_UPLOAD_AVATAR). \
            send_keys(get_random_avatar())
        return time.sleep(1)

    def make_upload_image_on_avatar_1mb(self):
        self.find_element(TociFieldsLocators.LOCATOR_HIDDEN_INPUT_UPLOAD_AVATAR). \
            send_keys(get_avatar_1mb())
        return time.sleep(1.5)

    def make_upload_image_on_avatar_10mb(self):
        self.find_element(TociFieldsLocators.LOCATOR_HIDDEN_INPUT_UPLOAD_AVATAR). \
            send_keys(get_avatar_10mb())
        return time.sleep(1.5)

    def make_upload_image_on_collection_cover(self):
        self.find_element(TociFieldsLocators.LOCATOR_COLLECTION_HIDDEN_INPUT_ADD_IMAGE).\
            send_keys(get_random_gif())
        return time.sleep(1)

    def make_block_function(self, my_formula):
        find_input = self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION)
        find_input.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                             Keys.ARROW_DOWN, Keys.ENTER, Keys.ENTER, Keys.ARROW_UP)
        self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_OPEN_TOOLBAR)
        self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_ADD_BLOCK_FORMULA)
        input_formula = self.find_element(TociTextLocators.LOCATOR_EDITOR_BLOCK_FORMULA_DESCRIPTION)
        input_formula.send_keys(my_formula)
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_RED)
        
    def make_add_cookies(self, valid_cookie_user):
        self.driver.add_cookie(valid_cookie_user)
        self.driver.refresh()

    def make_delete_content_in_title(self):
        content = self.find_element(TociFieldsLocators.LOCATOR_TITLE)
        while content.text is not "":
            content.send_keys(Keys.BACKSPACE)
        return self

    def make_delete_collection_name(self):
        content = self.find_element(TociFieldsLocators.LOCATOR_COLLECTION_NAME)
        while content.text is not "":
            content.send_keys(Keys.BACKSPACE)
        return self

    def make_delete_content_in_description(self):
        self.click_on_element(TociFieldsLocators.LOCATOR_DESCRIPTION)
        self.clear_text()

    def make_profile_choose_language_en(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_SELECT_LANGUAGE)
        self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_EDUCATION).send_keys(
            Keys.TAB, Keys.ARROW_DOWN, Keys.ENTER)

    def make_profile_choose_language_ru(self):
        self.click_on_element(TociButtonsLocators.LOCATOR_PROFILE_SELECT_LANGUAGE)
        self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_EDUCATION).send_keys(
            Keys.TAB, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)


# findme -----------------------------------------  WriteHelper  -------------------------------------------------------

class WriteHelper(BasePage):

    def enter_login(self, word):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_LOGIN)
        search_field.send_keys(word)
        return search_field

    def enter_password(self, word):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_PASSWORD)
        search_field.send_keys(word)
        return search_field

    def write_title(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_TITLE)
        search_field.send_keys("Auto-title # ", get_random_letters(5), Keys.ARROW_DOWN)
        
    def write_another_title(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_TITLE)
        search_field.clear()
        search_field.send_keys("Auto-title new-rewrote) # ", get_random_letters(5), Keys.ARROW_DOWN)
        
    def write_description(self, some_text):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION)
        search_field.send_keys(some_text, '\nGo next line ->')
        search_field.send_keys('\nНу пожалуйстааааа..')
        search_field.send_keys('\n...Спасибо)')
        time.sleep(0.3)

    def write_title_and_description(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_TITLE)
        search_field.send_keys("Auto-title # ", get_random_letters(5), Keys.TAB, "Авто описание поста. Би-буп ")
        
    def add_separator(self):
        list_of_elem = self.find_elements(TociButtonsLocators.LOCATOR_EDITOR_ADD_BLOCK)
        return self.highlight_click(list_of_elem[5])

    def write_advanced_description_add_separator(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_DESCRIPTION)
        search_field.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                               Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER, Keys.ENTER)
        self.click_on_element(TociButtonsLocators.LOCATOR_EDITOR_OPEN_TOOLBAR)
        self.add_separator()
        
    def write_tag(self):
        search_field_1 = self.find_element(TociFieldsLocators.LOCATOR_ADD_TAG)
        search_field_1.send_keys("auto_spelling_tag_of_doom")
        search_field_1.send_keys(Keys.ARROW_UP, Keys.ARROW_UP, Keys.ARROW_UP, Keys.ARROW_UP, Keys.ARROW_UP,
                                 Keys.ARROW_UP, Keys.ARROW_UP)
        search_field_1.send_keys(Keys.ENTER)
        
    def write_tag_2(self):
        search_01 = self.find_element(TociFieldsLocators.LOCATOR_ADD_TAG)
        search_01.send_keys('auto_spelling_tag_of_doom')
        search_01.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                            Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN)
        search_01 = self.find_element(TociFieldsLocators.LOCATOR_ADD_TAG)
        search_01.send_keys(Keys.ENTER)

    def write_profile_full_name(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_FULL_NAME)
        return search_field.send_keys(f'Auto Created Guy #{get_random_letters(5)}')

    def write_profile_profession(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_PROFESSION)
        return search_field.send_keys(get_random_letters(5))

    def write_profile_place_of_work(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_PLACE_OF_WORK)
        return search_field.send_keys(get_random_letters(5))

    def write_profile_education(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_EDIT_PROFILE_EDUCATION)
        return search_field.send_keys(get_random_letters(5))

    def write_a_comment(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT)
        comment_text = f'Привет, я коммент. # {get_random_letters(5)}'
        search_field.send_keys(comment_text)
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_RED)
        time.sleep(0.4)
        return comment_text

    def write_another_comment(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT)
        comment_text = f'Привет, я другой коммент.Хехе) # {get_random_letters(5)}'
        search_field.send_keys(comment_text)
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_RED)
        time.sleep(0.1)
        return comment_text

    def write_a_comment_lvl_2(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT)
        search_field.send_keys(
            'Ооо! Что ты тут делашеь?', Keys.ENTER, 'Комментик у тебя, кстати, так себе..', Keys.ENTER,
            f'Без обид) # {get_random_letters(5)}')
        comment_text = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT).text
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_RED)
        time.sleep(0.1)
        return comment_text

    def write_another_comment_lvl_2(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT)
        search_field.send_keys(
            'Пёс ты, а не коммент.', Keys.ENTER, f'Без каких-либо обид,ага)) # {get_random_letters(5)}')
        comment_text = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT).text
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_RED)
        time.sleep(0.1)
        return comment_text

    def write_downvote_explanation(self):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_WRITE_COMMENT)
        search_field.send_keys('F*ck this!')
        self.click_on_element(TociButtonsLocators.LOCATOR_BTN_BLUE)

    def write_collection_name(self, fake_collection_name):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_COLLECTION_NAME)
        search_field.send_keys(fake_collection_name)
        return fake_collection_name

    def write_collection_description(self, fake_collection_description):
        search_field = self.find_element(TociFieldsLocators.LOCATOR_COLLECTION_DESCRIPTION)
        search_field.send_keys(fake_collection_description)
        return fake_collection_description
