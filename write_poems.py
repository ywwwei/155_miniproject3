import nltk
from nltk.corpus import cmudict
# try:
#     nltk.data.find('cmudict')
# except LookupError:
#     nltk.download('cmudict')


def get_last_word(sentence):
    '''
    :param sentence: str
    :return: last_word: str, the last word of sentence
    '''
    sentence = sentence.replace('.', '').replace('?', '')
    last_word = sentence.split()[-1]
    return last_word


def get_last_syllable(input, tag='sentence'):
    '''

    :param input: str, a word with tag being 'word' or a sentence with tag being 'sentence',
    :param tag: demonstrate the type of input, 'word' or 'sentence'
    :return: str, the last syllable of current sentence or word
    '''
    if tag == 'sentence':
        cur_word = get_last_word(input)
    else:
        cur_word = input
    syllable = cmudict.dict().get(cur_word, [])
    return syllable[0][-1] if syllable else ''


def count_sentence_syllables(sentence, word_id_dict, syllables_dict):
    '''
    :param sentence: str, sentence
    :param word_id_dict: dict
    :param syllables_dict: dict
    :return: syllable_count: int, the count of syllable in this sentence
    '''
    sentence = sentence.replace('.', '').replace('?', '')
    words = sentence.split()
    syllable_count = 0
    for idx, cur_word in enumerate(words):
        word_id = word_id_dict[cur_word]
        if idx == len(words)-1:
            syllable_count += syllables_dict[word_id][1]
        else:
            syllable_count += syllables_dict[word_id][0]
    return syllable_count


if __name__ == '__main__':
    word = 'love'
    print(get_last_syllable(word))
