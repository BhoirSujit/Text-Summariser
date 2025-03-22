from tkinter import *
from tkinter import ttk

class TextSummerizerView:
    def __init__(self, root) :
      
        #TODO
        # add one input textbox make sure it is scrollable to user can enter message
        # add one output box to show summer summurizerd text
        # add one button for summarize action button
        # add combobox to select between extrative/abstrative
        # use place method to properly place ui
        # use proper scale for each and every widgets
        
        #input frame
        inputFrame = LabelFrame(root, text=" Input Text ")
        inputFrame.grid(row=0, column=0, padx=10, pady=10)
        
        inputText = Text(inputFrame)
        inputText.pack(fill='both', padx=10, pady=10)
        
        #output frame
        outputFrame = LabelFrame(root, text=" Output Text ")
        outputFrame.grid(row=0, column=1, padx=10, pady=10)
        
        outputText = Text(outputFrame)
        outputText.pack(fill='both', padx=10, pady=10)
        
        #footer
        footerFrame = Frame(root, border=1, relief='groove')
        footerFrame.grid(column=0, row=2, columnspan=2, sticky='nsew', padx=10, pady=10) 

        #weight
        footerFrame.columnconfigure(0, weight=1)  
        footerFrame.columnconfigure(1, weight=2)  
        footerFrame.columnconfigure(2, weight=1)
        
        #warning label
        warningLabel = Label(footerFrame, text="Warning: Summarization may take some time.", fg="red")
        warningLabel.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        #dropdown
        summarizationType = StringVar(footerFrame)
        summarizationType.set("Extractive")

        dropdown = OptionMenu(footerFrame, summarizationType, "Extractive", "Abstractive")
        dropdown.grid(row=0, column=2, padx=10, pady=10, sticky='e')

        #summerize button
        summarizeButton = Button(footerFrame, text="Summarize")
        summarizeButton.grid(row=0, column=3, padx=10, pady=10, sticky='e', ipadx=30)

