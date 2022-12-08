from typing import Counter
import pprint

#PART I
#I didnt understand how to do the @classmethod, i tryed but isnt working
class Text():
    def __init__(self, text_str:str) -> None:
        self.text_str = text_str
    @classmethod
    def check_text(cls,text_file):
        with open (text_file, mode='r') as file:
            text_file = file.read()
            return Text(text_file)

    def frequency_of_word(self, word) -> int:
        '''returns the frequency of a given word in the self.text_str'''               
        if len(self.text_str) != 0:
            split = self.text_str.split(' ')
            frequency = split.count(word)
            return f' the frequency of `{word}` is {frequency}'
        else: None

    def most_common_word(self)->int:
        '''returns the most common word in the self.text_str''' 
        if len(self.text_str) != 0:
            split = Counter(self.text_str.split(' '))
            most_common = split.most_common(1)
            return f'the most common word is `{most_common}`'
        else:None

    def unique_words(self)->list: 
        '''returns a list of words that appears just once in the self.text_str'''
        if len(self.text_str) != 0: #strip()
            clean_text = self.text_str.strip('.')
            unique_words = set(clean_text.split(' '))
            return f'The unique words are: {unique_words}'

text1 = Text('A good book would sometimes cost as much as a good house.')
print(text1.frequency_of_word('good'))
text2 = Text('geeks for geeks is for geeks. By geeks and for the geeks.')
print(text2.most_common_word())
print(text2.unique_words())

#Part II
uploaded_text = Text('./the_stranger.txt')
print(uploaded_text.check_text('./the_stranger.txt'))
print(uploaded_text.most_common_word())
print(uploaded_text.check_text())
print(uploaded_text.frequency_of_word('good'))
                
