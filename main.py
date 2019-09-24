from selenium import webdriver
import argparse
from selenium.webdriver.chrome.options import Options

def open(i):
    i = '+'.join(i.split())
    url = "https://www.youtube.com/results?search_query="+i
    return url

parser = argparse.ArgumentParser()
parser.add_argument('o', help="Enter Song name", type=str)
args = parser.parse_args()

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get(open(args.o))
type(browser)
linkElem = browser.find_element_by_id('thumbnail')
type(linkElem)
linkElem.click()
print(browser.current_url)
browser.set_network_conditions(
    offline=False,
    latency=5,
    download_throughput= 40000,  
    upload_throughput= 32000)
browser.get(browser.current_url)
linkElem = browser.find_element_by_id('movie_player')
type(linkElem)
linkElem.click()
print("completed")
browser.save_screenshot("screenshot.png")
