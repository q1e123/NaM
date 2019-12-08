import time
import sys
from selenium.webdriver.common.keys import Keys

from driver_tor import DriverTor
from driver_ff import DriverFirefox
from guerilla_mail import GuerrillaMail

import utils

def login(username, password):
	driver.goto("https://www.ninjamanager.com/account/login")
	driver.send_keys('//*[@id="input-login"]',username)
	driver.send_keys('//*[@id="input-password"]',password)
	driver.click('//*[@id="login-nm-button"]')

	time.sleep(5)

def setup_attacks():
	driver.goto('https://www.ninjamanager.com/arena')
	#settings
	driver.click('//*[@id="content"]/div[2]/div/div/div[2]/div[1]/div/div[3]/div[1]/span')
	#skip
	if not driver.is_selected('//*[@id="arena-settings"]/div[2]/div/label/input'):
		driver.click('//*[@id="arena-settings"]/div[2]/div/label/input')
	#save
	driver.click('//*[@id="save-settings"]/span')
	time.sleep(3)

def attack_friends():
	driver.goto('https://www.ninjamanager.com/arena')
	driver.click('//*[@id="left-sidebar-menu"]/div[1]/a[3]/i')
	time.sleep(2)

	for _ in range(5):
		if get_AE() < 5:
			return
		i = 1
		while get_AE() > 5:
			try:
				xpath = '//*[@id="friends-list"]/div[%d]/div[2]/div[1]'%i
				driver.click(xpath)
				i+=1
				time.sleep(2)
			except:
				try:
					#close
					driver.click('//*[@id="modal-sidebar"]/div/div[5]/div/div[2]/span')
				except:
					#End
					break

def get_AE():
	return int(driver.get_value('//*[@id="header-team"]/div[5]/div[2]/span[1]','innerText'))

def attack_random():
	driver.goto('https://www.ninjamanager.com/arena')

	i=1
	while get_AE() > 4:
		try:
			xpath = '//*[@id="content"]/div[2]/div/div/div[2]/div[2]/div[2]/div[%d]/div[9]/span' %i
			driver.click(xpath)
			i+=1
			time.sleep(2)
		except:
			try:
				driver.click('//*[@id="site-container"]/main/div[2]/div[5]/div[2]/div[3]/div/div[2]/span')
			except:
				i = 1

def logoff():
	driver.click('//*[@id="site-container"]/header/div[1]/div/div[2]/div[2]/a[3]/div')

def get_WE():
	return int(driver.get_value('//*[@id="header-team"]/div[6]/div[2]/span[1]','innerText'))

def farm_noref(xpath,energy_cost):
	while get_WE() > energy_cost:
		driver.click(xpath)
		driver.click('//*[@id="modal-battle"]/div/div[4]/div/div[1]/div/div/div[2]/div[1]/span')
		driver.click('//*[@id="modal-battle"]/div/div[4]/div/div[3]/div/div/div[2]/div[2]/span')
		time.sleep(1)

def mission(link,xpath):
	driver.goto(link)
	driver.click(xpath)

def farm(link, xpath, energy_cost):
	while get_WE() > energy_cost:
		mission(link,xpath)


def gold_frozen():
	farm('https://www.ninjamanager.com/world/area/frozen-island',
	     '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]/span', 4)

def gold_deadshore():
	farm('https://www.ninjamanager.com/world/area/island-turtle',
	     '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]/span', 6)

def gold_tsunade():
	farm('https://www.ninjamanager.com/world/area/island-turtle',
	     '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]/span', 7)

def gold_panda():
	farm('https://www.ninjamanager.com/world/area/immortal-beast-cavern',
	     '//*[@id="content"]/div[2]/div[2]/div/div[3]/div[4]/div/div[4]/div/div[2]/span', 5)

def material_dice():
	farm('https://www.ninjamanager.com/world/area/blood-prison',
	     '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]/span', 5)

def material_ink():
	farm('https://www.ninjamanager.com/world/area/forbidden-temple-outer',
	     '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[33]/div/div[4]/div/div[2]/span', 6)

def material_web():
	farm('https://www.ninjamanager.com/world/area/ruins-of-roran',
	     '//*[@id="content"]/div[6]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]/span', 5)

