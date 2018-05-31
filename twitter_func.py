import tweepy
import json

def save_tweets_json_in_file(ids_tweets, consumer_key, consumer_secret, access_token, access_token_secret):

	if ((not ids_tweets) or (len(ids_tweets) == 0)):
		raise ValueError('A lista ids_tweets não pode ser nula ou vazia.')

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	status_json = []
	print('Iniciando busca na API do Twitter...')
    
	for id in ids_tweets:
		try:
			status = api.get_status(id)
			#print('Lendo tweet : ', status.id)
			status_json.append(status._json)
		except tweepy.TweepError as err:
			print('Erro ao buscar tweet do id : ', id)
            
	print('finalizando busca na API do Twitter...')
	print('salvando dados no arquivo...')
    
	with open('tweet_json.txt', "w", encoding="utf8") as outfile:
		json.dump(status_json, outfile)
    
	print('Arquivo salvo com sucesso!')

#test
#save_tweets_json_in_file(['892420643555336193','892177421306343426','891815181378084864','891087950875897856'], 'fJmmapkD8vwb2Z7xeo1p3IEum', 'ci0SlDlQzh5ch5jybWuOCxRaa2zdR0TNNKkDz11Xfux2rImpBp', '930905256405426177-We3KEnLpg9dzHr1iy1awQ3vyriX2aly', 'tXCGULXPUon56C7Cei2lEyQs8f7OIduGTLf3Os34GQ7WB')