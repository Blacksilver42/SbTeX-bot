import discord, subprocess, time


with open("token", "r") as f:
	TOKEN = f.read().rstrip()

client = discord.Client();


@client.event
async def on_message(M):
	if(M.content.startswith(PREFIX+"s") or M.content.startswith(PREFIX+"S")):
		tmpfile = time.strftime("tmp/img-%s.png")
		proc = subprocess.run(["SbTeX/sbtex", "-o", "../" + tmpfile, "-i", M.content[2:]], cwd="SbTeX/")
		await client.send_file(M.channel, tmpfile)
		
		
	if(M.content.startswith(PREFIX + 'reboot')):
		if(M.author.id == "247841704386756619"):
			system("sudo shutdown -r now")


client.run(TOKEN)