def material_wood():
	farm('https://www.ninjamanager.com/world/area/anbu-hideout',
	     '//*[@id="content"]/div[3]/div/div/div[3]/div[3]/div/div[4]/div/div[2]/span', 6)

def tog_zabuza():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[8]/div[2]/div/div/div[2]/div/div[4]/div/div[2]/span', 6)

def tog_zabuza2():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[8]/div[2]/div/div/div[3]/div[1]/div[4]/div/div[2]/span', 6)

def tog_jinin():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[2]/div[2]/div/div[3]/div[2]/div/div[4]/div/div[2]/span', 6)

def tog_jinin2():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[2]/div[2]/div/div[3]/div[3]/div/div[4]/div/div[2]/span', 6)

def tog_jinpachi():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[4]/div/div[2]/span', 6)

def tog_ameyuri():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[4]/div[2]/div/div/div[2]/div[1]/div[4]/div/div[2]/span', 6)

def tog_kushimaru():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[5]/div[2]/div/div/div[2]/div/div[4]/div/div[2]/span', 6)

def tog_kushimaru2():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[5]/div[2]/div/div/div[3]/div/div[4]/div/div[2]/span', 6)

def tog_fuguki():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[6]/div[2]/div/div/div[2]/div[1]/div[4]/div/div[2]/span', 6)

def tog_mangestu():
	farm('https://www.ninjamanager.com/world/area/tower-of-god',
	     '//*[@id="content"]/div[7]/div[2]/div/div/div[2]/div[1]/div[4]/div/div[2]/span', 6)

def lw_demonic_flute():
	farm('https://www.ninjamanager.com/world/area/ryuichi-cave',
	     '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]/span', 6)

def daily_recipe():
	driver.goto("https://www.ninjamanager.com/forge")
	driver.click('//*[@id="daily-recipe-button"]/span')
	driver.click('//*[@id="craft-button-learn"]/span')

def daily_wheel_material():
	driver.goto("https://www.ninjamanager.com/forge")
	driver.click('//*[@id="start-daily-reward"]/span')
	time.sleep(10)
	driver.click('//*[@id="content"]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/span')

def daily_wheel_gold():
	driver.goto("https://www.ninjamanager.com/forge")
	driver.click('//*[@id="start-daily-reward"]/span')
	time.sleep(10)
	driver.click('//*[@id="content"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/span')

def material_iron_snow():
	farm('https://www.ninjamanager.com/world/area/snow-country', 
		 '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]/span', 4)


def _clicknwait(xpath):
	driver.click(xpath)
	time.sleep(3.5)

def logout():
	driver.goto('https://www.ninjamanager.com/')
	driver.click('//*[@id="site-container"]/header/div[1]/div/div[2]/div[2]/a[3]/div/span')

def material_dark_chakra_eel():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[4]/div/div[2]',5)

def material_granite():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]',5)

def material_serpent_scale():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]',5)

def material_lava():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]',5)

def material_quicklime():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[4]/div/div[4]/div/div[2]',5)

def lw_firestorm_staff():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]',5)

def lw_occult_grimoire():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]',5)

def material_uchiha_crest():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[3]/div[2]/div[4]/div/div[2]',5)

def material_serpent_soul():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[6]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]',5)
	
def material_cursed_feather():
	farm('https://www.ninjamanager.com/world/area/moryo-shrine',
		 '//*[@id="content"]/div[6]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]',5)
	

