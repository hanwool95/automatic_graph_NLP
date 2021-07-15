from sorting_text import sorting_text_n_num_v
import re, datetime

setting_date = [datetime.datetime(2021, 1, 1), datetime.datetime.now()]

increasing_list = ['늘어나다', '때문']

x_axle_list = ['철수', '영희']
y_axle_list = ['확진']

def determine_graph(noun, number, verb):
    graph_info = "line_graph"
    date_info = setting_date
    x_axle_info = []
    y_axle_info = []

    if number:
        date_list, trigger = datetime_translate(number)
        if trigger:
            if len(date_list) > 1:
                date_info = date_list
                x_axle_info = date_info
            else:
                date_info[0] = date_list[0]
        for word in verb:
            if word in increasing_list:
                date_info[0] = date_info[0].replace(month=date_info[0].month - 1)


    if noun:
        for word in noun:
            if word in x_axle_list:
                x_axle_info.append(word)
            elif word in y_axle_list:
                y_axle_info.append(word)

    if len(x_axle_info) > 1:
        graph_info = 'bar_graph'

    if not y_axle_info:
        if date_info != setting_date or x_axle_info != []:
            y_axle_info.append('확진')

    if graph_info == 'line_graph':
        x_axle_info = ['시간']

    #print(graph_info, date_info, x_axle_info, y_axle_info)
    return graph_info, date_info, x_axle_info, y_axle_info

def find_number_in_string(string):
    number_list = re.findall('\d+', string)
    return int(number_list[0])



def datetime_translate(date_list):
    date = [datetime.date(2021, 1, 1)]
    trigger = False
    for data in date_list:
        if data[-1] == '월':
            trigger = True
            if date[0] != datetime.date(2021, 1, 1):
                date.append(datetime.date(2021, find_number_in_string(data), 1))
            else:
                date[0] = date[0].replace(month=find_number_in_string(data))
        elif data[-1] == '일':
            trigger = True
            if len(date) > 1:
                date[1] = date[1].replace(day=find_number_in_string(data))
            else:
                date[0] = date[0].replace(day=find_number_in_string(data))
    return date, trigger





if __name__ == "__main__":
    text = input("원하는 텍스트를 입력해주세요").encode('utf-8')
    text = text.decode('utf-8')
    text_tuple = sorting_text_n_num_v(text)     # return noun_text, number_text, verb_text
    determine_graph(text_tuple[0], text_tuple[1], text_tuple[2])


