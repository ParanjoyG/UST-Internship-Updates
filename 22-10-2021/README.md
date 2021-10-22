# Work done

Today I tried to get my hands on GPT-2 and GPT-Neo first.
GPT-2 while being the predecessor to GPT-3, GPT-Neo is a GPT-3 clone trained on 2.7B parameters.
So for me I can its a good starting point for the project.

## Data Generation

For the time being I have scrapped a website called [Obama Speeches](), to get about 100 speeches of Obama. I have attached the scrapping code and the folder containing the speeches.
Although its a small amount of data (about 1MB), its a good start. Some difficulties where faced while scrapping like some pages had the speeches together while some had them in different paragraphs.
Each speech is in a text file

## GPT-2

To work with GPT-2 I have used [RunwayML]() . I have used their text generation model where you can fine tune the model using your custom dataset. I have then generated a new speech of about 5K words
and copied the text in a python program and printed it in the terminal for ease of reading. Following is the text and I have also attached the code


## GPT-Neo

For GPT-Neo I can generate text using the [HuggingFace]() transformer. However I am studying the docs so as to fine tune the data. Once I complete that, the aim is to generate a speech using the same prompt
and compare the 2.\

Overall I think the comparison would be a good start here. An then I create a logic to implement the same using GPT-3. My next aim would be to convert the text to speech using some way.
