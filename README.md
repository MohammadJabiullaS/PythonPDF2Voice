├── .idea
    ├── .gitignore
    ├── PythonPDF2Voice.iml
    ├── inspectionProfiles
    │   └── profiles_settings.xml
    ├── misc.xml
    ├── modules.xml
    └── vcs.xml
├── README.md
└── src
    ├── EntryTextVar.py
    ├── ISellMyDreams.pdf
    ├── PDF2Audio2PDF.py
    ├── pdf2speech.py
    └── samplepdf.pdf


/.idea/.gitignore:
--------------------------------------------------------------------------------
1 | # Default ignored files
2 | /shelf/
3 | /workspace.xml
4 | # Editor-based HTTP Client requests
5 | /httpRequests/
6 | # Datasource local storage ignored files
7 | /dataSources/
8 | /dataSources.local.xml
9 | 


--------------------------------------------------------------------------------
/.idea/PythonPDF2Voice.iml:
--------------------------------------------------------------------------------
 1 | <?xml version="1.0" encoding="UTF-8"?>
 2 | <module type="PYTHON_MODULE" version="4">
 3 |   <component name="NewModuleRootManager">
 4 |     <content url="file://$MODULE_DIR
quot;>
 5 |       <excludeFolder url="file://$MODULE_DIR$/.venv" />
 6 |     </content>
 7 |     <orderEntry type="jdk" jdkName="Python 3.13 (PythonPDF2Voice)" jdkType="Python SDK" />
 8 |     <orderEntry type="sourceFolder" forTests="false" />
 9 |   </component>
10 | </module>


--------------------------------------------------------------------------------
/.idea/inspectionProfiles/profiles_settings.xml:
--------------------------------------------------------------------------------
1 | <component name="InspectionProjectProfileManager">
2 |   <settings>
3 |     <option name="USE_PROJECT_PROFILE" value="false" />
4 |     <version value="1.0" />
5 |   </settings>
6 | </component>


--------------------------------------------------------------------------------
/.idea/misc.xml:
--------------------------------------------------------------------------------
1 | <?xml version="1.0" encoding="UTF-8"?>
2 | <project version="4">
3 |   <component name="Black">
4 |     <option name="sdkName" value="Python 3.13 (PythonPDF2Voice)" />
5 |   </component>
6 | </project>


--------------------------------------------------------------------------------
/.idea/modules.xml:
--------------------------------------------------------------------------------
1 | <?xml version="1.0" encoding="UTF-8"?>
2 | <project version="4">
3 |   <component name="ProjectModuleManager">
4 |     <modules>
5 |       <module fileurl="file://$PROJECT_DIR$/.idea/PythonPDF2Voice.iml" filepath="$PROJECT_DIR$/.idea/PythonPDF2Voice.iml" />
6 |     </modules>
7 |   </component>
8 | </project>


