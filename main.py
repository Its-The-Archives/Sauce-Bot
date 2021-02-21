from keep_alive import keep_alive
import discord
import random
import os
client = discord.Client()
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  sauce_words = [
    'Sauce?', 
    'sauce?'
  ]
  msg = message.content
  if any(word in msg for word in sauce_words):
    await message.channel.send ('https://nhentai.net/g/' + str(random.randrange(1, 350000)))
  outoftouch_words = [
  'Its Thursday', 
  'its thursday', 
  'its Thursday', 
  "Its thursday",
  "It's Thursday", 
  "it's thursday", 
  "it's Thursday", 
  "It's Thursday"
]
  if any(word in msg for word in outoftouch_words):
    await message.channel.send("You're out of touch I'm out of time But I'm out of my head When you're not around You're out of touch I'm out of time But I'm out of my head When you're not around" + " https://media.tenor.com/images/2c57da68010fa0a31575c2850b0c3c7b/tenor.gif")
  riddle_questions = [
  'tell me a riddle', 
  'Tell me a riddle'
]
  if any(word in msg for word in riddle_questions):
    await message.channel.send("Im loud and obnoxious, I like music that rhymes. I'm a fraction of the population, yet commit half the crimes. Who Am I?")
  friday_words = [
  'its friday night',
  'Its Friday night',
  'Its Friday Night', 
  "it's friday night",
  "It's Friday night", 
  "It's Friday Night"
  ]
  if any(word in msg for word in friday_words):
    await message.channel.send("https://media1.tenor.com/images/638220bb50e17f8c56b04a4ed71bfd09/tenor.gif?itemid=20413260")
  mclovin_words = [
    'who are you',
    'who are you?',
    'Who are you'
  ]
  if any(word in msg for word in mclovin_words):
    await message.channel.send("I am McLovin.")
  mac_words = [
    'Macaroni and Cheese', 
    'macaroni and cheese', 
    'Macaroni and cheese', 
  ]
  if any(word in msg for word in mac_words):
    await message.channel.send('With the Chicken Strips.')
  destiny_words = [
    'destiny', 
    'Destiny'
  ]
  if any(word in msg for word in destiny_words):
    await message.channel.send("Destiny? Did someone say Destiny? That game that Sam and Schnieds *still* play? I mean how the **FUCK** can you play the same game for 3000+ hours!? The game isn't even that good anymore. Opulence was the peak of that damn game and you know it. It's just a bullshit game where all the good shit you get gets sent to the Aether a few months from when you get it. The game isn't even original anymore. Might as well call it 'Destiny 1: Remastered' or 'Destiny 1: Deluxe'. Just play a better fucking game already. You know what? It doesn't even have to be a better game at this point. Just play something fucking *different*.")
keep_alive()
client.run(os.getenv('TOKEN'))
