from pageobject.homepage import HomePage
import requests
import csv

from utllities.contextmanager import FileManager


class TestMainAuto:

    # Getting the text from the Api
    def test_get_api_data(self, url, browser_invocation, filenamemode):
        homepage = HomePage(browser_invocation)  # Object creation
        api = url + homepage.get_get_api().text  # Getting the API Link
        r = requests.get(api)  # Getting the Text from the API
        if r.status_code == 200:  # Checking that any error is occured or not
            with FileManager(filenamemode[0], filenamemode[1]) as f:  # Writing the data in CSV file
                csv.writer(f).writerows(r.json().items())
        else:
            browser_invocation.quit()  # If error occured then closing the browser

    # Posting the text on API
    def test_post_in_api(self, url, browser_invocation, filenamemode):
        homepage = HomePage(browser_invocation)
        homepage.get_post_api().click()
        api = url + homepage.get_get_api().text
        r = requests.post(api, json={"name": "morpheus", "job": "leader"})  # Posting the data to API
        if r.status_code == 201:
            with FileManager(filenamemode[0], filenamemode[1]) as f:
                csv.writer(f).writerows(r.json().items())
        else:
            browser_invocation.quit()

    # Putting the test on API
    def test_put_in_api(self, url, browser_invocation, filenamemode):
        homepage = HomePage(browser_invocation)
        homepage.get_put_api().click()
        api = url + homepage.get_get_api().text
        r = requests.put(api, data={"name": "morpheus", "job": "zion resident"})  # Putting the data to API
        if r.status_code == 200:
            with FileManager(filenamemode[0], filenamemode[1]) as f:
                csv.writer(f).writerows(r.json().items())
        else:
            browser_invocation.quit()

    # Patching the text on API
    def test_patch_in_api(self, url, browser_invocation, filenamemode):
        homepage = HomePage(browser_invocation)
        homepage.get_patch_api().click()
        api = url + homepage.get_get_api().text
        r = requests.patch(api, data={"name": "morpheus", "job": "zion resident"})  # Patching the data to API
        if r.status_code == 200:
            with FileManager(filenamemode[0], filenamemode[1]) as f:
                csv.writer(f).writerows(r.json().items())
        else:
            browser_invocation.quit()

    # Deleting the API
    def test_delete_in_api(self, url, browser_invocation, filenamemode):
        homepage = HomePage(browser_invocation)
        homepage.get_delete_api().click()
        api = url + homepage.get_get_api().text
        r = requests.delete(api)  # Deleting the API
        if r.status_code == 204:
            with FileManager(filenamemode[0], filenamemode[1]) as f:
                csv.writer(f).writerows([{"Deleted successfully"}])
        else:
            browser_invocation.quit()
