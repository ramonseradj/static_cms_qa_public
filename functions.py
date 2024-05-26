from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, requests, xmltodict

def get_datalayer(url: str, index: int = 0, event: str = "None", navigation_steps: list = None, wait_for_cmp: bool = True, cmp_selector: str = "#cmpwelcomebtncustom"):
    """
    Opens a webpage and returns a specific DataLayer object.
    The object can be selected either by index or by event-name.
    """
    # Set up the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'excludeSwitches', 
        ['enable-logging']
        )
    driver = webdriver.Chrome()

    driver.get(url)
    time.sleep(2)
    if wait_for_cmp:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, cmp_selector)))

    # Optional navigation through page
    if navigation_steps is not None:
        for step in navigation_steps:
            sel = step["css-selector"]
            el = WebDriverWait(driver, step["wait"]).until(EC.visibility_of_element_located((By.CSS_SELECTOR, sel)))
            if step["action"] == "click":
                el.click()
                print("clicked")
            elif step["action"] == "scroll":
                el.location_once_scrolled_into_view
                print("scrolled")
    data = {}
    if event == "None":
        dataLayer = driver.execute_script(f"return window.dataLayer[{index}];")
        data. = dataLayer
    else:
        dataLayer = driver.execute_script("return window.dataLayer;")
        occ = []
        for ob in dataLayer:
            if "event" in ob and ob["event"] == event:
                occ.append(ob)
        data = occ[index]
    return data[index]

def get_sitemap(url: string, limit = None):
    """
    Returns list with all links, that are existend in sitemap.xml file
    """
    res = requests.get(url)
    raw = xmltodict.parse(res.text)
    data = [r["loc"] for r in raw["urlset"]["url"]]
    if limit:
        return data[:limit]
    else:
        return data

def check_datalayer_object(object, values):
    missing_values = []
    for key in values:
        if key not in object:
            missing_values.append(key)
    return missing_values
