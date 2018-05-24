from textra_parser import TextParser
import matplotlib.pyplot as plt

texts, whois = TextParser('C:\\Users\\Nicholas\\Documents\\VS Code Projects\\Text Analysis\\Katelyn_texts.txt')

messagelength = [len(text['message']) for text in texts]

plt.plot_date([text['timestamp'] for text in texts], messagelength)
plt.show()

longestmessage = [text['message']  for text in texts if (len(text['message']) > 2000)]