--------------------------------------------------------------------------------
/.idea/vcs.xml:
--------------------------------------------------------------------------------
1 | <?xml version="1.0" encoding="UTF-8"?>
2 | <project version="4">
3 |   <component name="VcsDirectoryMappings">
4 |     <mapping directory="$PROJECT_DIR
quot; vcs="Git" />
5 |   </component>
6 | </project>


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
1 | [![MohammadJabiullaS/PythonPDF2Voice context](https://badge.forgithub.com/MohammadJabiullaS/PythonPDF2Voice/tree/master)](https://uithub.com/MohammadJabiullaS/PythonPDF2Voice/tree/master)
2 | 


--------------------------------------------------------------------------------
/src/EntryTextVar.py:
--------------------------------------------------------------------------------
 1 | # Import the necessary module
 2 | import tkinter as tk
 3 | 
 4 | def on_text_Chage(*args):
 5 |    new_value = text_variable.get()
 6 |    print("Entered text:", new_value)
 7 | 
 8 | # Create a Tkinter window
 9 | window = tk.Tk()
10 | window.title("Getting Textvariable from Entry")
11 | 
12 | # Create a textvariable
13 | text_variable = tk.StringVar()
14 | text_variable.trace('w', on_text_Chage)
15 | # Create an Entry widget associated with the textvariable
16 | entry = tk.Entry(window, textvariable=text_variable)
17 | entry.pack()
18 | 
19 | def retrieve_text():
20 |    # Retrieve the text from the textvariable
21 |    entered_text = text_variable.get()
22 |    print("Entered text:", entered_text)
23 | 
24 | # Create a button to trigger text retrieval
25 | button = tk.Button(window, text="Retrieve Text", command=retrieve_text)
26 | button.pack()
27 | 
28 | # Run the Tkinter event loop
29 | window.mainloop()
30 | 
31 | 


--------------------------------------------------------------------------------
/src/ISellMyDreams.pdf:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/MohammadJabiullaS/PythonPDF2Voice/master/src/ISellMyDreams.pdf


--------------------------------------------------------------------------------
/src/PDF2Audio2PDF.py:
--------------------------------------------------------------------------------
  1 | from tkinter import *
  2 | import tkinter.messagebox as mb
  3 | 
  4 | from path import Path
  5 | from PyPDF4.pdf import PdfFileReader as PDFreader, PdfFileWriter as PDFwriter
  6 | import pyttsx3
  7 | from speech_recognition import Recognizer, AudioFile
  8 | from pydub import AudioSegment
  9 | import os
 10 | 
 11 | 
 12 | # Initializing the GUI window
 13 | class Window(Tk):
 14 |     def __init__(self):
 15 |         super(Window, self).__init__()
 16 |         self.title("Python PDF to Audio and Audio to PDF converter")
 17 |         self.geometry('400x250')
 18 |         self.resizable(0, 0)
 19 |         self.config(bg='Burlywood')
 20 | 
 21 |         Label(self, text='Python PDF to Audio and Audio to PDF converter', wraplength=400,
 22 |               bg='Burlywood', font=("Courier", 15)).place(x=0, y=0)
 23 | 
 24 |         Button(self, text="Convert PDF to Audio", font=("Courier", 15), bg='light blue',
 25 |                command=self.pdf_to_audio, width=25).place(x=40, y=80)
 26 | 
 27 |         Button(self, text="Convert Audio to PDF", font=("Courier", 15), bg='light blue',
 28 |                command=self.audio_to_pdf, width=25).place(x=40, y=150)
 29 | 
 30 |     def pdf_to_audio(self):
 31 |         pta = Toplevel(self)
 32 |         pta.title('Convert PDF to Audio')
 33 |         pta.geometry('500x300')
 34 |         pta.resizable(0, 0)
 35 |         pta.config(bg='Chocolate')
 36 | 
 37 |         Label(pta, text='Convert PDF to Audio', font=('Courier', 15), bg='Chocolate').place(relx=0.3, y=0)
 38 | 
 39 |         Label(pta, text='Enter the PDF file location (with extension): ', bg='Chocolate', font=("Verdana", 11)).place(
 40 |             x=10, y=60)
 41 |         filename = Entry(pta, width=32, font=('Verdana', 11))
 42 |         filename.place(x=10, y=90)
 43 | 
 44 |         Label(pta, text='Enter the page to read from the PDF (only one can be read): ', bg='Chocolate',
 45 |               font=("Verdana", 11)).place(x=10, y=140)
 46 |         page = Entry(pta, width=15, font=('Verdana', 11))
 47 |         page.place(x=10, y=170)
 48 | 
 49 |         Button(pta, text='Speak the text', font=('Gill Sans MT', 12), bg='Snow', width=20,
 50 |                command=lambda: self.speak_text(filename.get(), page.get())).place(x=150, y=240)
 51 | 
 52 |     def audio_to_pdf(self):
 53 |         atp = Toplevel(self)
 54 |         atp.title('Convert Audio to PDF')
 55 |         atp.geometry('675x300')
 56 |         atp.resizable(0, 0)
 57 |         atp.config(bg='FireBrick')
 58 | 
 59 |         Label(atp, text='Convert Audio to PDF', font=("Courier", 15), bg='FireBrick').place(relx=0.36, y=0)
 60 | 
 61 |         Label(atp, text='Enter the Audio File location that you want to read [in .wav or .mp3 extensions only]:',
 62 |               bg='FireBrick', font=('Verdana', 11)).place(x=20, y=60)
 63 |         audiofile = Entry(atp, width=58, font=('Verdana', 11))
 64 |         audiofile.place(x=20, y=90)
 65 | 
 66 |         Label(atp, text='Enter the PDF File location that you want to save the text in (with extension):',
 67 |               bg='FireBrick', font=('Verdana', 11)).place(x=20, y=140)
 68 |         pdffile = Entry(atp, width=58, font=('Verdana', 11))
 69 |         pdffile.place(x=20, y=170)
 70 | 
 71 |         Button(atp, text='Create PDF', bg='Snow', font=('Gill Sans MT', 12), width=20,
 72 |                command=lambda: self.speech_recognition(audiofile.get(), pdffile.get())).place(x=247, y=230)
 73 | 
 74 |     @staticmethod
 75 |     def speak_text(filename, page):
 76 |         if not filename or not page:
 77 |             mb.showerror('Missing field!', 'Please check your responses, because one of the fields is missing')
 78 |             return
 79 | 
 80 |         reader = PDFreader(filename)
 81 |         engine = pyttsx3.init()
 82 | 
 83 |         with Path(filename).open('rb'):
 84 |             page_to_read = reader.getPage(int(page) - 1)
 85 |             text = page_to_read.extractText()
 86 | 
 87 |             engine.say(text)
 88 |             engine.runAndWait()
 89 | 
 90 |     @staticmethod
 91 |     def write_text(filename, text):
 92 |         writer = PDFwriter()
 93 |         writer.addBlankPage(72, 72)
 94 | 
 95 |         pdf_path = Path(filename)
 96 | 
 97 |         with pdf_path.open('ab') as output_file:
 98 |             writer.write(output_file)
 99 |             output_file.write(text)
100 | 
101 |     def speech_recognition(self, audio, pdf):
102 |         if not audio or not pdf:
103 |             mb.showerror('Missing field!', 'Please check your responses, because one of the fields is missing')
104 |             return
105 | 
106 |         audio_file_name = os.path.basename(audio).split('.')[0]
107 |         audio_file_extension = os.path.basename(audio).split('.')[1]
108 | 
109 |         if audio_file_extension != 'wav' and audio_file_extension != 'mp3':
110 |             mb.showerror('Error!', 'The format of the audio file should only be either "wav" and "mp3"!')
111 | 
112 |         if audio_file_extension == 'mp3':
113 |             audio_file = AudioSegment.from_file(Path(audio), format='mp3')
114 |             audio_file.export(f'{audio_file_name}.wav', format='wav')
115 | 
116 |         source_file = f'{audio_file_name}.wav'
117 | 
118 |         r = Recognizer()
119 |         with AudioFile(source_file) as source:
120 |             r.pause_threshold = 5
121 |             speech = r.record(source)
122 | 
123 |             text = r.recognize_google(speech)
124 | 
125 |             self.write_text(pdf, text)
126 | 
127 | 
128 | # Finalizing the GUI window
129 | app = Window()
130 | 
131 | app.update()
132 | app.mainloop()


--------------------------------------------------------------------------------
/src/pdf2speech.py:
--------------------------------------------------------------------------------
 1 | import PyPDF2
 2 | import pyttsx3
 3 | from pyttsx3 import speak
 4 | 
 5 | from src.PDF2Audio2PDF import pdfPath
 6 | 
 7 | #choose file path
 8 | filePath = open('samplepdf.pdf', 'rb')
 9 | pdfReader = PyPDF2.PdfReader(filePath)
10 | 
11 | from_page = pdfReader.pages[2]
12 | text = from_page.extract_text()
13 | 
14 | speak = pyttsx3.init()
15 | speak.say(text)
16 | speak.runAndWait()
17 | 
18 | 


--------------------------------------------------------------------------------
/src/samplepdf.pdf:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/MohammadJabiullaS/PythonPDF2Voice/master/src/samplepdf.pdf


--------------------------------------------------------------------------------
