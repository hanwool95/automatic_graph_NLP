from sorting_text import sorting_text_n_num_v
from Determiner import determine_graph

example_list = ['3월 확진자 늘어난 것은 철수 때문이야.', '4월 20일부터 확진자가 늘어났어.', '아 배고프다.', 'ㅋㅋㅋㅋㅋㅋㅋ 님 천재다.', '맞아맞아',
                '확진자는 예전부터 많았어.', '4월보다 5월 확진자가 많아', '영희때보다 철수때 확진자가 더 많아.']
example_list2 = ['오세훈 당선되고나서 3월부터 확진자가 늘어났어', '오세훈때와 박원순 때 확진자 증가는 비슷해', '이탈리아와 비교해서 우리나라 확진자는 별로 늘지 않았는데?',]



def answer_graph(kinds, date, x_axle, y_axle):
    if y_axle == []:
        return '사용되지 않습니다.'
    else:
        text = "사용되는 그래프 / "
        text += kinds + " 그래프 / "
        text += str(date) + " / "
        text += 'x축' + str(x_axle) + ', y축' + str(y_axle) + ' 사용합니다.'
    return text


if __name__ == "__main__":
    text = input("원하는 텍스트를 입력해주세요").encode('utf-8')
    text = text.decode('utf-8')
    text_tuple = sorting_text_n_num_v(text)     # return noun_text, number_text, verb_text
    raph_info, date_info, x_axle_info, y_axle_info = determine_graph(text_tuple[0], text_tuple[1], text_tuple[2])
    print(answer_graph(raph_info, date_info, x_axle_info, y_axle_info))