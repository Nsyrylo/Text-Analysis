import re

def TextParser(PATH):
    """ 
        Inputs:
            PATH: the path of the text file

        Returns:
            messagelist: Parsed list of each message
    """

    textfile = open('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\Katelyn_texts.txt','r', encoding="utf8")
    # accepts anything of the format '[MM/DD/YY AM|PM]'
    regex = r"(\[\d+/\d+/\d+\s\d+\:\d+\s[a-zA-Z]+\])"

    linelastmatch = -1
    messagelist = []

    for num,line in enumerate(textfile,0):
        match = re.search(regex,line)

        if num == 0:
            # Splitting first line which contains who the conversation is with.
            # convWhoIs[2:-2] removes the first two words (Conversation With) and removes the last 
            # 2 words (the person's numbers)
            convwhois = line.split(' ')
            convwhois = convwhois[2:-2]
        elif num > 1:
            if match != None:
                #TODO : create function NewMessage(match)
                message = line.replace(match.group(1), '') # Removes the date from message
                message = message.rstrip('\n') 
                sender,message = message.split(':',1) # Splits after the first colon
                messagelist.append([sender,message])
                linelastmatch += 1
                messagelist[linelastmatch].insert(0,match.group(1)) #Insert the date back into the list

            else:
                #TODO : create function ContinueMessage
                message = line.rstrip('\n')
                messagelist[linelastmatch][2] = messagelist[linelastmatch][2] + message

    return messagelist

if __name__ == "__main__":
    TextParser('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\Katelyn_texts.txt')