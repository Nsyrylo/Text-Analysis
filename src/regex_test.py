import re

textfile = open('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\test_texts.txt','r', encoding="utf8")



# accepts anything of the format '[MM/DD/YY AM|PM]'
regex = r"(\[\d+/\d+/\d+\s\d+\:\d+\s[a-zA-Z]+\])"

for num,line in enumerate(textfile,1):
    match = re.search(regex,line)
    if num == 1:
        # Splitting first line which contains who the conversation is with.
        # convWhoIs[2:-2] removes the first two words (Conversation With) and removes the last 
        # 2 words (the person's numbers)
        convWhoIs = line.split(' ')
        convWhoIs = convWhoIs[2:-2]
    #if match:
        # ADD NewMessage() function
    