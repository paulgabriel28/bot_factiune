import discord 
import asyncio
from discord.ext.commands import Bot
import datetime
import requests
import json

current_time = datetime.datetime.now()
client = discord.Client(intents=discord.Intents.all())
prefix = ","
p_total = 0


async def change_status():
    games = ["by acid#8560", "rage.b-hood.ro", "Hitman Agency - RAGE", "B-Hood Comunity"]

    while not client.is_closed():
        for loop in range(20):
            for game in games:
                await asyncio.sleep(7)
                await client.change_presence(activity=discord.Game(name=game))
        await change_status()

@client.event
async def on_ready():
    await change_status()

@client.event
async def on_member_join(member):
    channel = client.get_channel(1060302684940402708)
    await channel.send(f"`[+] `{member.mention}` s-a alaturat factiunii Hitman Agency!`")
    await member.send(f"Salut {member.mention}\nBun venit in **Hitman Agency**.\nNu uita ca trebuie sa respecti atat regulamentul server-ului de RAGE:MP, cat si regulamentul factiunii.\n> regulament RAGE:MP general: https://ragepanel.b-hood.ro/rules/view/regulament-server\n> regulament factiune: https://ragepanel.b-hood.ro/rules/view/regulament-hitman\nNu uita sa iti verifici contul de discord pe server-ul factiunii pe canalul <#1060174775009419307> respectand modelul, daca nu il respecti 100% nu vei primi gradul!\nDistractie placuta in factiune si succes la raport!")
    
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1060314375052857465)
    await channel.send(f"`[-] `{member.mention}` [INFO: {member.name}#{member.discriminator} | {member.mention}`")


    
