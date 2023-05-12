from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
import os

def network_call(driver, directory):
    file_path = f"{directory}/network_data.txt"
    existing_urls = set()
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for line in file:
                url = line.split()[0]
                existing_urls.add(url)
        write_requests(driver,file_path,existing_urls)
    else:
        write_requests(driver,file_path,existing_urls)
        

def write_requests(driver, file_path, existing_urls):
    with open(file_path, "a") as file:
            time.sleep(3)
            iframe = driver.find_element(By.XPATH, "//iframe[@id='iframe-embed']")
            driver.switch_to.frame(iframe)
            driver.find_element(By.XPATH,"//div[@aria-label='Start Playback']").click()
            duration = 600
            start_time = time.time()
            while time.time() - start_time < duration:
                for request in driver.requests:
                    if request.response and request.url not in existing_urls:
                        file.write(
                            f"{request.url} {request.response.status_code} {request.response.headers['Content-Type']}\n"
                        )
                        print(f"{request.url} {request.response.status_code} {request.response.headers['Content-Type']}")
                        existing_urls.add(request.url)
            driver.quit() 
