""""
This tool was made by CodingLive#0001
For educational purpose only.
I'm not responsible for any damage
"""
from discord.ext import commands
import json
import discord
import time
import pyfiglet
import time
import os

ascii_banner = pyfiglet.figlet_format("Discord DM Spam")
print(ascii_banner)

a = input("Do you know how to get the user token? (y/n) ")
if a == "y":
    pass
elif a == "n":
    print(f""""
    1. Open your browser
    2. Open the deveoloper menu (right click; inspect)
    3. Open the 'Network' Tab
    4. Send a message in the server
    5. Search in the Network-Tab for a package with the name 'message'
    6. click it
    7. Click on Header
    8. Search for: Authorization
    9. Copy the token
    10. Thats it. Paste it and you're done!
    """)
else:
    print("[-] Please enter only 'y' or 'n'")
    exit()
token = input("Enter the token: ")
mess = input("Enter message to send: ")
spam_ = int(input("Do you want to spam [0] or send only one message [1]"))
if spam_ == 0:
    num = int(input("How many messages?"))

aaa = False

dir = "ids.json"
    
out = input("What do you want to do?\nLogging ips [0] or start sending dm's [1]?")
if int(out) == 1:
    out2 = input("Load from collected ID's [0] or from personal file (created by you) [1]? ")
    if int(out2) == 0:
        pass
    else:
        dir = input("Enter file location: ")
        if os.path.isfile(dir):
            pass
        else:
            exit("Location not valid")
        aaa = True

if int(out) == 0:
    def log_id(id):
        try:
            with open("ids.json", "r") as file:
                data = json.load(file)
        except:
            print("Creating file...")
            f = open("ids.json", "w")
            f.write("[]")
            f.close()
            with open("ids.json", "r") as file:
                data = json.load(file)
        if id not in data:
            data.append(id)
            with open("ids.json", "w") as file:
                json.dump(data, file)
            print(" [+]", id, "Total:", len(data))
    bot = commands.Bot(command_prefix="?")
    @bot.event
    async def on_ready():
        print(' [!] Started logging ids\n')
    @bot.event
    async def on_message(message):
        if not message.author.bot:
            log_id(message.author.id)
    @bot.event
    async def on_raw_reaction_add(payload):
        if not payload.member.bot:
            log_id(payload.member.id)
    @bot.event
    async def on_member_join(member):
        if not member.bot:
            log_id(member.id)
    @bot.event
    async def on_member_update(before, after):
        if not after.member.bot:
            log_id(after.member.id)
    @bot.event
    async def on_voice_state_update(member, before, after):
        if not member.bot:
            log_id(member.id)
    try:
        bot.run(token, bot=False)
    except:
        print("[-] Token is wrong.")
        exit()
elif int(out) == 1:
    if spam_ == 0:
        bot = commands.Bot(command_prefix='?')
        @bot.event
        async def on_ready():
            print(' [!] Started sending\n')
            with open(dir, "r") as file:
                data = json.load(file)
            indx = 0
            for i in data:
                indx += 1
                member = await bot.fetch_user(i)
                try:
                    for i in range(num):
                        await member.send(mess)
                        time.sleep(4)
                        print(f" [+] Sent message {indx} / {len(data)}")
                except discord.errors.HTTPException:
                    print("Timeout")
                    time.sleep(15)
                    pass
                except Exception as e:
                    print("Couldn't send message to user: ", member)
            print(" [+] Done")
            exit()
        try:
            bot.run(token, bot=False)
        except:
            print("[-] Token is wrong.")
            exit()
    elif spam_ == 1:
        bot = commands.Bot(command_prefix='?')


        @bot.event
        async def on_ready():
            print(' [!] Started sending\n')
            with open(dir, "r") as file:
                data = json.load(file)
            indx = 0
            for i in data:
                indx += 1
                member = await bot.fetch_user(i)
                try:
                    await member.send(mess)
                    print(f" [+] Sent message {indx} / {len(data)}")
                    time.sleep(4)
                except discord.errors.HTTPException:
                    print("Timeout")
                    time.sleep(15)
                    pass
                except Exception as e:
                    print("Couldn't send message to user: ", member)
            print(" [+] Done")
            exit()


        try:
            bot.run(token, bot=False)
        except:
            print("[-] Token is wrong.")
            exit()
else:
    print("[-] Please enter 0 or 1!")
    exit()
