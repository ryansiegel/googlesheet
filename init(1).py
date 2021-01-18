# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

import discord
from datetime import datetime, timedelta


from gsheet import *

client = discord.Client()
sheet = gsheet()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Restrict the command to a role
    # Change REQUIREDROLE to a role id or None
    REQUIREDROLE = None
    if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=str(REQUIREDROLE)) is None:
        await message.channel.send('You don\'t have the required role!')
        return


    # Finds !alert1 in Discord for alerts
    global result
    global RANGE_NAME
    # Finds !report in Discord
    if message.content.startswith('!report'):

# \\\\\\\\\\\\\\\\\\\\\\\\\ LEXINGTON /////////////////////////
# Addison Park
        if 'Addison Park' in message.content:
            RANGE_NAME = 'D10'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Addison' in message.content:
            RANGE_NAME = 'D10'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
            
# Andover Walking Trail
        elif 'Andover Walking Trail' in message.content:
            RANGE_NAME = 'D11'
            msg = message.content[30:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Andover Walking' in message.content:
            RANGE_NAME = 'D11'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Andover' in message.content:
            RANGE_NAME = 'D11'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Arboretum
        elif 'Arboretum' in message.content:
            RANGE_NAME = 'D12'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

        # Ashland / HCE
        elif 'Ashland' in message.content:
            RANGE_NAME = 'D13'
            msg = message.content[15:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'HCE' in message.content:
            RANGE_NAME = 'D13'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Beaumont Park
        elif 'Beaumont Park' in message.content:
            RANGE_NAME = 'D14'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Beaumont' in message.content:
            RANGE_NAME = 'D14'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Bell House Park
        elif 'Bell House Park' in message.content:
            RANGE_NAME = 'D15'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Bell House' in message.content:
            RANGE_NAME = 'D15'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'BHP' in message.content:
            RANGE_NAME = 'D15'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Belleau Woods Park
        elif 'Belleau Woods Park' in message.content:
            RANGE_NAME = 'D16'
            msg = message.content[27:]
            result = [msg.replace('', '')]
            result = [ i.capitalize() for i in result ]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Belleau Woods' in message.content:
            RANGE_NAME = 'D16'
            msg = message.content[22:]
            result = [msg.replace('', '')]
            result = [ i.capitalize() for i in result ]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Belleau' in message.content:
            RANGE_NAME = 'D16'
            msg = message.content[16:]
            result = [msg.replace('', '')]
            result = [ i.capitalize() for i in result ]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Berry Hill Park
        elif 'Berry Hill Park' in message.content:
            RANGE_NAME = 'D17'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Berry Hill' in message.content:
            RANGE_NAME = 'D17'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Berry' in message.content:
            RANGE_NAME = 'D17'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Cardinal Run Park
        elif 'Cardinal Run Park' in message.content:
            RANGE_NAME = 'D18'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cardinal Run' in message.content:
            RANGE_NAME = 'D18'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cardinal' in message.content:
            RANGE_NAME = 'D18'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Castlewood Park
        elif 'Castlewood Park' in message.content:
            RANGE_NAME = 'D19'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Castlewood' in message.content:
            RANGE_NAME = 'D19'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Charles Young Park
        elif 'Charles Young Park' in message.content:
            RANGE_NAME = 'D20'
            msg = message.content[30:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Charles Young' in message.content:
            RANGE_NAME = 'D20'
            msg = message.content[25:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'CYP' in message.content:
            RANGE_NAME = 'D20'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Clinton Road Park
        elif 'Clinton Road Park' in message.content:
            RANGE_NAME = 'D21'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Clinton Road' in message.content:
            RANGE_NAME = 'D21'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Clinton Park' in message.content:
            RANGE_NAME = 'D21'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Clinton' in message.content:
            RANGE_NAME = 'D21'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]

# Constitution Park
        elif 'Constitution Park' in message.content:
            RANGE_NAME = 'D22'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Constitution' in message.content:
            RANGE_NAME = 'D22'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Coolavin Park
        elif 'coolavin park' in message.content:
            RANGE_NAME = 'D23'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'coolavin' in message.content:
            RANGE_NAME = 'D23'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Cross Keys Park
        elif 'Cross Keys Park' in message.content:
            RANGE_NAME = 'D24'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cross Keys' in message.content:
            RANGE_NAME = 'D24'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cross' in message.content:
            RANGE_NAME = 'D24'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Dixie Park
        elif 'Dixie Park' in message.content:
            RANGE_NAME = 'D25'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Dixie' in message.content:
            RANGE_NAME = 'D25'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Dogwood Park
        elif 'Dogwood Park' in message.content:
            RANGE_NAME = 'D26'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Dogwood' in message.content:
            RANGE_NAME = 'D26'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
    
# Duncan Park
        elif 'Duncan Park' in message.content:
            RANGE_NAME = 'D27'
            msg = message.content[20:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Duncan' in message.content:
            RANGE_NAME = 'D27'
            msg = message.content[15:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Ecton Park
        elif 'Ecton Park' in message.content:
            RANGE_NAME = 'D28'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Ecton' in message.content:
            RANGE_NAME = 'D28'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Fayette County Court Yard
        elif 'Fayette County Court Yard' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[34:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Fayette County Court' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[29:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Fayette Court Yard' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[27:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Fayette Yard' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Fayette Court' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Fayette' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'FCCY' in message.content:
            RANGE_NAME = 'D29'
            msg = message.content[13:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Gainesway Park
        elif 'Gainesway Park' in message.content:
            RANGE_NAME = 'D30'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Gainesway' in message.content:
            RANGE_NAME = 'D30'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Gardenside Park
        elif 'Gardenside Park' in message.content:
            RANGE_NAME = 'D31'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Gardenside' in message.content:
            RANGE_NAME = 'D31'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Garden Springs Park
        elif 'Garden Springs Park' in message.content:
            RANGE_NAME = 'D32'
            msg = message.content[28:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Garden Springs' in message.content:
            RANGE_NAME = 'D32'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'GSP' in message.content:
            RANGE_NAME = 'D32'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Gratz Park
        elif 'Gratz Park' in message.content:
            RANGE_NAME = 'D33'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Gratz' in message.content:
            RANGE_NAME = 'D33'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Green Acres Park
        elif 'Green Acres Park' in message.content:
            RANGE_NAME = 'D34'
            msg = message.content[25:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Green Acres' in message.content:
            RANGE_NAME = 'D34'
            msg = message.content[20:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Green' in message.content:
            RANGE_NAME = 'D34'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Harrods Hill Park
        elif 'Harrods Hill Park' in message.content:
            RANGE_NAME = 'D35'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Harrods Hill' in message.content:
            RANGE_NAME = 'D35'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Harrods' in message.content:
            RANGE_NAME = 'D35'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Hartland Park
        elif 'Hartland Park' in message.content:
            RANGE_NAME = 'D36'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'HP' in message.content:
            RANGE_NAME = 'D36'
            msg = message.content[11:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Hartland Swim & Racquet Club
        elif 'Hartland Clubhouse' in message.content:
            RANGE_NAME = 'D37'
            msg = message.content[27:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Hartland Club' in message.content:
            RANGE_NAME = 'D37'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'HC' in message.content:
            RANGE_NAME = 'D37'
            msg = message.content[11:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Highbee Mill Park
        elif 'Highbee Mill Park' in message.content:
            RANGE_NAME = 'D38'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Highbee Mill' in message.content:
            RANGE_NAME = 'D38'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Highbee' in message.content:
            RANGE_NAME = 'D38'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Hill N Dale Park
        elif 'Hill n Dale Park' in message.content:
            RANGE_NAME = 'D39'
            msg = message.content[25:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Hill n Dale' in message.content:
            RANGE_NAME = 'D39'
            msg = message.content[20:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'HND' in message.content:
            RANGE_NAME = 'D39'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Horse Park
        elif 'Horse Park' in message.content:
            RANGE_NAME = 'D40'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Horse' in message.content:
            RANGE_NAME = 'D40'
            msg = message.content[14:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Idle Hour Park
        elif 'Idle Hour Park' in message.content:
            RANGE_NAME = 'D41'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Idle Hour' in message.content:
            RANGE_NAME = 'D41'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Idle' in message.content:
            RANGE_NAME = 'D41'
            msg = message.content[13:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Jacobson Park
        elif 'Jacobson Park' in message.content:
            RANGE_NAME = 'D42'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Jacobson' in message.content:
            RANGE_NAME = 'D42'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Johnson Heights Park
        elif 'Johnson Heights Park' in message.content:
            RANGE_NAME = 'D43'
            msg = message.content[29:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Johnson Heights' in message.content:
            RANGE_NAME = 'D43'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Johnson' in message.content:
            RANGE_NAME = 'D43'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Kenawood Park
        elif 'Kenawood Park' in message.content:
            RANGE_NAME = 'D44'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Kenawood' in message.content:
            RANGE_NAME = 'D44'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Kingtree Park
        elif 'Kingtree Park' in message.content:
            RANGE_NAME = 'D45'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Kingtree' in message.content:
            RANGE_NAME = 'D45'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Kirklevington Park
        elif 'Kirklevington Park' in message.content:
            RANGE_NAME = 'D46'
            msg = message.content[27:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Kirklevington' in message.content:
            RANGE_NAME = 'D46'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Kirk' in message.content:
            RANGE_NAME = 'D46'
            msg = message.content[13:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
            
# Lakeside Golf Course
        elif 'Lakeside Golf Course' in message.content:
            RANGE_NAME = 'D47'
            msg = message.content[29:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Lakeside' in message.content:
            RANGE_NAME = 'D47'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
            
# Lakeview Park
        elif 'LP1' in message.content:
            RANGE_NAME = 'D48'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
            
# Lansdowne-Merrick Park 
        elif 'Landsdowne Merrick Park' in message.content:
            RANGE_NAME = 'D49'
            msg = message.content[32:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Landsdowne Merrick' in message.content:
            RANGE_NAME = 'D49'
            msg = message.content[27:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Landsdowne' in message.content:
            RANGE_NAME = 'D49'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
            
# Liberty Park 
        elif 'Liberty Park' in message.content:
            RANGE_NAME = 'D50'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Liberty' in message.content:
            RANGE_NAME = 'D50'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')




# \\\\\\\\\\\\\\\\\\\\\\\\\ FRANKFORT /////////////////////////
# Bellepoint Park aka Todd Park
        elif 'Bellepoint Park' in message.content:
            RANGE_NAME = 'I10'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Bellepoint' in message.content:
            RANGE_NAME = 'I10'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Todd Park' in message.content:
            RANGE_NAME = 'I10'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Capitol View Park
        elif 'Capitol View Park' in message.content:
            RANGE_NAME = 'I11'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Capitol View' in message.content:
            RANGE_NAME = 'I11'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Capitol' in message.content:
            RANGE_NAME = 'I11'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Cove Springs Park
        elif 'Cove Springs Park' in message.content:
            RANGE_NAME = 'I12'
            msg = message.content[26:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cove Springs' in message.content:
            RANGE_NAME = 'I12'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cove' in message.content:
            RANGE_NAME = 'I12'
            msg = message.content[13:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# East Frankfort Park
        elif 'East Frankfort Park' in message.content:
            RANGE_NAME = 'I13'
            msg = message.content[28:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'East Frankfort' in message.content:
            RANGE_NAME = 'I13'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'EFP' in message.content:
            RANGE_NAME = 'I13'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Fantasy Garden
        elif 'Fantasy Garden' in message.content:
            RANGE_NAME = 'I14'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Fantasy' in message.content:
            RANGE_NAME = 'I14'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Fort Hill
        elif 'Fort Hill' in message.content:
            RANGE_NAME = 'I15'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'FH' in message.content:
            RANGE_NAME = 'I15'
            msg = message.content[11:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Josephine Sculpture Park 
        elif 'Josephine Sculpture Park' in message.content:
            RANGE_NAME = 'I16'
            msg = message.content[33:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Josephine Sculpture' in message.content:
            RANGE_NAME = 'I16'
            msg = message.content[28:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Josephine' in message.content:
            RANGE_NAME = 'I16'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Juniper Hills Lower
        elif 'Juniper Hills Lower' in message.content:
            RANGE_NAME = 'I17'
            msg = message.content[28:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'JHL' in message.content:
            RANGE_NAME = 'I17'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Juniper Hills Upper
        elif 'Juniper Hills Upper' in message.content:
            RANGE_NAME = 'I18'
            msg = message.content[28:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'JHU' in message.content:
            RANGE_NAME = 'I18'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Kiwanis
        elif 'Kiwanis' in message.content:
            RANGE_NAME = 'I19'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Lakeview Park - Franklin
        elif 'LP2' in message.content:
            RANGE_NAME = 'I20'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Lakeview Springs Golf Course
        elif 'Lakeview Springs Golf Course' in message.content:
            RANGE_NAME = 'I21'
            msg = message.content[37:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Lakeview Springs' in message.content:
            RANGE_NAME = 'I21'
            msg = message.content[25:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'LSGC' in message.content:
            RANGE_NAME = 'I21'
            msg = message.content[13:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Riverview Park
        elif 'Riverview Park' in message.content:
            RANGE_NAME = 'I22'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Riverview' in message.content:
            RANGE_NAME = 'I22'
            msg = message.content[18:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')


# \\\\\\\\\\\\\\\\\\\\\\\\\ GEORGETOWN /////////////////////////
# Canewood Golf Course
        elif 'Canewood Golf Course' in message.content:
            RANGE_NAME = 'I26'
            msg = message.content[29:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Canewood' in message.content:
            RANGE_NAME = 'I26'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Cardone Park
        elif 'Cardone Park' in message.content:
            RANGE_NAME = 'I27'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cardone' in message.content:
            RANGE_NAME = 'I27'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Charles Brooking Park 
        elif 'Charles Brooking Park' in message.content:
            RANGE_NAME = 'I28'
            msg = message.content[30:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Charles Brooking' in message.content:
            RANGE_NAME = 'I28'
            msg = message.content[25:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'CBP' in message.content:
            RANGE_NAME = 'I28'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
            
# Cherry Blossom Golf Club 
        elif 'Cherry Blossom Golf Club' in message.content:
            RANGE_NAME = 'I29'
            msg = message.content[33:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cherry Blossom' in message.content:
            RANGE_NAME = 'I29'
            msg = message.content[23:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Cherry' in message.content:
            RANGE_NAME = 'I29'
            msg = message.content[15:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Ed Davis Park
        elif 'Ed Davis Park' in message.content:
            RANGE_NAME = 'I30'
            msg = message.content[22:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Ed Davis' in message.content:
            RANGE_NAME = 'I30'
            msg = message.content[17:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'EDP' in message.content:
            RANGE_NAME = 'I30'
            msg = message.content[12:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')


# \\\\\\\\\\\\\\\\\\\\\\\\\ WILMORE /////////////////////////
# Centennial Park
        elif 'Centennial Park' in message.content:
            RANGE_NAME = 'I76'
            msg = message.content[24:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Centennial' in message.content:
            RANGE_NAME = 'I76'
            msg = message.content[19:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Kinlaw Park
        elif 'Kinlaw Park' in message.content:
            RANGE_NAME = 'I77'
            msg = message.content[20:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Kinlaw' in message.content:
            RANGE_NAME = 'I77'
            msg = message.content[15:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')

# Talbott Park
        elif 'Talbott Park' in message.content:
            RANGE_NAME = 'I78'
            msg = message.content[21:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')
        elif 'Talbott' in message.content:
            RANGE_NAME = 'I78'
            msg = message.content[16:]
            resultt = [msg.replace('', '')]
            result = [i.capitalize() for i in resultt]
            await message.channel.send('Your nest report has been entered in the nest sheet!')


# \\\\\\\\\\\\\\\\\\\\\\\\\ ISSUES AND OTHER /////////////////////////
# ALL OTHER ISSUES 
        else:
            await message.channel.send('Your nest report has NOT been entered in the nest sheet! This could be due to your location not being capitalized, your location nickname not being correct,  your location not being spelled correctly, or the location isnt able to be transfered to the sheet yet. As such, please confirm that the location can be sent to the sheet via the updates in the #nest-announcements channel.')


   
        print(message.created_at)
        SPREADSHEET_ID = '1s1-niKvWanpbsE499C5boCpAsEyjjVh3URFK2rEeB7I'
        sheet.add(SPREADSHEET_ID, RANGE_NAME, result)
        
    elif message.content.startswith('!early'):
        RANGE_NAME = 'R6'
        result = ['YES']
        await message.channel.send('This confirms that nests have rotated early. The nest sheet has been updated.')
        print(message.created_at)
        SPREADSHEET_ID = '1s1-niKvWanpbsE499C5boCpAsEyjjVh3URFK2rEeB7I'
        sheet.add(SPREADSHEET_ID, RANGE_NAME, result)
        
    elif message.content.startswith('!rotate'):
        RANGE_NAME = 'S6'
        result = ['YES']
        await message.channel.send('This confirms that nests have rotated. The nest sheet has been updated.')
        print(message.created_at)
        SPREADSHEET_ID = '1s1-niKvWanpbsE499C5boCpAsEyjjVh3URFK2rEeB7I'
        sheet.add(SPREADSHEET_ID, RANGE_NAME, result)
        
        RANGE_NAME = 'M13'
        
        date = str(datetime.date(datetime.now() + timedelta(days=14)))
        result = [date + " 19:00:00"]
        await message.channel.send('This confirms that the next rotation time has been updated via the nest sheet.')
        print(message.created_at)
        SPREADSHEET_ID = '1s1-niKvWanpbsE499C5boCpAsEyjjVh3URFK2rEeB7I'
        sheet.add(SPREADSHEET_ID, RANGE_NAME, result)
       
client.run('Nzg1MDM2NTM2MDg1MDg2MjQ5.X8yAPw.cLSVo5x6tDd6X5bc4cTP_DOKXmM') # Add bot token here
