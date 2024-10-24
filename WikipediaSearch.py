from selenium.webdriver.common.by import By  # Импорт для поиска элементов
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def search_wikipedia(query):
    chrome_options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(f"https://ru.wikipedia.org/wiki/{query}")
    time.sleep(3)
    return driver


def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs, start=1):
        print(f"\nПараграф {i}:\n{paragraph.text}")
        input("\nНажмите Enter для продолжения...\n")


def list_internal_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    for i, link in enumerate(links, start=1):
        print(f"Ссылка {i}: {link.get_attribute('href')} - {link.text}")

    choice = int(input("Введите номер ссылки, на которую хотите перейти (0 для выхода): "))
    if choice == 0:
        return None
    selected_link = links[choice - 1].get_attribute('href')
    driver.get(selected_link)
    time.sleep(3)
    return driver


def main():
    query = input("Введите запрос для поиска на Википедии: ")
    driver = search_wikipedia(query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы статьи")
        print("2. Перейти по внутренней ссылке")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            list_paragraphs(driver)
        elif choice == '2':
            driver = list_internal_links(driver)
            if driver is None:
                break
        elif choice == '3':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

    driver.quit()


if __name__ == "__main__":
    main()
