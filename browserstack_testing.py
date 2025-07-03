from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

USERNAME = "spurthimadhukar_OAS5Yg"
ACCESS_KEY = "ZasyiSVLyLrdBDujbFTp"

capabilities = [
    {
        'os': 'Windows',
        'os_version': '11',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'name': 'Windows Chrome Test',
    },
    {
        'os': 'OS X',
        'os_version': 'Monterey',
        'browser': 'Safari',
        'browser_version': 'latest',
        'name': 'macOS Safari Test',
    },
    {
        'device': 'Samsung Galaxy S22',
        'real_mobile': 'true',
        'os_version': '12.0',
        'name': 'Android Mobile Test',
    },
    {
        'device': 'iPhone 14',
        'real_mobile': 'true',
        'os_version': '16',
        'name': 'iOS Mobile Test',
    },
    {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Windows Firefox Test',
    }
]

def run_test(cap):
    cap['browserstack.debug'] = True
    url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
    driver = webdriver.Remote(command_executor=url, desired_capabilities=cap)
    
    try:
        driver.get("https://example.com")
        print(f"{cap['name']} - Title: {driver.title}")
    except Exception as e:
        print(f"{cap['name']} - Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_test, capabilities)
