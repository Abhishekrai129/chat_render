from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(user_input):
    # Encode the user input
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # Generate a response from the model
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # Decode the response and return it
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
