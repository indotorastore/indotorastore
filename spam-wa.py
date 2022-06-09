import requests, os

url_api_spam_wa= "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa">

os.system("clear")
os.system("figlet Spam-wa")
print("[-] Creator :Diony")
print("[-] Youtube : diony")
nomor = input("\n[?] input nomor  : ")
jumlah = input("[?] input jumlah : ")
print()
data = {
"nomor":nomor
}
for free_tutorial in range(int(jumlah)):
        sanz = requests.get(url_api_spam_wa, para>
if "Berhasil ngab ! .. Subrek Yt FREE TUTORIAL." >
        print("[+] Berhasil Ngab")
else:
        print("[!] Gagal Ngab")
