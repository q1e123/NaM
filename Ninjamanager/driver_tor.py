from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)

profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)

class DriverTor:
	def __init__(self,headless = False):
		self.headless = headless
		options.headless = headless
		self.driver = webdriver.Firefox(options=options, firefox_profile=profile)

	def newID(self):
		self.driver.quit()
		self.driver = None
		options = Options()
		options.headless = self.headless
		profile = webdriver.FirefoxProfile()
		profile.set_preference('network.proxy.type', 1)
		profile.set_preference('network.proxy.socks', '127.0.0.1')
		profile.set_preference('network.proxy.socks_port', 9050)

		profile.set_preference("browser.cache.disk.enable", False)
		profile.set_preference("browser.cache.memory.enable", False)
		profile.set_preference("browser.cache.offline.enable", False)
		profile.set_preference("network.http.use-cache", False)
		self.driver = webdriver.Firefox(options=options, firefox_profile=profile)

	def goto(self,site):
		self.driver.get(site)

	def click(self,xpath):
		elem = self._find(xpath)
		elem.click()

	def send_keys(self, xpath, keys):
		elem = self._find(xpath)
		elem.send_keys(keys)

	def get_value(self,xpath,attribute):
		elem = self._find(xpath)
		return elem.get_attribute(attribute)

	def is_selected(self, xpath):
		elem = self._find(xpath)
		return elem.is_selected()

	def refresh(self):
		self.driver.refresh()

	def _find(self, xpath):
		return self.driver.find_element_by_xpath(xpath)
