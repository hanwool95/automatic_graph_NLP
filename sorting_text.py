from NLP_process import komoran_tokenization_text, okt_tokenization_text

def sorting_text_n_num_v(text):
    noun_text1 = komoran_tokenization_text(text, 'NNG')
    nount_text2 = komoran_tokenization_text(text, 'NNP')
    number_text = okt_tokenization_text(text, 'Number')
    verb_text = okt_tokenization_text(text, 'Verb')

    return noun_text1+nount_text2, number_text, verb_text


if __name__ == "__main__":
    text = input("원하는 텍스트를 입력해주세요").encode('utf-8')
    text = text.decode('utf-8')
    text_tuple = sorting_text_n_num_v(text)
    for text in text_tuple:
        print(text)

