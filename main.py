#!/usr/bin/python3
import discord, subprocess, time

PREFIX="/"

with open("token", "r") as f:
	TOKEN = f.read().rstrip()

client = discord.Client();


@client.event
async def on_message(M):
	if(M.content.startswith(PREFIX+"s") or M.content.startswith(PREFIX+"S")):
		tmpfile = time.strftime("tmp/img-%s.png")
		proc = subprocess.run(["SbTeX/sbtex", "-o", "../"+tmpfile, "-i", M.content[2:]], cwd="SbTeX/")
		await client.send_file(M.channel, tmpfile)
		
	
	if(M.content == PREFIX+"make"):
		proc = subprocess.run(["make","-C","SbTeX"], stderr=STDOUT)
		await cleint.send_message(proc.stdout.read())
	
	if(M.content == PREFIX+"make clean"):
		proc = subprocess.run(["make", "-C", "clean", "SbTeX"], stderr=STDOUT)
		await cleint.send_message(proc.stdout.read())
		
	
	if(M.content.startswith(PREFIX + 'reboot')):
		if(M.author.id == "247841704386756619"):
			system("sudo shutdown -r now")


client.run(TOKEN)
