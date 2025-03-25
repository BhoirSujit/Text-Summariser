import tkinter
from view.main_view import TextSummerizerView


if __name__ == '__main__':
    root = tkinter.Tk()
    
    root.title("Text Summerizer")

    app = TextSummerizerView(root)

    root.mainloop();
    
