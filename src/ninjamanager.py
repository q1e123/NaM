import time
import sys
from driver_tor import DriverTor
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

def farm(link, xpath, energy_cost):
        while get_WE() > energy_cost:
                driver.goto(link)
                driver.click(xpath)

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

def _clicknwait(xpath):
        driver.click(xpath)
        time.sleep(3.5)

def _skip():

        _clicknwait('/html/body/div[1]/main/div[2]/div[1]/div/div[4]/div/div[3]/div/div/div[2]/div[2]/span')
        _clicknwait('/html/body/div[1]/main/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/span')

def make_orders():
        orders = dict()
        orders['AF'] = attack_friends
        orders['AR'] = attack_random

        orders['FGF'] = gold_frozen
        orders['FGD'] = gold_deadshore
        orders['FGT'] = gold_tsunade
        orders['FGP'] = gold_panda

        orders['Dice'] = material_dice
        orders['Ink']  = material_ink
        orders['Web']  = material_web
        orders['Wood'] = material_wood
        return orders

def routine(filename):
        order_dict = make_orders()

        with open(filename) as file:
                for line in file:
                        user, passwd, orders = line.split()
                        if len(orders)<1:
                                continue

                        login(user,passwd)
                        print("Logged to " + user)
                        order_list = orders.split(';')

                        setup_attacks()
                        for order in order_list:
                                print("Started doing " + order)
                                order_dict[order]()
                                print("Stopped doing " + order)
                        driver.newID()

        driver.driver.quit()

def create_accounts(ammount, filename):
        file = open(filename, 'a')
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


if '-h' in sys.argv:
        headless = True
else:
        headless = False

driver = DriverTor(headless=headless)

if '-r' in sys.argv:
        i = sys.argv.index('-r')
        routine(sys.argv[i+1])


if '-ca' in sys.argv:
        i = sys.argv.index('-ca')
        n = sys.argv[i+1]
        fn = sys.argv[i+2]
        create_accounts(n,fn)