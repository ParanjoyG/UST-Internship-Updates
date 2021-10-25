# 25-10-2021

Hey sorry for a late update.

Today I tried to work with GPT-Neo. I was trying to find some way to train it to custom data. However it soon became a bit confusing and I thought I need a fresh start.\
So I will start again tomorrow.

## Some points I noticed while using GPT-Neo :

* I was trying different data. I once gave it a bengali prompt 'Kichu bol na?" and it did create a speech in bengali. However when I tried again it created gibberish. That is something to be looked into.
* I tried the 2.7B version in both my local computer as well as Google Colab however it was out of disk size. So I have used the 1.3B version. Need to look to get more space.
* Definitely need to see how to run Pytorch on the GPU. The CPU takes a lot of time.
* One funny thing is even though it says that huggingface can use Tensorflow for GPT-Neo however thats a scam and it just cant. (Clearly didnt spend hours trying to debug the error!)

\
Then I used the IBM Watson Text to Speech to convert the speech to text. I have created a free account to use it for now which allows 10,000 words so I clearly need to remember to upgrade in future.

## Some Points I noticed in Watson TTS :

* It could emit emotions based on punctuations. Already makes it better than the Google assistant.
* I has 5-6 dialects in free trial so need to play with those.
* Its cool but in future I would like to study this TTS and build my own that can have any custom voice.

\

Yeah! That was it for today. I have attached the code as usual. I have also given a text generated and its correponding speech.
### Note : Prefer GPT-Neo over GPT-2 (SHOCK).
