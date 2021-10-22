# Kindly run this in cmd might not work in visual studio

from gtts import gTTS
import os

print( """instructions:-
            
            If you want the person to say in any language you need to type the following but only the keyword
            for example : en - english
                          |
                       key word
            languages:-      
            af: Afrikaans
            ar: Arabic
            bg: Bulgarian
            bn: Bengali
            bs: Bosnian
            ca: Catalan
            cs: Czech
            cy: Welsh
            da: Danish
            de: German
            el: Greek
            en: English
            eo: Esperanto
            es: Spanish
            et: Estonian
            fi: Finnish
            fr: French
            gu: Gujarati
            hi: Hindi
            hr: Croatian
            hu: Hungarian
            hy: Armenian
            id: Indonesian
            is: Icelandic
            it: Italian
            ja: Japanese
            jw: Javanese
            km: Khmer
            kn: Kannada
            ko: Korean
            la: Latin
            lv: Latvian
            mk: Macedonian
            ml: Malayalam
            mr: Marathi
            my: Myanmar (Burmese)
            ne: Nepali
            nl: Dutch
            no: Norwegian
            pl: Polish
            pt: Portuguese
            ro: Romanian
            ru: Russian
            si: Sinhala
            sk: Slovak
            sq: Albanian
            sr: Serbian
            su: Sundanese
            sv: Swedish
            sw: Swahili
            ta: Tamil
            te: Telugu
            th: Thai
            tl: Filipino
            tr: Turkish
            uk: Ukrainian
            ur: Urdu
            vi: Vietnamese
            zh-CN: Chinese
            zh-TW: Chinese (Mandarin/Taiwan)
            zh: Chinese (Mandarin)""" )

text = input( "Type any sentence or sentences : " )

languages = input( "Write the keywords of a language which are given in the instructions : " )

output = gTTS( text=text , lang=languages , slow=False )

output.save( "Audio_generated_by_gamerguyashutosh.mp3" )

os.system( "start Audio_generated_by_gamerguyashutosh.mp3" )
