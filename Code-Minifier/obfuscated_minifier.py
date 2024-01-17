# Take the encryption method from the website = https://pyobfuscate.com/minifier
# Time : Wednesday, January 17, 2024 23:26:47
# Platform : Windows-AMD64
_C='https://pyobfuscate.com/minifier'
_B=False
_A=True
import importlib,requests as r
from bs4 import BeautifulSoup as bs
import os,sys,datetime,time,platform
k='\x1b[1;33m'
a='\x1b[1;30m'
m='\x1b[1;31m'
h='\x1b[1;32m'
p='\x1b[1;37m'
b='\x1b[1;34m'
v='\x1b[1;35m'
u='\x1b[1;36m'
j='\x1b[1;38;5;202m'
def clear():
	if'linux'in sys.platform.lower():os.system('clear')
	elif'win'in sys.platform.lower():os.system('cls')
def logo():A='Ryougaa and Denventa';print('%s      _____  .__       .__  _____.__              '%p);print('%s     /     \\ |__| ____ |__|/ ____\\__| ___________ '%h);print('%s    /  \\ /  \\|  |/    \\|  \\   __\\|  |/ __ \\_  __ \\/'%p);print('%s   /    Y    \\  |   |  \\  ||  |  |  \\  ___/|  | \\/'%h);print('%s   \\____|__  /__|___|  /__||__|  |__|\\___  >__|   '%p);print('%s           \\/        \\/                  \\/       %s'%(h,p))
try:clear();importlib.import_module('requests');requests_module_installed=_A
except ImportError:requests_module_installed=_B
try:clear();importlib.import_module('Crypto');crypto_module_installed=_A
except ImportError:crypto_module_installed=_B
if not crypto_module_installed:print(f"{h}[{a}•{h}] {p}Modul Crypto   : ({a}pycryptodome{p}) belum terinstall.");print(f"{h}[{a}•{h}] {p}Ketik perintah : pip install {a}pycryptodome")
try:importlib.import_module('bs4');bs4_module_installed=_A
except ImportError:bs4_module_installed=_B
if not crypto_module_installed or not requests_module_installed or not bs4_module_installed:
	print(f"{h}[{a}•{h}] {p}Beberapa modul belum terinstal. Anda perlu menginstal modul-modul berikut {a}:")
	if not requests_module_installed:print(f"  {a}- {p}pycryptodome (Crypto)");print(f"  {a}- {p}requests");print(f"  {a}- {p}bs4 (Beautiful Soup)")
	print(f"{h}[{a}•{h}] {p}Ketik perintah: pip install {a}pycryptodome bs4 requests {p}")
else:
	if'linux'in platform.system().lower():os.system('clear')
	elif'win'in platform.system().lower():os.system('cls')
	Take_the_encryption=_C;current_time=datetime.datetime.now();current_time_str=current_time.strftime('%A, %B %d, %Y %H:%M:%S');logo();print('');print('Python - Platform Version : ');print(__import__('sys').version);input_file=input(f"\n{h}[{a}•{h}] {p}Masukkan nama file Input {a}: {p}")
	if not input_file:print(f"{m}[{a}!{m}] {p}File '{input_file}' tidak ditemukan.");exit()
	elif not input_file.endswith('.py'):print(f"{m}[{a}!{m}] {p}File harus memiliki ekstensi .py {p}");exit();input_text=None
	try:
		with open(input_file,'r',encoding='utf-8')as file:input_text=file.read()
	except FileNotFoundError:print(f"{p}File '{input_file}' tidak ditemukan.");input_text=None
	if input_text:
		response=r.post(_C,data={'input_text':input_text});source=bs(response.text,'html.parser');result=source.find('textarea',{'id':'myTextarea2'})
		while _A:
			output_file=input(f"{h}[{a}•{h}] {p}Masukkan nama file Output {a}: {p}")
			if not output_file:print(f"{m}[{a}!{m}] {p}Isi dengan benar {m}! {p}");exit()
			elif not output_file.endswith('.py'):print(f"{m}[{a}!{m}] {p}File output harus memiliki ekstensi .py {p}");exit()
			else:break
		if result:
			encrypted_code=result.text
			with open(output_file,'w',encoding='utf-8')as file:file.write(f"# Take the encryption method from the website = {Take_the_encryption}\n");file.write(f"# Time : {current_time_str}\n");file.write(f"# Platform : {platform.system()}-{platform.machine()}\n"+encrypted_code)
			print(f"{h}[{a}•{h}] {p}Berhasil, file {input_file} tersimpan di {a}: {output_file} {p}")
		else:print(f"{m}[{a}!{m}] {p}Tidak dapat menemukan kode Obfuscate.")
	else:print(f"{h}[{k}+{h}] {p}Proses Obfuscate dibatalkan karena file Input tidak ditemukan.")