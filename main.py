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
    'Macaroni', 
    'macaroni' 
  ]
  if any(word in msg for word in mac_words):
    await message.channel.send('With the Chicken Strips.')
  destiny_words = [
    'destiny', 
    'Destiny'
  ]
  if any(word in msg for word in destiny_words):
    await message.channel.send("Destiny? Did someone say Destiny? That game that Sam and Schnieds *still* play? I mean how the **FUCK** can you play the same game for 3000+ hours!? The game isn't even that good anymore. Opulence was the peak of that damn game and you know it. It's just a bullshit game where all the good shit you get gets sent to the Aether a few months from when you get it. The game isn't even original anymore. Might as well call it 'Destiny 1: Remastered' or 'Destiny 1: Deluxe'. Just play a better fucking game already. You know what? It doesn't even have to be a better game at this point. Just play something fucking *different*.")
  if message.content.startswith('+help'):
    await message.channel.send("+help brings up this help screen\n if anyone says 'Destiny', makes fun of Sam and Schnieds\n if anyone says 'macaroni', says with the chicken strips\n if anyone says the n-word, says Nial\n if anyone says 'Sauce?', gives random nhentai entry\n if anyone says 'who are you', says 'I am McLovin'\n if anyone says 'its thursday', sings out of touch\n if anyone says 'its friday night', sends gif of friday night\n if anyone says 'tell me a riddle', says riddle\n if anyone says schnieder's name or any variation, sends hava nagila\n if anyone says 'May I consult The Archives?', brings up series of questions before giving access")
  jew_words = [
    'Schnieds', 
    'Schnieder', 
    'jew', 
    'schnieds', 
    'schnieder', 
    'Jew'
  ]
  if any(word in msg for word in jew_words):
    await message.channel.send("https://www.youtube.com/watch?v=vHSNZK4Je-Y&ab_channel=XxMsrSzprzxX")
  if message.content.startswith('May I consult The Archives?'):
    await message.channel.send("Hmmm.... The Archives? What do you need The Archives for? First you must answer a few questions before you may gain access. First, what is it that all tomboys pack? answer with + then answer, like so: +gamer or for multiple words, include the space like this: +gamer time")
  if message.content.startswith("+dump truck"):
    await message.channel.send("Congratulations! You have answered the first question correctly! I have now disengaged the first locking mechanism, however your quest is still far from over. The questions are only going to get harder from here. Your next question is this: What song tormented Weikel during the first months of quarantine?")
  question_2_words = [
    '+mio honda step', 
    '+step mio honda', 
    '+Mio Honda Step', 
    '+Step Mio Honda', 
    '+step', 
    '+Step'
  ]
  if any(word in msg for word in question_2_words):
    await message.channel.send("Congratulations! You have now answered the second question correctly! The second locking mechanism is now undone, yet your journey to enlightenment is not over yet. The final question is the toughest of all, yet you still want The Archives? Alright then, prove yourself worthy with your final answer: What is the name of Weikel's guitar and why did he name it that?")
  question_3_words = [
    '+Geeta, from K-On!', 
    '+geeta from k on', 
    '+Geeta from k on', 
    '+geeta from K-On!'
  ]
  if any(word in msg for word in question_3_words):
    await message.channel.send("Oh My God. You did it. You actually did it. How did you even know that last one? Weikel never talks about that. But that means the 3rd and final locking mechanism has been disabled. Welcome, my friend, to The Archives. Have a look around, only the finest may enter here. Enjoy your stay. https://pastebin.com/RgSyGvpj")
  ping_words = [
    '@McNab#2547', 
    '@Toastman Tom#5870', 
    '@SKIEH#6694', 
    '@PresumedPack890#3201', 
    '@YaBoySchnieds#3707', 
    '@kookoomomopants500#3596', 
    '@deckstein#5959', 
    '@SlightIncon#7291', 
    '@Owner of The Archives#7746', 
    '@Bertram#9737', 
    '@Anime_Liker_3000', 
    '@'
    ]
  #if any(word in msg for word in ping_words):
    #await message.channel.send("You fucking retard. You Just tried to ping someone in #general, didn't you. Well too bad, you just triggered me into sending this message, that means you will be banned for violating rule 10. Nice try.")
    ira_words = [
        'IRA', 'ira', 'car bomb', 'Car bomb', 'Ireland', 'ireland', 'Dublin',
        'dublin'
    ]
    if any(word in msg for word in ira_words):
        await message.channel.send(
            "https://www.youtube.com/watch?v=OT0yoo9B2Bc&ab_channel=SnorDrake")

    tomboy_words = [
        "It's Tuesday", "Its Tuesday", "it's Tuesday", "its Tuesday",
        "It's tuesday", "Its tuesday", "its tuesday", "it's tuesday"
    ]
    if any(word in msg for word in tomboy_words):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/669562122799284238/815054400280068096/Tomboy_Tuesday.mp4"
        )
    keep_alive()
client.run(os.getenv('TOKEN'))
