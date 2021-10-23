# Kindly run this in cmd might not work in visual studio

from gtts import gTTS
import os

text = input( "Type any sentence or sentences : " )

languages = "en"

output = gTTS( text=text , lang=languages , slow=False )

output.save( "Audio_generated_by_gamerguyashutosh.mp3" )

os.system( "start Audio_generated_by_gamerguyashutosh.mp3" )
