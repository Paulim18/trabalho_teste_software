import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture(scope="function")
def page_context():
    with sync_playwright() as playwright:
        # Lançar o navegador
        browser = playwright.chromium.launch(headless=False)  # headless=True para modo sem interface
        context = browser.new_context()
        page = context.new_page()
        yield page  # Retorna a página para uso nos testes
        context.close()
        browser.close()

def test_register_success(page_context: Page):
    print("Iniciando o teste de sucesso no cadastro.")
    page = page_context
    page.goto("file:///C:/Users/paulo/Downloads/trabalho/test_trabalho.html")
    page.fill('#registerName', 'Carlos')
    page.fill('#registerEmail', 'carlos@example.com')
    page.fill('#registerPassword', 'senha123')
    page.click('#registerButton')
    
    # Verificar se o alerta foi exibido com a mensagem esperada
    assert page.expect_event("dialog", lambda dialog: "Cadastro realizado com sucesso!" in dialog.message)
    print("Teste de sucesso no cadastro passou com sucesso!")

def test_register_empty_fields(page_context: Page):
    print("Iniciando o teste de cadastro com campos vazios.")
    page = page_context
    page.goto("file:///C:/Users/paulo/Downloads/trabalho/test_trabalho.html")
    page.click('#registerButton')

    # Verificar se o alerta foi exibido com a mensagem esperada
    assert page.expect_event("dialog", lambda dialog: "Por favor, preencha todos os campos de cadastro!" in dialog.message)
    print("Teste de cadastro com campos vazios passou com sucesso!")

def test_login_success(page_context: Page):
    print("Iniciando o teste de sucesso no login.")
    page = page_context
    page.goto("file:///C:/Users/paulo/Downloads/trabalho/test_trabalho.html")
    page.fill('#loginEmail', 'carlos@example.com')
    page.fill('#loginPassword', 'senha123')
    page.click('#loginButton')

    # Verificar se o alerta foi exibido com a mensagem esperada
    assert page.expect_event("dialog", lambda dialog: "Login realizado com sucesso!" in dialog.message)
    print("Teste de sucesso no login passou com sucesso!")

def test_login_empty_fields(page_context: Page):
    print("Iniciando o teste de login com campos vazios.")
    page = page_context
    page.goto("file:///C:/Users/paulo/Downloads/trabalho/test_trabalho.html")
    page.click('#loginButton')

    # Verificar se o alerta foi exibido com a mensagem esperada
    assert page.expect_event("dialog", lambda dialog: "Por favor, preencha todos os campos de login!" in dialog.message)
    print("Teste de login com campos vazios passou com sucesso!")
