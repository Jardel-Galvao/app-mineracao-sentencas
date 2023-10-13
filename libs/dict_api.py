import requests

def get_word_definition(word):
    try:
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        json_response = response.json()
        definitions = json_response[0]['meanings'][0]['definitions']
        
        definition = {
            'word' : json_response[0]['word'],
            'phonetic' : json_response[0]['phonetic'],
            'definitions' : [definition['definition'] for definition in definitions],
            'examples' : [definition['example'] for definition in definitions if 'example' in definition],
        }
        
        return definition
    except Exception as e:
        print(f'An error occour during the dict API consult! Error: {e}')