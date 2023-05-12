import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 



link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    param = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    if param:
        button = browser.find_element(By.ID, "book")
        button.click()
    val= browser.find_element(By.ID, "input_value")

    x = val.text

    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(f"{y}")

    button2 = browser.find_element(By.ID, "solve")
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
