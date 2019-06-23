from selenium import webdriver
from time import sleep


URL = "https://careers.veeam.com/" # Путь к старнице
COUNTRY = "Romania" # Выбираемая страна
LANG = ["English",] # Список интересующих языков


browser = webdriver.Chrome() # Инициализируем webdriwer
browser.get(URL) # Открываем страницу
browser.maximize_window() # Расширяем окно браузера
country_select = browser.find_element_by_id("country-element") # Находим селектор страны по id
country_select.click() # Открываем список вариантов
sleep(1) # Ожидаем открытия списка
country_select.find_element_by_xpath("//span[contains(text(),'"+COUNTRY+"')]").click() # Выбираем страну
lang_select = browser.find_element_by_id("language") # Находим селектор языков
lang_select.click() # Открываем список вариантов
sleep(1) # Ожидаем открытия списка
lang_list = lang_select.find_elements_by_class_name("controls-checkbox") # Получаем список возможных вариантов
for lang in lang_list:
    if lang.text in LANG:
        lang.click() # Выбираем инетерсующие нас варианты
lang_select.find_element_by_class_name("selecter-fieldset-submit").click() # Применяем выбор языков
sleep(1) # Ожидаем применения
count_jobs = browser.find_element_by_class_name("pr0-md-down").text.split(" ")[0] # Находим информацию о количестве подходящих под фильтр вакансий
print(count_jobs) # Выводим количество вакансий по фильтру