@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    if message.content == "salut":
        await message.channel.send("Salut!")
        return

    global prefix
    member = message.guild.get_member(message.author.id)
    if member is not None:
        if message.content.startswith(prefix):
            if discord.utils.get(member.roles, name="[7]") is not None or discord.utils.get(member.roles, name="[6]") is not None or discord.utils.get(member.roles, name="♖ Manager") is not None:
                command, *args = message.content.split()
                
                if command == f"{prefix}setprefix":
                    if not args:
                        await message.channel.send(f"Foloseste **{prefix}setprefix [prefix]**!")
                        return 
                    prefix = args[0]
                    await message.channel.send(f":white_check_mark: Prefix-ul setat este **{prefix}**!")
                    pass
            
            
                elif command == f"{prefix}kick":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}kick [persoana] [motiv]**!")
                        return
                    
                    member_to_kick = message.mentions[0]
                    
                    if member_to_kick == message.author:
                        await message.channel.send("**Eroare:** Nu iti poti da kick singur!")
                    else:
                        reason_kick = " ".join(args[1:]) 
                        if len(reason_kick) < 1:
                            reason_kick = "Nespecificat"
                        await message.channel.send(f"`I-ai dat kick lui `**{member_to_kick}**`, motiv: `**{reason_kick}**")
                        await member_to_kick.send(f"Salut, {member_to_kick.mention} ai primit **kick** de la **{message.author}** de pe server-ul de discord al factiunii **Hitman Agency** pe motivul **{reason_kick}**, ai mai multa grija data viitoare si reciteste regulamentele!\n> regulament RAGE:MP general: https://ragepanel.b-hood.ro/rules/view/regulament-server\n> regulament factiune: https://ragepanel.b-hood.ro/rules/view/regulament-hitman")
                        await member_to_kick.kick()
                
                    log_channel = client.get_channel(1061572282478252052)  
                    await log_channel.send(f"{message.author}` i-a dat kick lui` **{member_to_kick}**`, motiv: `**{reason_kick}**")
                    pass
                
                
                elif command == f"{prefix}ban":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}ban [persoana] [motiv]**!")
                        return
                    if len(args) < 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    member_to_ban = message.mentions[0]
                    if member_to_ban == message.author:
                        await message.channel.send("**Eroare:** Nu iti poti da ban singur!")
                    else:
                        reason_ban = " ".join(args[1:]) 
                        if len(reason_ban) < 1:
                            reason_ban = "Nespecificat"
                        await message.channel.send(f"`L-ai banat pe `**{member_to_ban}**`, motiv: `**{reason_ban}**")
                        await member_to_ban.send(f"Salut, {member_to_ban.mention} ai primit **ban permanent** de la **{message.author}** de pe server-ul de discord al factiunii **Hitman Agency** pe motivul **{reason_ban}**!")
                        await member_to_ban.ban(reason=f"{message.author} i-a dat ban lui {member_to_ban} motiv: {reason_ban}")
                
                    log_channel = client.get_channel(1061572282478252052)  
                    if len(reason_ban) < 1:
                            reason_ban = "Nespecificat"
                    await log_channel.send(f"{message.author}` i-a dat ban lui `**{member_to_ban}**` motiv: `**{reason_ban}**")
                    pass
                
                
                elif command == f"{prefix}membru":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}membru [persoana]**!")
                        return
                    if len(args) > 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    
                    member_role = message.mentions[0]
                    role_object1 = discord.utils.get(message.guild.roles, name="✯ Membru HA")
                    role_object2 = discord.utils.get(message.guild.roles, name="𓀝 Neverificat")
                    await member_role.add_roles(role_object1)
                    await member_role.remove_roles(role_object2)
                    await message.channel.send(f"I-ai dat gradul de <@&1060297692108046346> lui {member_role}!")
                
                    log_channel = client.get_channel(1061634819303428136)  
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    await log_channel.send(f"**{message.author}**` i-a dat gradul de` <@&1060297692108046346> `lui` **{member_role}** `[data: `**{current_time}**`]`")
                    pass
                    
                
                elif command == f"{prefix}rup":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}rup [persoana]**!")
                        return
                    if len(args) > 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    
                    member_role = message.mentions[0]
                    
                    if member_role == message.author:
                        await message.channel.send("**Eroare:** Nu iti poti da rank-up singur!")
                        return
                        
                    rol_acordat = 1
                    ver_acces = 1
                    
                    if discord.utils.get(member_role.roles, name = "[5]"):
                        await message.channel.send(f"**{member_role}** are gradul maxim! (5)")
                        ver_acces = 0
                        
                    elif discord.utils.get(member_role.roles, name = "[4]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[5]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[4]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_acordat = 1060298459527254056
                        pass
                    
                    elif discord.utils.get(member_role.roles, name = "[3]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[4]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[3]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_acordat = 1060298250529275954
                        pass  
                    
                    elif discord.utils.get(member_role.roles, name = "[2]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[3]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[2]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_acordat = 1060298253461114950
                        pass

                    elif discord.utils.get(member_role.roles, name = "[1]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[2]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[1]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_acordat = 1060298255713452182
                        pass
                    
                    elif discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[1]")
                        await member_role.add_roles(role_object1)
                        rol_acordat = 1060298258376822815
                        pass
                    
                    if ver_acces == 1:
                        await message.channel.send(f"I-ai dat gradul de <@&{rol_acordat}> lui **{member_role}**!")
                        log_channel = client.get_channel(1061634819303428136)  
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        await log_channel.send(f"**{message.author}**` i-a dat gradul de` <@&{rol_acordat}> `lui` **{member_role}** `[data: `**{current_time}**`]`")
                    pass
                
                elif command == f"{prefix}rdown":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}rdown [persoana]**!")
                        return
                    if len(args) > 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    
                    member_role = message.mentions[0]
                    
                    if member_role == message.author:
                        await message.channel.send("**Eroare:** Nu iti poti da rank-down singur!")
                        return
                        
                    rol_acordat = 0
                    rol_scos = 0
                    ver_acces = 1
                    
                    if discord.utils.get(member_role.roles, name = "[5]"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[4]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[5]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_scos = 1060298459527254056
                        rol_acordat = 1060298250529275954
                        
                    elif discord.utils.get(member_role.roles, name = "[4]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[3]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[4]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_scos = 1060298250529275954
                        rol_acordat = 1060298253461114950
                        pass
                    
                    elif discord.utils.get(member_role.roles, name = "[3]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[2]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[3]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_scos = 1060298253461114950
                        rol_acordat = 1060298255713452182
                        pass  
                    
                    elif discord.utils.get(member_role.roles, name = "[2]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object1 = discord.utils.get(message.guild.roles, name="[1]")
                        role_object2 = discord.utils.get(message.guild.roles, name="[2]")
                        await member_role.add_roles(role_object1)
                        await member_role.remove_roles(role_object2)
                        rol_scos = 1060298255713452182
                        rol_acordat = 1060298258376822815
                        pass

                    elif discord.utils.get(member_role.roles, name = "[1]") and discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        role_object2 = discord.utils.get(message.guild.roles, name="[1]")
                        await member_role.remove_roles(role_object2)
                        rol_scos = 1060298258376822815
                        rol_acordat = 1060297692108046346
                        pass
                    
                    elif discord.utils.get(member_role.roles, name = "✯ Membru HA"):
                        ver_acces = 0
                        await message.channel.send(f"**{member_role}** are gradul minim de pe server, nu il poti scoate!")
                        pass
                    
                    if ver_acces == 1:
                        await message.channel.send(f"I-ai scos gradul de <@&{rol_scos}> lui **{member_role}**, acum are gradul de <@&{rol_acordat}>!")
                        log_channel = client.get_channel(1061634819303428136)  
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        await log_channel.send(f"**{message.author}**` i-a scos gradul de` <@&{rol_scos}> `lui` **{member_role}** `[data: `**{current_time}**`]`")
                    pass
                
                
                elif command == f"{prefix}tester":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}tester [persoana]**!")
                        return
                    if len(args) > 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    member_role = message.mentions[0]
                    
                    if discord.utils.get(member_role.roles, name = "✵ Tester"):
                        await message.channel.send(f"**Eroare:** {message.author.mention}, **{member_role.mention}** are deja gradul de '**Tester**'!\nDaca vrei sa ii scoti functia foloseste comanda **{prefix}rtester [persoana] [motiv]**")
                        return
                    elif discord.utils.get(member_role.roles, name = "[1]") or discord.utils.get(member_role.roles, name = "[2]") :
                        await message.channel.send(f"**Eroare:** {message.author.mention}, **{member_role.mention}** nu are gradul necesar (3) pentru functia de '**Tester**'!")
                        return
                    
                    role_object = discord.utils.get(message.guild.roles, name="✵ Tester")
                    await member_role.add_roles(role_object)
                    await message.channel.send(f"I-ai dat gradul de <@&1060300639671951460> lui **{member_role}**!")
                
                    log_channel = client.get_channel(1060305676196388975)  
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                    await log_channel.send(f"**{member_role.name}** a fost promovat la functia de **Tester** in cadrul factiunii **Hitman Agency**, felicitari si succes cu functia! [**{current_time} | ||{member_role.mention}||**]")

                    log_channel = client.get_channel(1061634819303428136)  
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    await log_channel.send(f"**{message.author}**` i-a dat gradul de` <@&1060300639671951460> `lui` **{member_role}** `[data: `**{current_time}**`]`")
                    pass
                
            
                elif command == f"{prefix}rtester":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}rtester [persoana] [motiv]**!")
                        return
                    if len(args) < 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    member_role = message.mentions[0]
                    reason_tester = " ".join(args[1:]) 
                    if discord.utils.get(member_role.roles, name = "✵ Tester"):
                        if len(reason_tester) < 1:
                            reason_tester = "Nespecificat"
                            
                        await message.channel.send(f"I-ai scos functia de **Tester**, lui **{member_role.mention}** motiv: **{reason_tester}**")
                        role_object = discord.utils.get(message.guild.roles, name="✵ Tester")
                        await member_role.remove_roles(role_object)
                            
                        log_channel = client.get_channel(1060305676196388975)  
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                        await log_channel.send(f"**{member_role.name}** nu mai are functia de **Tester** in factiunea Hitman Agency [**{current_time} | ||{member_role.mention}||**]\nMotiv: **{reason_tester}**")
                    else:
                        await message.channel.send(f"**Eroare:** {message.author.mention}, **{member_role.mention}** nu are gradul de '**Tester**'!")
                    pass
                
                
                elif command == f"{prefix}respo":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}respo [persoana]**!")
                        return
                    if len(args) > 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    member_role = message.mentions[0]
                    
                    if discord.utils.get(member_role.roles, name = "✶ Responsabil"):
                        await message.channel.send(f"**Eroare:** {message.author.mention}, **{member_role.mention}** are deja gradul de '**Responsabil**'!\nDaca vrei sa ii scoti functia foloseste comanda **{prefix}rrespo [persoana] [motiv]**")
                        return
                    
                    role_object = discord.utils.get(message.guild.roles, name="✶ Responsabil")
                    await member_role.add_roles(role_object)
                    await message.channel.send(f"I-ai dat gradul de <@&1060300646911332483> lui **{member_role}**!")
                
                    log_channel = client.get_channel(1060305676196388975)  
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                    await log_channel.send(f"**{member_role.name}** a fost promovat la functia de **Responsabil** in cadrul factiunii **Hitman Agency**, felicitari si succes cu functia! [**{current_time} | ||{member_role.mention}||**]")

                    log_channel = client.get_channel(1061634819303428136)  
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    await log_channel.send(f"**{message.author}**` i-a dat gradul de` <@&1060300646911332483> `lui` **{member_role}** `[data: `**{current_time}**`]`")
                    pass
                
            
                elif command == f"{prefix}rrespo":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}rrespo [persoana] [motiv]**!")
                        return
                    if len(args) < 1:
                        await message.channel.send("**Eroare:** Mentioneaza o singura persoana!")
                        return
                    member_role = message.mentions[0]
                    reason_respo = " ".join(args[1:]) 
                    if discord.utils.get(member_role.roles, name = "✶ Responsabil"):
                        if len(reason_respo) < 1:
                            reason_respo = "Nespecificat"
                            
                        await message.channel.send(f"I-ai scos functia de **Responsabil**, lui **{member_role.mention}** motiv: **{reason_respo}**")
                        role_object = discord.utils.get(message.guild.roles, name="✶ Responsabil")
                        await member_role.remove_roles(role_object)
                            
                        log_channel = client.get_channel(1060305676196388975)  
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                        await log_channel.send(f"**{member_role.name}** nu mai are functia de **Responsabil** in factiunea Hitman Agency [**{current_time} | ||{member_role.mention}||**]\nMotiv: **{reason_respo}**")
                    else:
                        await message.channel.send(f"**Eroare:** {message.author.mention}, **{member_role.mention}** nu are gradul de '**Responsabil**'!")
                    pass
                
                elif command == f"{prefix}cc":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}cc [nr]**!")
                        return
                    val = int(args[0]) + 1
                    await message.channel.purge(limit = val)
                    pass
                
                
                elif command == f"{prefix}help":
                    embed_help = discord.Embed(title = "Help List", description = f"Prefix = {prefix}", color=0x00ff00)
                    embed_help.add_field(name=f"{prefix}kick [persoana] [motiv]", value="-> dai kick unui membru", inline=False)
                    embed_help.add_field(name=f"{prefix}ban [persoana] [motiv]", value="-> dai ban unui membru", inline=False)
                    embed_help.add_field(name=f"{prefix}membru [persoana]", value="-> dai rolul de Membru si scoti rolul de Neverificat", inline=False)
                    embed_help.add_field(name=f"{prefix}rup [persoana]", value="-> dai rank-up automat unui membru", inline=False)
                    embed_help.add_field(name=f"{prefix}rdown [persoana]", value="-> dai rank-down automat unui membru", inline=False)
                    embed_help.add_field(name=f"{prefix}tester / {prefix}rtester [persoana]", value="-> dai / scoti gradul de Tester", inline=False)
                    embed_help.add_field(name=f"{prefix}respo / {prefix}rrespo [persoana]", value="-> dai / scoti gradul de Responsabil", inline=False)
                    embed_help.add_field(name=f"{prefix}cc [nr]", value="-> dai clear chat", inline=False)
                    embed_help.add_field(name=f"{prefix}anno [mesaj]", value="-> dai un anunt pe canalul 🔔・┃anno si PM la toti membrii", inline=False)
                    embed_help.add_field(name=f"{prefix}pm [persoana] [mesaj]", value="-> dai un mesaj in privat membrului mentionat", inline=False)
                    embed_help.set_footer(text="acid & rage.b-hood.ro")
                    await message.channel.send(embed = embed_help)
                    pass
                
                elif command == f"{prefix}anno":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}anno [mesaj]**!")
                        return
                    if len(args) < 3:
                        await message.channel.send("**Eroare:** Mesajul este prea scurt!")
                        return
                    channel = discord.utils.get(message.guild.text_channels, name="🔔・┃anno")
                    args = message.content.split(" ")
                    msg = " ".join(args[1:])
                    for member in filter(lambda m: not m.bot, channel.members):
                        try:
                            await member.send(f"Anno by {message.author}: **{msg}**")
                            await asyncio.sleep(5)
                        except:
                            pass
                    channel_log = discord.utils.get(message.guild.text_channels, name="📝・┃pm_anno")
                    await channel.send(f"Anno Automat: **{msg}**\n||@everyone||")
                    await message.channel.send("**Info Anno:** Mesajul a fost trimis catre toti membrii si postat pe <#1060305573909889155>")
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                    await channel_log.send(f"Anno by {message.author.name}: **{msg}**\n`Data: {current_time}`")
                    pass
                
                
                elif command == f"{prefix}pm":
                    if not args: 
                        await message.channel.send(f"**Info:** Foloseste **{prefix}pm [persoana] [mesaj]**!")
                        return
                    if len(args) < 4:
                        await message.channel.send("**Eroare:** Mesajul este prea scurt!")
                        return
                    args = message.content.split(" ")
                    msg = " ".join(args[2:])
                    channel_log = discord.utils.get(message.guild.text_channels, name="📝・┃pm_anno")
                    for member in message.mentions:
                        await member.send(f"PM by **{message.author.name}**: **{msg}**")
                        await message.channel.send(f"**PM:** Mesajul a fost trimis cu succes catre **{member.name}**!")
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y")
                        await channel_log.send(f"PM de la {message.author.name} pentru {member.name}: {msg}\n`Data: {current_time}`")
                    pass
                
                
                # elif command == f"{prefix}cerere":
                #     embed=discord.Embed(title="Verificare cont ", description="Lasa mai jos o cerere de rank pentru a primi acces la server-ul de discord.", color=0x871212)
                #     embed.add_field(name="Nume server:", value="Nickname-ul tau de pe server-ul de RAGE.", inline=True)
                #     embed.add_field(name="Rank", value="Rank-ul actual din factiune.", inline=False)
                #     embed.add_field(name="Dovada:", value="ScreenShot intreg la joc cand ai [/raport] in chat.", inline=True)
                #     embed.set_footer(text="acid & rage.b-hood.ro")
                #     await message.channel.send(embed=embed) 
                #     pass
                
                else:
                    await message.channel.send(f"**Eroare:** Comanda folosita nu exista, foloseste comanda **{prefix}help** pentru ajutor!")
                
            else:
                await message.channel.send("**Eroare:** Nu ai permisiunea de a folosi aceasta comanda.")


client.run("TOKEN")
