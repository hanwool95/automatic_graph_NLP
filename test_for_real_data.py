from external.crawling import allComments
from sorting_text import sorting_text_n_num_v
from Determiner import determine_graph
from prototype import answer_graph
import csv

if __name__ == "__main__":
    f = open('result.csv', 'a', newline='')
    wr = csv.writer(f)

    for comments in allComments:

        #print(text)
        print(comments)
        text_tuple = sorting_text_n_num_v(comments)  # return noun_text, number_text, verb_text
        graph_info, date_info, x_axle_info, y_axle_info = determine_graph(text_tuple[0], text_tuple[1], text_tuple[2])
        wr.writerow([comments, answer_graph(graph_info, date_info, x_axle_info, y_axle_info)])
    f.close()