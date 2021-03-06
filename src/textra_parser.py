import re
from datetime import datetime
import matplotlib.dates as plt

def TextParser(PATH):
    """ 
        Inputs:
            PATH: the path of the text file

        Returns:
            messagelist: Parsed list of each message
    """

    textfile = open(PATH,'r', encoding="utf8")
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
            convwhois = ' '.join(convwhois)
        elif num > 1:
            if match != None:
                # This creates a new message entry in the messagelist list variable
                linelastmatch += 1

                message = line.replace(match.group(1), '') # Removes the date from message
                message = message.rstrip('\n')
                
                timestamp_string = match.group(1)
                timestamp = plt.date2num(datetime.strptime(timestamp_string[1:-1], "%m/%d/%y %I:%M %p" )) # Converts the timestampt string to date object and then matplotlib converts it to a float to be used in plotting
                sender,message = message.split(':',1) # Splits after the first colon
                
                messagelist.append({"timestamp" : timestamp, "timestamp_s" : timestamp_string, "sender" : sender, "message" : message})
            else:
                # This is when a text is multiple lines, it appends the message to the last new message
                message = line.rstrip('\n')
                messagelist[linelastmatch]["message"] = messagelist[linelastmatch]["message"] + message

    return messagelist, convwhois

if __name__ == "__main__":
    texts = TextParser('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\test_texts.txt')
    print(texts)