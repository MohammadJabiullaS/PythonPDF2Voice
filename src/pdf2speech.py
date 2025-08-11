import PyPDF2
import pyttsx3
from pyttsx3 import speak

from src.PDF2Audio2PDF import pdfPath

#choose file path
filePath = open('samplepdf.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(filePath)

from_page = pdfReader.pages[2]
text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

