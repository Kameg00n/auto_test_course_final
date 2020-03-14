from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math

class ProductPage(BasePage):
    def should_be_button_add(self):
        add_button = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        add_button.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")