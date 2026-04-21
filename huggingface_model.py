from transformers import pipeline
# llm_env\Scripts\activate   to activate env enviroment in terminal 
# while using any model from hugging face we need to install transformers library using pip install transformers in terminal and then we can import the pipeline function from the transformers library to create a text generation pipeline with a specific model.
# this code is using the Hugging Face Transformers library to create a text generation pipeline with a specific model called "TinyLlama/TinyLlama-1.1B-Chat-v1.0".
#  The pipeline is set to run on the CPU.
# This is how we can load model from hugging face and use it to generate text based on user input. The code also maintains a chat memory to keep track of the conversation history,
#  allowing the model to generate responses that are contextually relevant to the ongoing conversation.
# Pipeline here is a high-level API provided by the Hugging Face Transformers library that allows you to easily use pre-trained models for various natural language processing tasks,
#  such as text generation, sentiment analysis, and more. In this case, we are using the "text-generation" pipeline to generate text based on user input.
# The model "TinyLlama/TinyLlama-1.1B-Chat-v1.0" is a specific pre-trained model that is designed for chat-based interactions, and it is being loaded onto the CPU for inference.
pipe = pipeline("text-generation",model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",device = "cpu")

print("model loaded")
## Memory added 
chat_memory = [
    {"role": "system", "content":'you are a friendly chatbot '},
]
while True:
    user_input = input("User: ")


    chat_memory.append({"role": "user", "content": user_input})

    prompt = pipe.tokenizer.apply_chat_template(
    chat_memory,
    tokenize = False,
    add_generation_prompt = True
)
    outputs = pipe(
    prompt,
    max_new_tokens = 400,
    temperature = 0.5,
    do_sample = True, # this means that the model will generate text based on the probabilities of the next word, rather than always choosing the most likely words.
)
    ###
    
    response = outputs[0]["generated_text"][len(prompt):]  # Extract the generated response by removing the prompt from the output
    chat_memory.append({"role": "assistant", "content": response})  
    print("\nGenerated text:\n")
    print(outputs[0]["generated_text"])