from tkinter import *
from model.abstrative_summarizer import abstractive_summarization
from model.extractive_summerizer import extractive_summarization

def doSummrize(text, option, warninglabel: Label = None, outputText: Text = None):
    if (len(text) < 10):
        warninglabel.config(text="Warning: Please Enter enough text to Summarize")
        warninglabel.update()
        return
    
    warninglabel.config(text="Warning: Summarization may take some time.")
    warninglabel.update()
    
    result = extractive_summarization(text) if (option=="Extractive") else abstractive_summarization(text)
    
    #update
    outputText.delete("1.0", "end") 
    outputText.insert("1.0", result) 
    warninglabel.config(text="Summarization complete.", fg='green')
    warninglabel.update()
    
    
   
    