from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs 
from happytransformer import GENSettings

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")

args = GENTrainArgs(learning_rate =1e-5, num_train_epochs = 1)
happy_gen.train("everything.txt", args=args)

args = GENSettings(max_length = 5000, no_repeat_ngram_size=2, do_sample=True, early_stopping=False, top_k=50, temperature=0.9)

result = happy_gen.generate_text("10:30pm – Night Before the Election What a scene.", args)

speech = ""

for x in result.text.split('.') :
  speech = speech + x + ".\n"

with open('./gpt_neo_happytransformer_speech.txt', 'w') as file_ :
  file_.write(speech)


