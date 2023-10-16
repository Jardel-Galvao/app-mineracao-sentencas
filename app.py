import nltk
from nltk.stem import WordNetLemmatizer
from libs.api_anki import invoke
from libs.dict_api import get_word_definition

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

words_to_study = list_of_words_that_not_existis_anki()
with open('files/new_words_definitions.json', 'w', encoding='utf-8') as file:
    for i in range(0, 10):
        json.dump(get_word_definition(words_to_study[i]), file, ensure_ascii=False, indent=4)

print('TERMINOU')