import re

textfile = open('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\test_texts.txt','r', encoding="utf8")



# accepts anything of the format '[MM/DD/YY AM|PM]'
regex = r"(\[\d+/\d+/\d+\s\d+\:\d+\s[a-zA-Z]+\])"

matchcount = 0
messagelist = []

for num,line in enumerate(textfile,0):
    match = re.search(regex,line)

    # print(match)
    if num == 0:
        # Splitting first line which contains who the conversation is with.
        # convWhoIs[2:-2] removes the first two words (Conversation With) and removes the last 
        # 2 words (the person's numbers)
        convwhois = line.split(' ')
        convwhois = convwhois[2:-2]
    elif num > 1:
        if match != None:
            #TODO : create function NewMessage(match)
            message = line.replace(match.group(1), '')
            message = message.rstrip('\n')
            sender,message = message.split(':')
            messagelist.append([sender,message])
            print(messagelist)
        elif match == None :
            #TODO : create function ContinueMessage
            message = line.rstrip('\n')
            messagelist[matchcount][1] = messagelist[matchcount][1] + message

            matchcount += 1
