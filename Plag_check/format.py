from nltk import tokenize
import re
def line_seperator():
    file = open("sample_document.txt","r",encoding='utf-8')
    file_content = file.read()
    #symbols = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+",
    #       "=", "{", "[", "]", "}", "|", "\\", ":", ";", "\"", "<", ",", ">", ".", "?", "/", "  "]
    #d = dict.fromkeys(''.join(symbols), ' ')
    #t = str.maketrans(d)
    #file_content = file_content.translate(t)
    file_content1  = re.sub('\n'+'\n\n', '', file_content)
    global list_sentences
    list_sentences = list(tokenize.sent_tokenize(file_content))
    return  list_sentences
    