from googletrans import Translator

def translate():
    Translator= googletrans(to_lang="en")
    output = {}
    french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
    for phrase in french_words:
        translate = output.translate(phrase)
        translated_dic = translate.update(translation)
        return translated_dic
print(translate())




# result:{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}