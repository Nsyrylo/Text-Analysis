from textra_parser import TextParser
import matplotlib.pyplot as plt

texts = TextParser('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\Katelyn_texts.txt')

messagelength = [len(text['message']) for text in texts]

# plt.plot(range(0,len(messagelength)), messagelength)
# plt.show()

longestmessage = [text['message']  for text in texts if (len(text['message']) > 2000)]
print(longestmessage)