import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_autoinstaller.install()
#


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()

'''Явное ожидание'''

def test_show_all_pets(driver):
    #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('gavrilovdan.spb@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('rB7S21fD')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

def test_my_pets(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('gavrilovdan.spb@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('rB7S21fD')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    assert  driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]')

    #number_pets = driver.find_element(By.XPATH, '//table[@class="table table-hover"]//td')
    #number_pets = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    #sum_pets = len(number_pets)/4
    #count_pets = driver.find_element(By.XPATH, '//table[@class="table table-hover"]/tr')

    assert int(number_pets) == (len(count_pets)/4)

def test_show_all_my_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('gavrilovdan.spb@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('rB7S21fD')
    driver.implicitly_wait(10)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()


    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ', ' in descriptions[i]
       parts = descriptions[i].text.split(", ")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0