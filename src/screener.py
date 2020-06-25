from _md5 import md5

import requests
import imgkit



class Screener:

    @staticmethod
    def __prepare_html(html_text: str):
        return str(html_text)

    @staticmethod
    def do_screen_by_url(url: str, js_delay=0):

        path = md5(url.encode()).hexdigest() + '.png'

        options = {'format': 'png', 'width': '1920', 'javascript-delay': js_delay}

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
