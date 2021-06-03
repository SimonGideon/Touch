from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'en'
sp = gTTS(text="Michael works in Taita Taveta University of Science and Techonology Kenya", lang= language, slow=False)
sp.save(audio)
playsound(audio)