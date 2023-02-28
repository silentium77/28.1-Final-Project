import pytest

from pages.registr_page import Locators_RT_REGISTR


# проверяем что страница регистрации открывается
@pytest.mark.registration
def test_can_open_registration_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = Locators_RT_REGISTR(browser,browser.current_url)
    # проверяем, что открылась страница регистрации
    page2.should_be_message_about_registration()

@pytest.mark.registration
def test_that_all_input_forms_presented_on_registration_page(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    # проверяем, что открылась страница регистрации
    page2.should_be_message_about_registration()
    # проверяем что на странице регистрации есть поля
    # для ввода данных пользователя (имя,фамилия,регион,имеил или телефон, пароль, подтверждение пароля)
    page2.should_be_name_surname_login_password_confirm_password_forms()

@pytest.mark.registration
def test_that_logo_is_presented(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    # проверяем что на странице есть лого
    page2.if_there_is_logo()

@pytest.mark.registration
def test_show_error_message_in_case_name_is_entered_not_in_сyrillic(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    name = "Yuliya"
    # вводим имя латиницей в поле Имя
    page2.enter_first_name(name)
     # проверяем что появилась надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    page2.should_have_name_error_message()

@pytest.mark.registration
def test_show_error_message_in_case_surname_is_entered_not_in_сyrillic(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    surname = "Zimina"
    # вводим фамилию латиницей в поле Имя
    page2.enter_last_name(surname)
     # проверяем что появилась надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    page2.should_have_surname_error_message()

@pytest.mark.registration
def test_show_error_message_in_case_password_shorter_then_8_symbols(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    password = "5R9824"
    # вводим пароль в поле Пароль длиной 5 символов
    page2.enter_password(password)
    # проверяем что появилась надпись "Длина пароля должна быть не менее 8 символов"
    page2.should_have_error_message_that_password_should_be_more_then_8_symbols()

@pytest.mark.registration
def test_show_error_message_in_case_password_does_not_contain_capital_letters(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    name = "Yuliya"
    password = "1ghu"
    page2.enter_first_name(name)
    # вводим пароль в поле Пароль без заглавных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать хотя бы одну заглавную букву"
    page2.should_have_error_message_that_password_does_not_contain_capital_letters()

@pytest.mark.registration
def test_show_error_message_in_case_password_does_not_contain_small_letters(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    name = "Yuliya"
    password = "LOGO25"
    page2.enter_first_name(name)
    # вводим пароль в поле Пароль без строчных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать хотя бы одну заглавную букву"
    page2.should_have_error_message_that_password_does_not_contain_small_letters()

@pytest.mark.registration
def test_show_error_message_in_case_password_contains_cyrrilics_letters(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    name = "Yuliya"
    password = "Яблокоogkgjgy"
    page2.enter_first_name(name)
    # вводим пароль в поле Пароль без заглавных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать только латинские буквы"
    page2.should_have_error_message_that_password_must_contain_only_latin_letters()

@pytest.mark.registration
def test_show_error_message_in_case_of_password_and_confirmation_password_dont_match(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    password = "Logo25"
    confirm_password = "Logo24"
    # вводим пароль в поле Пароль
    page2.enter_password(password)
    # вводим не совпадающий с первым пароль в поле Подтвердить пароль
    page2.enter_confirmation_of_password(confirm_password)
    # нажимаем кнопку Зарегистрироваться
    page2.click_enter_reg_button()
    # проверяем что появилась надпись "Пароли не совпадают"
    page2.should_have_error_message_that_passwords_dont_match()

@pytest.mark.registration
def test_register_new_user(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    password = "T46ghtyugjhi"
    first_name = "Федор"
    last_name = "Федор"
    email = "fedorfedorov2524@gmail.com"
    # Регистрируем нового пользователя
    page2.register_new_user(first_name, last_name, email, password)
    page2.click_enter_reg_button()
    # проверяем что новый пользователь успешно прошел Регистрацию
    page2.should_have_message_to_confirm_email_of_new_user()

@pytest.mark.registration
def test_register_new_user_that_already_exists(browser):
    link = "https://b2c.passport.rt.ru/auth/"
    page = Locators_RT_REGISTR(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()
    page2 = Locators_RT_REGISTR(browser, browser.current_url)
    password = "Silentium77"
    first_name = "Юлия"
    last_name = "Зимина"
    email = "ziminajn90@gmail.com"
    # Регистрируем нового пользователя
    page2.register_new_user(first_name, last_name, email, password)
    page2.click_enter_reg_button()
    # проверяем что появилась надпись "Учётная запись уже существует"
    page2.should_have_message_that_account_already_exists()