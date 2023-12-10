import base64,os,platform,time,pyfiglet
red='\x1b[1;91m'
green='\x1b[1;92m'
cyan='\x1b[1;96m'
def clear():
	if platform.system()=='Windows':os.system('cls')
	else:os.system('clear')
banner="\x1b[38;5;197m              '##::::'##:'########:'##::::'##:'##:::::::\n               ##:::: ##:... ##..:: ###::'###: ##:::::::\n               ##:::: ##:::: ##:::: ####'####: ##:::::::\n               #########:::: ##:::: ## ### ##: ##:::::::\n               ##.... ##:::: ##:::: ##. #: ##: ##:::::::\n               ##:::: ##:::: ##:::: ##:.:: ##: ##:::::::\n               ##:::: ##:::: ##:::: ##:::: ##: ########:\n              \x1b[38;5;202m...:::::..:::::..:::::..:::::..::........::\n\t\n\x1b[38;5;092m                           Coded By Err0r_HB\n"
def main():
	D='utf-8';clear()
	for A in range(0,101,10):clear();print(f"{cyan}[{red}{A}%{cyan}]{green}{'■'*(A//10)}");time.sleep(.5)
	clear();print(banner);B=input(f"{cyan}[!][38;5;021m Enter your html file {cyan}>>> {red}");E=open(B,'r',encoding='UTF-8').read();F=E.encode(D);G=base64.b64encode(F).decode(D);H=f"<!-- Encoding By Err0r_HB | Telegram : t.me/Cyb3r_Drag0nz -->\n<!-- GitHub :  https://github.com/Err0r-ICA -->\n\n<script type='text/javascript'>document.documentElement.innerHTML=atob('{G}');</script>\n";I=os.getcwd();C=f"{B.replace('.html','')}_en.html";open(C,'w').write(H)
	for A in range(0,101,10):clear();print(f"{cyan}[{red}{A}%{cyan}]{green}{'■'*(A//10)}");time.sleep(1)
	clear();print(banner);print(f"\n{cyan}[+]{red} The file was encrypted and saved as:‍{green} {os.path.join(I,C)}\n")
main()
