from transformers import pipeline
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = '' # Insert API KEY here
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/0ea1c083-b8fd-4983-a05a-eb78ffe40352'


generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
result = generator('What are you doing?', do_sample = True, min_length = 250)
speech = ""
for x in result[0]['generated_text'].split('\n') :
  speech = speech + x + ". "

with open ('./speech(text).txt', 'w') as text :
    text.write(result[0]['generated_text'])


authenticator = IAMAuthenticator(api_key)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('./speech.mp3', 'wb') as audio_file :
  res = tts.synthesize(speech, accept = 'audio/mp3', voice='en-US_AllisonV3Voice').get_result()
  audio_file.write(res.content) 
