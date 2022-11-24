from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    def calculate_value(x: int) -> str:
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.maximize_window()

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    value_element_to_calculate = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "input_value")))
    calculated_value = calculate_value(value_element_to_calculate.text)

    answer_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "answer")))
    answer_field.send_keys(calculated_value)

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, "solve").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
