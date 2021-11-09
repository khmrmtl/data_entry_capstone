from time import sleep
from selenium import webdriver

CHROME_DRIVER_PATH = "C:\Development\chromedriver"
WEBSITE_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22' \
               'usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-' \
               '122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22' \
               'isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%' \
               '7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%' \
               '7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%' \
               '22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%' \
               '22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3' \
               'A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
GOOGLE_FORMS_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSdcjNpsMh6PYr4fPRfq-6sZRuOICdwW_uYUCSeyTillSid5LQ/viewform?usp=sf_link'

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(url=WEBSITE_LINK)
sleep(5)

# use to scroll the page
# element = driver.find_element_by_xpath('/html/body')
# element.send_keys(Keys.NULL)
# element.click()
# listing = driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]')
# listing.send_keys(Keys.NULL)
# for i in range(0, 200):
#     print("baba")
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;", element)
#     element.send_keys(Keys.DOWN)

links = driver.find_elements_by_css_selector('.list-card-top a.list-card-link')
links = [link.get_attribute('href') for link in links]

addresses = driver.find_elements_by_css_selector('li article a address.list-card-addr')
addresses = [address.text for address in addresses]

prices = driver.find_elements_by_css_selector("div.list-card-price")
prices = [price.text for price in prices]


driver.get(GOOGLE_FORMS_LINK)
sleep(2)
for i in range(0, len(addresses)-1):
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[i])
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[i])
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[i])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit.click()
    sleep(.5)
    submit_again = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_again.click()
    sleep(.5)

