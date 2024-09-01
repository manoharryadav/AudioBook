import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Open file dialog to select PDF
book = askopenfilename()

# Initialize PDF reader
pdfreader = PyPDF2.PdfReader(book)


pages = len(pdfreader.pages)


player = pyttsx3.init()


for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()  

    
    if text.strip():  
        player.say(text)
        player.runAndWait()
