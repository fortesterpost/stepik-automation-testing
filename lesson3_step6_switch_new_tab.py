from selenium import webdriver
import time
import math

# математическая функция
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # находим кнопку и нажимаем
    element = browser.find_element_by_css_selector("button.trollface")
    element.click()

    # переходим в новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # вызываем математическую функцию и вычисляем
    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)

    # код, который заполняет  поля
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

