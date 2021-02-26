import ChatBot

bot = ChatBot('Luisa')
from chatterbot.trainers import ListTrainer

bot.set_trainer(ListTrainer)
bot.train(['What is your name?', 'My name is Luisa'])
bot.train(['Who are you?', 'I am a bot, created by you' ])
bot.train(['Do you know Bernardo Schaefers?', 'Yes, that is you, and you created me'])

from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
chatbot.get_response("Hello, how are you today?")

for files in os.listdir('./english/'):
    data=open('./english/'+files,'r').readlines()
    bot.train(data)

while True:
    message=input('\t\t\tYou:')
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Luisa:',reply)
    if message.strip()=='Bye':
        print('Luisa: Bye')
        break    

    