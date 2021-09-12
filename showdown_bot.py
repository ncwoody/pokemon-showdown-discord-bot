import discord

client = discord.Client()

#  declaring our globabl variables
mon = ""
itm = ""
abl = ""
lvl = 100
hp = 0
atk = 0
de = 0
spa = 0
spd = 0
spe = 0
nat = "Serious"
mov1 = ""
mov2 = ""
mov3 = ""
mov4 = ""


@client.event
async def on_ready():
    try:
        print('Logged in as {0.user}'.format(client))
    except:
        print("Could not login")

@client.event
async def on_message(message):
    if message.author == client.user:  #  so we don't respond to our own messages- we shouldn't but just in case
        return
    if message.content.startswith("!help"):  #  if they want a list of the functions of the bot
        await message.channel.send("This bot will allow you to build a Pokemon you can then import to Pokemon Showdown")
        await message.channel.send("!mon sets the pokemon in question")
        await message.channel.send("!item sets the pokemon's item")
        await message.channel.send("!abilty sets the pokemon's ability")
        await message.channel.send("!level sets the pokemon's level (default is 100)")
        await message.channel.send("the corresponding ev is used to set a EV value (i.e. !hp, !atk, !def, !spa, !spd, !spe) (defaults for EVs will be 0)")
        await message.channel.send("!nature sets the nature (default is serious)")
        await message.channel.send("!move# will set the attack corresponding to the move you specify (i.e. !move1 to set the first move)")
        await message.channel.send("!generate will generate the showdown import code from the fields you have specified")
        await message.channel.send("!reset will reset each field to null")
    if message.content.startswith("!mon"):  # if they want to chose a pokemon
        global mon
        mon = message.content  # stripping down to the desired pokemon
        mon = mon.replace("!mon", "")
        mon = mon.strip()
    if message.content.startswith("!item"):  # if they want to choose an item
        global itm
        itm = message.content  # stripping down to the desired item
        itm = itm.replace("!item", "")
        itm = itm.strip()
    if message.content.startswith("!ability"):  # if they want to choose an ability
        global abl
        abl = message.content  # stripping down to the desired ability
        abl = abl.replace("!ability", "")
        abl = abl.strip()
    if message.content.startswith("!level"):  # if they want to set a level
        global lvl
        lvl = message.content  # stripping down to the desired level
        lvl = lvl.replace("!level", "")
        lvl = lvl.strip()
    if message.content.startswith("!hp"):  # if they want to set the hp
        global hp
        hp = message.content  # stripping down to the desired hp
        hp = hp.replace("!hp", "")
        hp = hp.strip()
    if message.content.startswith("!atk"):  # if they want to set the attack
        global atk
        atk = message.content  # stripping down to the desired attack
        atk = atk.replace("!atk", "")
        atk = atk.strip()
    if message.content.startswith("!def"):  # if they want to set the defense
        global de
        de = message.content  # stripping down to the desired defense
        de = de.replace("!def", "")
        de = de.strip()
    if message.content.startswith("!spa"):  # if they want to set the special attack
        global spa
        spa = message.content  # stripping down to the desired special attack
        spa = spa.replace("!spa", "")
        spa = spa.strip()
    if message.content.startswith("!spd"):  # if they want to set the special defense
        global spd
        spd = message.content  # stripping down to the desired special defense
        spd = spd.replace("!spd", "")
        spd = spd.strip()
    if message.content.startswith("!spe"):  # if they want to set the speed
        global spe
        spe = message.content  # stripping down to the desired speed
        spe = spe.replace("!spe", "")
        spe = spe.strip()
    if message.content.startswith("!nature"):  # if they want to choose a nature
        global nat
        nat = message.content  # stripping down to the desired nature
        nat = nat.replace("!nature", "")
        nat = nat.strip()
    if message.content.startswith("!move1"):  # if they want to choose a first move
        global mov1
        mov1 = message.content  # stripping down to the desired move
        mov1 = mov1.replace("!move1", "")
        mov1 = mov1.strip()
    if message.content.startswith("!move2"):  # if they want to choose a second move
        global mov2
        mov2 = message.content  # stripping down to the desired move
        mov2 = mov2.replace("!move2", "")
        mov2 = mov2.strip()
    if message.content.startswith("!move3"):  # if they want to choose a third move
        global mov3
        mov3 = message.content  # stripping down to the desired move
        mov3 = mov3.replace("!move3", "")
        mov3 = mov3.strip()
    if message.content.startswith("!move4"):  # if they want to choose a fourth move
        global mov4
        mov4 = message.content  # stripping down to the desired move
        mov4 = mov4.replace("!move4", "")
        mov4 = mov4.strip()
    if message.content.startswith("!generate"):  # if they want to print the pokemon they specified
        if mon == "" or abl == "":
            await message.channel.send("You haven't entered all of the required fields (Pokemon, ability)")
        else:
            if itm != "":
                await message.channel.send(mon + " @ " + itm)
            else:
                await message.channel.send(mon)
            await message.channel.send("Ability: " + abl)
            evs = ev_String()
            if hp == 0 and atk == 0 and de == 0 and spa == 0 and spd == 0 and spe == 0:
                pass
            else:
                await message.channel.send("EVs: " + evs)
                await message.channel.send("Nature: " + nat)
            if mov1 != "":
                await message.channel.send("- " + mov1)
            if mov2 != "":
                await message.channel.send("- " + mov2)
            if mov3 != "":
                await message.channel.send("- " + mov3)
            if mov4 != "":
                await message.channel.send("- " + mov4)
    if message.content.startswith("!reset"):  # if they want to clear all the fields
        #  we just set all of them to default
        mon = ""
        itm = ""
        abl = ""
        lvl = 100
        hp = 0
        atk = 0
        de = 0
        spa = 0
        spd = 0
        spe = 0
        nat = "Serious"
        mov1 = ""
        mov2 = ""
        mov3 = ""
        mov4 = ""

def ev_String():
    ret = ""
    if int(hp) > 0:
        ret = ret + hp + " HP / "
    if int(atk) > 0:
        ret = ret + atk + " Atk / "
    if int(de) > 0:
        ret = ret + de + " Def / "
    if int(spa) > 0:
        ret = ret + spa + " SpA / "
    if int(spd) > 0:
        ret = ret + spd + " SpD / "
    if int(spe) > 0:
        ret = ret + spe + " Spe / " 
    return ret

client.run(<insert your token here>)

#  may add the ability to specify all fields in one command
#  maybe allow moves to be added with the !move command
    #  can specify the individual moves to overwrite accidents (i.e. move2 to overwrite the second move slot)
