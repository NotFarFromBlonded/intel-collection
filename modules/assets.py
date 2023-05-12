from seleniumwire import webdriver
from selenium.webdriver.common.by import By

def assets(driver, url, directory):
    file_path = f"{directory}/assets.txt"
    with open(file_path, "w") as file:
        file.write(f"linking site url: {url}\n")
        print(f"linking site url: {url}")
        hosting_site_url = driver.find_element(By.CSS_SELECTOR, "iframe#iframe-embed").get_attribute('src')
        file.write(f"hosting site url: {hosting_site_url}\n")
        print(f"hosting site url: {hosting_site_url}")
        script_tags = driver.find_element(By.TAG_NAME, "body").find_elements(By.CSS_SELECTOR, "script[src]")
        link_tags = driver.find_element(By.TAG_NAME, "head").find_elements(By.CSS_SELECTOR, "link[href]")
        script_head_tags = driver.find_element(By.TAG_NAME, "head").find_elements(By.CSS_SELECTOR, "script[src]")
        for script_tag in script_tags:
            src = script_tag.get_attribute("src")
            file.write(f"{src}\n")
            print(src)
        for link_tag in link_tags:
            href = link_tag.get_attribute("href")
            file.write(f"{href}\n")
            print(href)
        for script_head_tag in script_head_tags:
            src = script_head_tag.get_attribute("src")
            file.write(f"{src}\n")
            print(src)
        