def make_orders():
	orders = dict()
	# Arena
	orders['AF'] = attack_friends
	orders['AR'] = attack_random

	# Gold
	orders['FGF'] = gold_frozen
	orders['FGD'] = gold_deadshore
	orders['FGT'] = gold_tsunade
	orders['FGP'] = gold_panda

	# Material
	orders['Dice']				= material_dice
	orders['Ink']  				= material_ink
	orders['Web']				= material_web
	orders['Wood']				= material_wood
	orders['IronS']				= material_iron_snow
	orders['Dark_chakra_eel']	= material_dark_chakra_eel
	orders['Granite']			= material_granite
	orders['Serpent_scale']		= material_serpent_scale
	orders['Serpent_soul']		= material_serpent_soul
	orders['Lava']				= material_lava
	orders['Quicklime']			= material_quicklime
	orders['Uchiha_crest']		= material_uchiha_crest
	orders['Cursed_feather']	= material_cursed_feather

	# TOG
	orders['Zabuza']    	= tog_zabuza
	orders['Zabuza2']  		= tog_zabuza2
	orders['Jinin']     	= tog_jinin
	orders['Jinin2']    	= tog_jinin2
	orders['Jinpachi']  	= tog_jinpachi
	orders['Ameyuri']   	= tog_ameyuri
	orders['Kushimaru'] 	= tog_kushimaru
	orders['Kushimaru2'] 	= tog_kushimaru2
	orders['Fuguki']    	= tog_fuguki
	orders['Mangestu']  	= tog_mangestu

	# LWs
	orders['Demonic_flute'] 	= lw_demonic_flute
	orders['Firestorm_staff'] 	= lw_firestorm_staff
	orders['Occult_grimoire'] 	= lw_occult_grimoire

	# Progress
	orders['Intro']  = prg_intro
	orders['Snow']   = prg_snow
	orders['Frozen'] = prg_frozen
	
	# Other
	orders['Friends'] 	= add_friends
	orders['Recipe'] 	= daily_recipe
	orders['WheelM'] 	= daily_wheel_material
	orders['WheelG'] 	= daily_wheel_gold

	return orders

def kill_acc(driver):
	if isinstance(driver,DriverTor):
		driver.newID()
		return driver
	else:
		logoff()
		return driver


def routine(filename):
	global driver
	order_dict = make_orders()

	with open(filename) as file:
		for line in file:
			try:
				user, passwd, orders = line.split()
			except:
				print("Wrong format")
				continue
			login(user,passwd)
			print("Logged to " + user)
			
			order_list = orders.split(';')

			try:
				if get_AE() < 5:
					driver = kill_acc(driver)
					continue

				if get_WE() < 5:
					driver = kill_acc(driver)
					continue
				if 'AR' in order_list or 'AF' in order_list:
					setup_attacks()
				for order in order_list:
					print("Started doing " + order)
					order_dict[order]()
					print("Stopped doing " + order)
			except:
				driver = kill_acc(driver)
				print('!!! ERROR !!! ')
				continue
			
			
			driver = kill_acc(driver)
	
	driver.driver.quit()

def create_accounts(ammount, filename):
	file = open(filename, 'a+')
	file.write('\n')
	for _ in range(ammount):
		user = utils.random_string_alphanum()
		passw = utils.random_string_alphanum()
		email = user + '@sharklasers.com'

		driver.goto('https://www.ninjamanager.com/account/register')

		usr_tb = '//*[@id="input-email"]'
		passw_tb = '//*[@id="input-password"]'
		cpassw_tb = '//*[@id="input-password-confirm"]'

		driver.send_keys(usr_tb, email)
		driver.send_keys(passw_tb, passw)
		driver.send_keys(cpassw_tb, passw)

		btn = '//*[@id="register-nm-button"]'

		driver.click(btn)
		time.sleep(2)
		GuerrillaMail.goto_site(driver)
		GuerrillaMail.put_user(driver,user)
		GuerrillaMail.find_email(driver, 'NinjaManager', 2)
		time.sleep(4)
		driver.click('//*[@id="display_email"]/div/div[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a')
		time.sleep(1)

		file.write(email+  " " + passw+ '\n')
		driver.newID()

def _skip():
	_clicknwait('/html/body/div[1]/main/div[2]/div[1]/div/div[4]/div/div[1]/div/div/div[2]/div[1]/span')
	_clicknwait('/html/body/div[1]/main/div[2]/div[1]/div/div[4]/div/div[3]/div/div/div[2]/div[2]/span')

def add_friends():
	friends = list()
	with open('nm_friends') as file:
		for line in file:
			friends.append(line)
	driver.click('//*[@id="left-sidebar-menu"]/div[1]/a[3]/i')
	time.sleep(3)
	for friend in friends:
		driver.click('/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/input')
		driver.send_keys('/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/input', Keys.CONTROL + 'A')
		driver.send_keys('/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/input', Keys.BACKSPACE)
		driver.send_keys('/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/input', friend)
		driver.send_keys('/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/input', Keys.RETURN)		
		time.sleep(3)
		driver.click('/html/body/div[1]/main/div[2]/div[3]/div/div[4]/div/div[2]/div[1]/div[2]/div/div/div[3]/div')
		time.sleep(2)

