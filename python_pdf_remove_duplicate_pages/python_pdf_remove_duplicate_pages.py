"""Main module."""
'''
A simple tool to remove duplicate or near-duplicate PDF pages by comparing extracted text. Depends on 
'''

import fitz, sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re

# Open main window
window = tk.Tk()
window.geometry('300x100')
window.title('simplifyPDF')

# Select input and outputfile and call removeduplicatepdf
def keepPages():

    # File browser to open a file
    inFile = askopenfilename(filetypes=[('PDF Files', '*.pdf')])

    # File browser to save the file
    outFile = asksaveasfilename(filetypes=[('PDF Files', '*.pdf')])

    removeduplicatepdf(inFile, outFile) 

# Open file, select pages that have not been added already, save file
def removeduplicatepdf(inFile, outFile):

    if (inFile == "" or outFile == ""):
        return

    # Keep track of pages to keep
    toKeep = []

    # Open file
    f = fitz.open(inFile)

    numOfPages = f.page_count
    listallpages = []

    for pageNum in range(numOfPages-1):
        # Get current page and next page
        currPage = f[pageNum]

        # Extract text from both current and next page
        # Remove all whitespaces
        currText = currPage.get_text("text").encode("ascii", "ignore").decode('ascii')
        currStrip = re.sub(r"(\s|[0-9]+$)", "", currText)
        isDuplicate = False

        # Keep current page if next page doesn't already contain all text on current page
        for strip in listallpages:
            if currStrip == strip:
                isDuplicate = True
        if (not isDuplicate):
            toKeep.append(pageNum)
            listallpages.append(currStrip)

    # Create a new file using the page numbers of pages to keep
    f.select(toKeep)
    f.save('{0}.pdf'.format(outFile))
    f.close()
    print('Removed duplicates from:{0} and saved as {1}.'.format(inFile, outFile))

# Add button to open file browser
btn = ttk.Button(window, text="Open PDF File", command=lambda : keepPages())
btn.pack(side='top', pady=20)

def main():
    print(sys.argv)
    if len(sys.argv) == 1:
        window.mainloop()
    else:
        if sys.argv[1].startswith("-h") or sys.argv[1].startswith("-H"):
            print('Usage: pdfremoveduplicatepages inputfile [outputfile] -> if outputfile is empty use inputfile-noduplicates.pdf as output')
        if len(sys.argv) == 2:
            removeduplicatepdf(sys.argv[1], sys.argv[1] + '-noduplicates.pdf')
        if len(sys.argv) == 3:
            removeduplicatepdf(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()