import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestCalculator(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Firefox()
    self.driver.get("https://duckduckgo.com")

    wait = WebDriverWait(self.driver, 60)
    search = wait.until(
      expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, "input.search-input_searchInput__eWmpY")
      )
    )

    search.send_keys("calculator")
    search.send_keys(Keys.ENTER)
    self.display = wait.until(
      expected_conditions.visibility_of_element_located(
        (By.ID, "display")
      )
    )

    self.key_0 = self.driver.find_element(By.CSS_SELECTOR, "button[value='0']")
    self.key_1 = self.driver.find_element(By.CSS_SELECTOR, "button[value='1']")
    self.key_2 = self.driver.find_element(By.CSS_SELECTOR, "button[value='2']")
    self.key_3 = self.driver.find_element(By.CSS_SELECTOR, "button[value='3']")
    self.key_4 = self.driver.find_element(By.CSS_SELECTOR, "button[value='4']")
    self.key_5 = self.driver.find_element(By.CSS_SELECTOR, "button[value='5']")
    self.key_6 = self.driver.find_element(By.CSS_SELECTOR, "button[value='6']")
    self.key_7 = self.driver.find_element(By.CSS_SELECTOR, "button[value='7']")
    self.key_8 = self.driver.find_element(By.CSS_SELECTOR, "button[value='8']")
    self.key_9 = self.driver.find_element(By.CSS_SELECTOR, "button[value='9']")

    self.key_plus = self.driver.find_element(By.CSS_SELECTOR, "button[value='+']")
    self.key_minus = self.driver.find_element(By.CSS_SELECTOR, "button[value='-']")
    self.key_times = self.driver.find_element(By.CSS_SELECTOR, "button[value='×']")
    self.key_divide = self.driver.find_element(By.CSS_SELECTOR, "button[value='÷']")
    self.key_equals = self.driver.find_element(By.CSS_SELECTOR, "button[value='=']")


  def tearDown(self):
    self.driver.quit()

  def test_A_sum(self):
    """Somar dois números diferentes e verificar o resultado."""
    self.key_8.click()
    self.key_plus.click()
    self.key_7.click()
    self.key_equals.click()
    self.assertEqual("15", self.display.text)

  # def test_B_multiplication_and_division(self):
  #   """Multiplicar dois números diferentes e em seguida dividir o resultado por 10 e verificar o resultado."""
  #   pass

  # def test_C_subtraction_and_other_operation(self):
  #   """Fazer duas operações diferentes (uma sendo subtração) e verificar o resultado da última operação."""

  # def test_D_three_different_operations(self):
  #   """Fazer três operações diferentes, verificar o resultado de cada uma delas, e verificar que as três operações aparecem no histórico."""
