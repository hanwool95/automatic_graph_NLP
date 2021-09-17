from external.crawling import allComments
from sorting_text import sorting_text_n_num_v
from Determiner import determine_graph
from prototype import answer_graph
import csv

if __name__ == "__main__":
    f = open('comment_and_graph.csv', 'a', newline='')
    wr = csv.writer(f)

    for comments in allComments:
        #print(text)
        print(comments)
        text_tuple = sorting_text_n_num_v(comments)  # return noun_text, number_text, verb_text
        graph_info, date_info, x_axle_info, y_axle_info = determine_graph(text_tuple[0], text_tuple[1], text_tuple[2])
        date_list = []
        for date in date_info:
            date_list.append(date.strftime('%Y. %m. %d'))
        wr.writerow([comments, graph_info, date_list, x_axle_info, y_axle_info])
    f.close()