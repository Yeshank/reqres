from selenium.webdriver.common.by import By

from pageobject.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    get_api = (By.CSS_SELECTOR, "span[class='url']")
    post_api = (By.LINK_TEXT, "CREATE")
    put_api  = (By.CSS_SELECTOR, "li[data-id='put'] a")
    patch_api  = (By.CSS_SELECTOR, "li[data-id='patch'] a")
    delete_api = (By.LINK_TEXT, "DELETE")

    def get_get_api(self):
        return self.driver.find_element(*HomePage.get_api)

    def get_post_api(self):
        return self.driver.find_element(*HomePage.post_api)

    def get_put_api(self):
        return self.driver.find_element(*HomePage.put_api)

    def get_patch_api(self):
        return self.driver.find_element(*HomePage.patch_api)

    def get_delete_api(self):
        return self.driver.find_element(*HomePage.delete_api)