def prg_snow():
	driver.goto('https://www.ninjamanager.com/world/village/hidden-leaf')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span')
	
	link = 'https://www.ninjamanager.com/world/area/snow-country'
	mission(link, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[3]/div/div/div[2]/div[3]/div/div[4]/div/div[2]')
	mission(link, '/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[3]/div/div/div[2]/div[4]/div[2]/div[4]/div/div[2]')

	mission(link, '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]')

	mission(link, '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]')

def prg_frozen():
	link = 'https://www.ninjamanager.com/world/area/frozen-island'

	mission(link, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]')
	
	mission(link, '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[3]/div[2]/div/div[2]/div[4]/div/div[4]/div/div[2]')


	mission(link, '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[4]/div[2]/div/div[2]/div[4]/div[2]/div[4]/div/div[2]')

	mission(link, '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[2]/div/div[4]/div/div[2]')
	mission(link, '//*[@id="content"]/div[5]/div[2]/div/div[2]/div[3]/div/div[4]/div/div[2]')
	time.sleep(3)
	_skip()

def prg_intro():
	# continue
	driver.goto('https://www.ninjamanager.com/intro')
	time.sleep(2)
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/span')

	# select diff
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div/span')
	# select starter
	print('Selecting starter')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div/span')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[3]/div/div[2]/span')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div[4]/a/div/span')
	
	# intro
	print('Doing intro mission')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/span')
	_skip()
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div/div[4]/div/div/span')
	_skip()
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div/div/span')
	_skip()

	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/span')
	
	print('Set up team')
	# buy team
	driver.goto('https://www.ninjamanager.com/world/village/hidden-leaf/ninja-shop')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[4]/div[3]/div[7]/div[2]/div[3]/div/div[2]/span')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[3]/div/div[3]/div[1]/span')
	
	driver.goto('https://www.ninjamanager.com/world/village/hidden-leaf/ninja-shop')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[4]/div[3]/div[16]/div[2]/div[3]/div/div[2]/span')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[3]/div/div[2]/div/div[2]/div[4]')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[3]/div/div[3]/div[1]/span')

	# Set team
	driver.goto('https://www.ninjamanager.com/myteam')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/span')
	for _ in range(16):
		driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/i[2]')
	_clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/span')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[5]/div[3]/div[2]/div[2]/div/div[1]/div[2]/span')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[5]/div[3]/div[2]/div[2]/div/div[2]/div[2]/span')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[5]/div[3]/div[1]/div[4]/span')
	_clicknwait('/html/body/div[1]/header/div[2]/div[2]/div[2]/span')
	driver.click('/html/body/div[1]/main/div[2]/div[2]/div/div[3]/div/div[4]/div[2]/div[2]/div/span')
	driver.click('/html/body/div[1]/header/div[2]/div[2]/div[1]/div[2]/div[5]/div[1]')
	driver.click('/html/body/div[1]/main/div[2]/div[2]/div/div[3]/div/div[4]/div[3]/div[2]/div/span')
	driver.click('/html/body/div[1]/header/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]')
	driver.click('/html/body/div[1]/main/div[2]/div[2]/div/div[3]/div/div[4]/div[4]/div[2]/div/span')
	driver.click('/html/body/div[1]/header/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]')
	_clicknwait('/html/body/div[1]/main/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/span')

	print('Doing snow')
	prg_snow()

	# arena
	print('Doing Arena')
	driver.goto('https://www.ninjamanager.com/world/village/hidden-leaf')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span/b')
	
	setup_attacks()
	

	attack_friends()
	attack_random()

	driver.goto('https://www.ninjamanager.com/world/village/hidden-leaf')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span')
	driver.goto('https://www.ninjamanager.com/world/village/hidden-leaf')
	driver.click('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span')
	
	print('Doing Frozen')
	prg_frozen()
	gold_frozen()

if '-h' in sys.argv:
	headless = True
else:
	headless = False


driver = DriverTor(headless)


if '-r' in sys.argv:
	i = sys.argv.index('-r')
	routine(sys.argv[i+1])

if '-ca' in sys.argv:
	i = sys.argv.index('-ca')
	n = int(sys.argv[i+1])
	fn = sys.argv[i+2]
	create_accounts(n,fn)

driver = None

if '-f' in sys.argv:
	driver = DriverFirefox(headless)
	i = sys.argv.index('-f')
	routine(sys.argv[i+1])
