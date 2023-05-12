from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from modules.whois_func import whois_func
from modules.assets import assets
from modules.network_call import network_call

def main():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument('--no-sandbox')
    opts.add_argument("--mute-audio")
    urls = ["https://fmoviefree.sc/online/guardians-of-the-galaxy-vol-3-2023/watching.html/"]
    for url in urls:
        directory = f"outputs/{url[8:].split('/')[0]}"
        os.makedirs(directory, exist_ok=True)
        whois_func(url, directory)
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
        driver.get(url)
        assets(driver, url, directory)
        network_call(driver, directory)
main()