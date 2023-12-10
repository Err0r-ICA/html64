# -*- coding: utf-8 -*-
#usr/bin/env/python
#Err0r_HB
#Cyb3r Drag0nz Team

import base64
import os
import platform
import time
import pyfiglet

red = "\033[1;91m"
green = "\033[1;92m"
cyan = "\033[1;96m"

# Clear the console screen based on the operating system 
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Print the banner
banner = '''\033[38;5;197m              '##::::'##:'########:'##::::'##:'##:::::::
               ##:::: ##:... ##..:: ###::'###: ##:::::::
               ##:::: ##:::: ##:::: ####'####: ##:::::::
               #########:::: ##:::: ## ### ##: ##:::::::
               ##.... ##:::: ##:::: ##. #: ##: ##:::::::
               ##:::: ##:::: ##:::: ##:.:: ##: ##:::::::
               ##:::: ##:::: ##:::: ##:::: ##: ########:
              \033[38;5;202m...:::::..:::::..:::::..:::::..::........::
	
\033[38;5;092m                           Coded By Err0r_HB
'''

# Print the progress bar with sleep in between 
def main():
    clear()
    for progress in range(0, 101, 10):
        clear()
        print(f"{cyan}[{red}{progress}%{cyan}]{green}{'■' * (progress // 10)}")
        time.sleep(0.5)

    clear()
    print(banner)

    # Get the input HTML file
    html = input(f'{cyan}[!]\033[38;5;021m Enter your html file {cyan}>>> {red}')
    code = open(html, 'r', encoding='UTF-8').read()
    text = code.encode('utf-8')
    bsen = base64.b64encode(text).decode('utf-8')
    html_encoding = f"""<!-- Encoding By Err0r_HB | Telegram : t.me/Cyb3r_Drag0nz -->
<!-- GitHub :  https://github.com/Err0r-ICA -->

<script type='text/javascript'>document.documentElement.innerHTML=atob('{bsen}');</script>
"""
    path = os.getcwd()
    output_file = f"{html.replace('.html', '')}_en.html"
    open(output_file, 'w').write(html_encoding)

    # Print the progress bar again with sleep in between
    for progress in range(0, 101, 10):
        clear()
        print(f"{cyan}[{red}{progress}%{cyan}]{green}{'■' * (progress // 10)}")
        time.sleep(1)

    clear()
    print(banner)
    print(f"\n{cyan}[+]{red} The file was encrypted and saved as:‍{green} {os.path.join(path, output_file)}\n")

main()