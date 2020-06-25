from _sha256 import sha256

import requests
import imgkit


class UrlDoesNotExist(Exception):
    pass


class Screener:

    @staticmethod
    def __prepare_html(html_text: str):
        return str(html_text)

    @staticmethod
    def do_screen_by_url(url: str):

        try:
            response = requests.get(url)
        except requests.ConnectionError as exception:
            raise UrlDoesNotExist

        ready_html = Screener.__prepare_html(response.content)

        path = sha256(url.encode()).hexdigest() + '.png'

        options = {'format': 'png', 'width': '1920'}

        imgkit.from_url(url, path, options=options)

        return path

# from Screenshot import Screenshot_Clipping
# from selenium import webdriver
#
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
#
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-dev-shm-usage')
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get(url)
#
# path = sha256(url.encode()).hexdigest() + '.png'
#
# ob = Screenshot_Clipping.Screenshot()
#
# img_url = ob.full_Screenshot(driver, save_path=r'.', image_name=path)
