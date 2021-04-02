import pyttsx3
import PyPDF2

book = open('1501137575_Manual.Curso.de.java.desde.cero.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
"""rate settings"""
rate = speaker.getProperty('rate')
#print(rate)
speaker.setProperty('rate', 175)

"""voice settings"""
# voices = speaker.getProperty('voices')
# speaker.setProperty('voice', voices[1].id)

"""Volume"""
volume = speaker.getProperty('volume')
# print(volume)

#for num in range(9, pages):
page = pdfReader.getPage(3)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
#speaker.stop()kfa