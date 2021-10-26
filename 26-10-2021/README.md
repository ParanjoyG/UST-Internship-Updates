# Work Done

Well today was mostly on research. Not that much of work done. However I found this wonderful transformer called [Happy Transformer](https://happytransformer.com/) . This is basicall like a layer on top of the
HuggingFace transformer library. It gives a much smoother way to train the model with custom data and parameters.


As a result I tried out the transformer and trained the GPT Neo model on the Obama data that I scrapped in the first day for a comparative study. However it did take a lot of time as
my code kept crashing due to lack of space.(About 1hr and 40 mins every time it trained.) However in the end I used the 125M model of the GPT Neo for training.

I have attached the generated speech in the folder. The results are genuinely shocking.

## Comparing it with the prev GPT-2 result.

Well to be honest, the GPT-Neo model used is much smaller than GPT-2. However it generated a much more structured text. Not as good a model when used on its own, for there was a certain 
amount of non-sense there. However when trained with the custom data for even 1 epoch, it worked really well.
\
This shows that even though the GPT-2 is a bigger model than the GPT-Neo 125M model however the data on which the latter is trained is much cleaner and better than the former.



Tomorrow I would like to work on the Happy Transformer code bts, and try out different prompts with [different generation parameters](https://happytransformer.com/text-generation/settings/) so as to get a more clearer view.
