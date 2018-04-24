#!/usr/bin/python3
import discord, subprocess, time

PREFIX="/"

with open("token", "r") as f:
	TOKEN = f.read().rstrip()

client = discord.Client();

async def send_code(chan, code, lang="", before=""):
	await client.send_message(chan, before+"\n```"+lang+"\n" + code + "```")


async def make(M, arg="sbtex"):
	client.send_typing(M.channel)
	proc = subprocess.run(["make","-C","SbTeX", arg], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	await send_code(M.channel, proc.stdout.decode())



async def pull_typesetter(M):
	client.send_typing(M.channel)
	proc = subprocess.run(["git","-C","SbTeX","pull"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = proc.stdout.decode()
	if(output == "Already up-to-date.\n"):
		await client.add_reaction(M, u"\u2611")
	else:
		await send_code(M.channel, output, before="**Typesetter:**")
	

async def pull_self(M):
	proc = subprocess.run(["git","pull"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = proc.stdout.decode()
	if(output == "Already up-to-date.\n"):
		await client.add_reaction(M, "✅")
	else:
		await send_code(M.channel, output, before="**Self:**")


async def pull(M):
	await pull_self(M)
	await pull_typesetter(M)



@client.event
async def on_message(M):
	
	print("#{0} <{1}> {2}".format(M.channel.name, str(M.author), M.content))
	
	if(str(M.author) == "GitHub#0000"):
		await pull(M)
	
	
	if(M.content.startswith(PREFIX+"s") or M.content.startswith(PREFIX+"S")):
		tmpfile = time.strftime("tmp/img-%s.png")
		proc = subprocess.run(["SbTeX/sbtex", "-o", "../"+tmpfile, "-i", M.content[2:]], cwd="SbTeX/")
		await client.send_file(M.channel, tmpfile)
		
	if(M.content == PREFIX+"pull"):
		await pull(M)
	
	if(M.content == PREFIX+"make"):
		await make(M);
	
	if(M.content == PREFIX+"make clean"):
		await make(M, arg="clean")
		
	
	if(M.content.startswith(PREFIX + 'reboot')):
		if(M.author.id == "247841704386756619"):
			system("sudo shutdown -r now")


client.run(TOKEN)
