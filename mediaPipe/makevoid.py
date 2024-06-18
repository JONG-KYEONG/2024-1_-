from gtts import gTTS

def make (text):
    tts = gTTS(text=text) 
    filename= text+'.mp3'
    tts.save(filename)

text_list = ["Hi!", "V!", "SpiderMan!", "Good!", "Fuck!", "Promise Me!", "BANG!", "Danger"]

for text in text_list:
    make(text)