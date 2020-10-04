import PyPDF2
from gtts import gTTS
import inspect,os

files=os.scandir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))


i=1
books=[]


print("Available pdf files in this directory are - ")
for file in files:
    filename=str(file.name)
    if(filename.count(".pdf")):
        print(str(i)+") "+filename)
        books.append(filename)
        i=i+1
    elif(filename.count(".mp3")):
        os.remove(filename)
if(i==1):
    print("No pdf Found :(, please copy your pdf file in this directory \n")
choice=int(input("Choose Your Pdf- "))
while not choice<=i:
    choice=int(input("Please Enter valid choice- "))



book= open(books[choice-1], "rb")
pdfReader=PyPDF2.PdfFileReader(book)



def createSingleMp3(pagenumber):
    print("loading...................\n")
    page=pdfReader.getPage(pagenumber)        
    text=page.extractText()
    ttmp3=gTTS(text)
    ttmp3.save("page "+str(pagenumber)+" .mp3")

def createRangeMp3(startPage,endPage):
    print("loading...................\n")
    for i in range(startPage,endPage+1):
        page=pdfReader.getPage(i)
        text=page.extractText()
        ttmp3=gTTS(text)
        ttmp3.save("page "+str(i)+" .mp3")

def createAllMp3():
    print("loading...................\n")
    pages=pdfReader.getNumPages()
    for i in range(0,pages):
        page=pdfReader.getPage(i)
        text=page.extractText()
        ttmp3=gTTS(text)
        ttmp3.save("page "+str(i+1)+" .mp3")


print("Do you want to read --\n")
print("1) any particular page\n")
print("2) range of pages\n")
print("3) all pages\n")
print("Enter 1, 2 or 3--")
choice=int(input())


if(choice==1):
    page=int(input("Enter the page number - "))
    createSingleMp3(page)
    print("mp3 created, check in directory\n")
elif(choice==2):
    startPage=0
    endpage=0
    endpage=pdfReader.getNumPages()
    startPage=int(input("Enter starting page(input should be a digit)--"))
    while  not startPage<endpage :
        startPage=int(input("Enter digit smaller than total pages--"))
    endpage=int(input("Enter last page(input should be a digit)--"))
    while  not startPage<endpage :
        endpage=int(input("Enter digit greater than starting page--"))
    createRangeMp3(startPage,endpage)
    print("mp3 files created for requested pages, check in directory\n")
elif(choice==3):
    print("Minimise this and do your ot1her work while i am making the mp3 ;) ..........")
    createAllMp3()
    print("mp3 files created for all pages, check in directory\n")
else:
    choice=int(input("Please enter a valid choice - "))


