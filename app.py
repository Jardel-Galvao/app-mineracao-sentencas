import nltk
from nltk.stem import WordNetLemmatizer
from libs.api_anki import invoke
from libs.api_bard import bard_get_answer

import re, json

nltk.download('wordnet')

def lemmatize_word(word):
    lemmatizer = WordNetLemmatizer()

    return lemmatizer.lemmatize(word)

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        lemmatized_words = set(lemmatize_word(word) for word in words)

    return lemmatized_words

def export_sentences_txt(sentence_list):
    try:
        with open('files/sentence_list.txt', 'w') as file:
            for sentence in sentences:
                file.write(sentence + '\n')
    except Exception as e:
        print(f'An error occurred while exporting sentences! Error: {e}')

def list_of_sentences_anki():
    id_cards_deck_anki = invoke('findCards', query='deck:current')
    info_cards_deck_anki = invoke('cardsInfo', cards=id_cards_deck_anki)
    sentences = [re.sub(r'<.*?>|\[.*?\]|\n', ' ',card['fields']['Frente']['value']) for card in info_cards_deck_anki]

    return sentences

def list_of_words_that_not_existis_anki():
    file_a = 'files/english_word_data.txt'
    file_b = 'files/sentence_list.txt'
    words_set_a = read_file(file_a)
    words_set_b = read_file(file_b)
    unique_words = list(words_set_a - words_set_b)

    return unique_words

sentences = list_of_sentences_anki()
export_sentences_txt(sentences)

words_to_study =list_of_words_that_not_existis_anki()[:10]

prompt_bard = f'''
    "I need the following information for the following words:

    Definition to a beginer in english
    Phonetic Transcription
    Three short example phrases

    For the following words:"

    {words_to_study}

    and give me the answer in the following order but in html file:

    Ex: Current word is "fight"

    Definition:
    - To take part in a war or battle against an enemy

    Phonetic Transcription:
    - /faɪt/

    Three short example phrases
    - She helped him fight his drug addiction.
    - He broke his nose in the fight.
    - Now, we fight with guns.

'''
with open('files/new_words_definitions.txt', 'w', encoding='utf-8') as file:
    file.write(bard_get_answer(prompt_bard))

print('TERMINOU')