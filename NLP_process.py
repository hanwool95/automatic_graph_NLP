from konlpy.tag import Komoran, Okt

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

komoran = Komoran(userdic='./user_dic.txt')
okt = Okt()



def komoran_tokenization_text(text, position):      # position: 'NNP', 'NNG'
    #print(text)
    token_text = komoran.pos(text)
    #print(token_text)
    token_text = [word for word, pos in token_text if not word in stopwords and pos == position]  # 불용어 제거
    return token_text

def okt_tokenization_text(text, position):      # position: 'Noun', 'Number', 'Determiner', 'Number'
    #print(text)
    token_text = okt.pos(text, stem=True)
    #print(token_text)
    token_text = [word for word, pos in token_text if not word in stopwords and pos == position]  # 불용어 제거
    return token_text


if __name__ == "__main__":
    text = input("원하는 텍스트를 입력해주세요").encode('utf-8')
    text = text.decode('utf-8')
    print(okt_tokenization_text(text, 'Noun'))

