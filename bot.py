# -*- coding: utf-8 -*-
from chatterbot import ChatBot

chatbot = ChatBot('IRobot', trainer='chatterbot.trainers.ListTrainer')

chatbot.train([
	'Oi',
	'Oi, tudo bem ?',
	'Ola',
	'Ola tudo bem ?',
	'Como voce esta?',
	'De onde voce e ?',
	'Cade o xinelo ?',
	'Vamos assistir um filme ?',
	'Eu gosto de assistir o filme do capitao america'
])

while True:
		quest = raw_input('Voce: ')

		response = chatbot.get_response(quest);

		if float(response.confidence) > 0.5:
				print(response)
		else:
				print("Nao entendi")
(quest)




