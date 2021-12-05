import os, random, pyfiglet
logo = pyfiglet.figlet_format("Screaze Tools")
print(logo)
print("[$] Screaze Tools v1.5 by @blackscreaze")
print("[1] Webhook Discord Spam")
print("[2] Discord token checker")
print("[3] Discord Nitro Gen/Checker")
print("[4] Discord QR Code Token Grabber")
print("[5] Credits")
print("[6] Discord Token Generator")
print("[7] Spotify Account Generator")
print("[X] Exit")
blackscreaze = input("[?] Choose option > ")
if blackscreaze == "1":
	os.system('clear')
	os.system('python webhooks.py')

if blackscreaze == "2":
	os.system("clear")
	os.system("python checker.py")
	
if blackscreaze == "3":
	os.system("clear")
	os.system("python nitro.py")

if blackscreaze == "4":
	os.system("clear")
	os.system("python qr.py")

if blackscreaze == "5":
	os.system("clear")
	os.system("python credits.py")

if blackscreaze == "X":
	os.system("clear")
	logo2 = pyfiglet.figlet_format("Screaze Tools")
	print(logo2)
	print("[$] Goodbye ;)")
	exit()
if blackscreaze == "6":
	os.system("clear")
	os.system("python tokengen.py")

if blackscreaze == "7":
	os.system("clear")
	os.system("python spotifygen.py")