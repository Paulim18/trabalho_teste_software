import os
# playwright.config.py
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context(
            record_video_dir="./videos",  # Diretório para salvar vídeos
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()

        # Sua lógica de teste aqui
        page.goto("file:///C:/Users/paulo/Downloads/trabalho/test_trabalho.html")
        page.wait_for_timeout(3000)  # Simule interações de usuário
        
        context.close()  # Garante que o vídeo será salvo ao finalizar
        browser.close()
