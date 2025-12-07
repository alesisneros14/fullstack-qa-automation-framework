from tests.pages.login_page import LoginPage

def test_login_exitoso(driver):
    page = LoginPage(driver)
    page.open()
    page.perform_login("admin", "admin123")
    assert "Bienvenido" in page.get_welcome_message()

def test_login_fallido(driver):
    page = LoginPage(driver)
    page.open()
    page.perform_login("usuario_falso", "1234")
    assert "Credenciales Invalidas" in page.get_error_message()