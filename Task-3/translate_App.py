#importing necessary python modules 
#tkinter for GUI
#googletrans for language translation
from tkinter import *
from googletrans import Translator, constants
window = Tk()
window.title("Language Translator")
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
LanguageChoices = {'ar','bn','en','fr','de','el','gu','hi','hu','id','it','ja','kn','ko','la','ml','mr','my','ne','or','pt','pa','ru','es','ta','te','tr','ur'}
InputLanguageChoice.set('en')
TranslateLanguageChoice.set('hi')
detect_lang=""

def Translate():
    translator = Translator()
    translation=translator.translate(text=TextVar.get(),dest=TranslateLanguageChoice.get())
    global detect_lang 
    detect_lang =  constants.LANGUAGES[translation.src]
    Label(window,text=detect_lang).grid(row=3,column=0)
    Label(window,text=constants.LANGUAGES[translation.dest]).grid(row=3,column=3)
    OutputVar.set(translation.text)

NewLanguageChoiceMenu = OptionMenu(window,TranslateLanguageChoice,*LanguageChoices)
Label(window,text="Translated Language").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

Label(window,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(window,textvariable=TextVar).grid(row=2,column = 1)

Label(window,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(window,textvariable=OutputVar).grid(row=2,column = 3)

B = Button(window,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)
mainloop()
