import PyPDF2

def read_pdf(file_name):
    with open(file_name, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = pdf_reader.pages
        text = ''
        for i in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[i]
            text += page.extract_text().split('\n', 1)[1]
        #print(text.split('  '))
        return text

def get_lines(file_name):
    text = read_pdf(file_name)

    caps_found = False

    words = text.replace(':', '').replace('(', '').replace(')', '').split(' ')
    l, r = 0, 0
    i = 0
    while i < len(words):

        while i < len(words) and not words[i].isupper():
            i+=1
        l = i

        while i < len(words) and words[i].isupper():
            i+=1

        r = i-1

        if l < len(words) and r < len(words):
            words[l] = '\n' + words[l]
            words[r] = words[r] + '\n'
        i+=1

    print(' '.join(words))
    return words





#file_name = '/Users/denvar/Documents/Code/GitHub/CoHelm/src/data/medical-record-1.pdf'  # Replace with your PDF file name
#pdf_content = get_lines(file_name)
#print('\n'.join(pdf_content))  # Printing the first 500 characters of the PDF content
