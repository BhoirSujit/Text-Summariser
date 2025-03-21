import nltk
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Download necessary NLTK data
nltk.download("punkt")

# Load the model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def abstractive_summarization(text, max_length=100):
    """Generates an abstractive summary using the T5 transformer model."""
    
    # Preprocess text (T5 expects a prefix)
    input_text = "summarize: " + text
    
    # Tokenize input text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate summary
    summary_ids = model.generate(inputs, max_length=max_length, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    # Decode output
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary