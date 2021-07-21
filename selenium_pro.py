
from selenium import webdriver

import pandas as pd

def stringsnum(args):
    seq = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }
    return seq.get(args, "nothing")


page=1
while page<=5:
    options = webdriver.ChromeOptions()
    options.add_argument("start-minimized")
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

    url="https://www.justdial.com/Aurangabad-Maharashtra/Orthopaedic-Doctors-in-Aurangabad-HO/nct-10345039/page-"+str(page)
    driver.get(url)
    storeDetails = driver.find_elements_by_class_name('store-details')

    nameList = []
    addressList = []
    numbersList = []
    for i in range(len(storeDetails)):
        name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
        address = storeDetails[i].find_element_by_class_name('cont_sw_addr').text
        contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
        myList = []
        for j in range(len(contactList)):
            strs = contactList[j].get_attribute('class').split("-")[1]
            myList.append(stringsnum(strs))

        nameList.append(name)
        addressList.append(address)
        numbersList.append("".join(myList))

    data = {'Company Name': nameList,
        'Address': addressList,
        'Phone': numbersList}
    df = pd.DataFrame(data)
    print(df)
    print("-"*100)
    page=page+1
    driver.quit()

