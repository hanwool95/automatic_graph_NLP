from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render, HttpResponse
from .models import Graph
import datetime
from .data_sorting import date_list, case_dict, death_dict
import matplotlib.pyplot as plt
import matplotlib

import base64
import io

import numpy as np

import matplotlib.font_manager as fm
import matplotlib.ticker as ticker


from django.views.decorators.csrf import csrf_exempt


matplotlib.use('agg')
font_path = r'/Users/hanwool/PycharmProjects/automatic_graph_NLP/external/moonhwabold.ttf'
fontprop = fm.FontProperties(fname=font_path, size=10)


def get_string_to_list(string):
    x = string
    x = x.replace(" ", "")
    x = x.replace("[", "")
    x = x.replace("'", "")
    x = x.replace("]", "")
    x_list = x.split(',')
    return x_list

def string_list_to_int_list(string_list):
    int_list = []
    for word in string_list:
        if word == "":
            int_list.append(0)
        else:
            int_list.append(int(word))
    return int_list

def remove_dot_in_string(string):
    x = string
    x = x.replace('"', "")
    return x

def string_to_date(string):
    x = string
    x = x.replace(" ", "")
    x = x.replace("[", "")
    x = x.replace("'", "")
    x = x.replace("]", "")
    x_list = x.split(',')
    return x_list

@csrf_exempt
def chart_bar(request):
    #graph_init = Graph.objects.filter(id__lte=2570)
    graph_init = Graph.objects.all()
    graph_list=[]
    """
    for data in graph_init:
        print(data)
        comments = remove_dot_in_string(data.comments)
        x_axle_list = get_string_to_list(data.x_axle)
        y_axle_list = get_string_to_list(data.y_axle)
        date = string_to_date(data.pub_date)
        info = data.graph_info


        x_data = []
        y_data = []

        print(y_axle_list)
        for x in x_axle_list:
            if x in case_dict.keys():
                x_data.append(x)
                if '사망' in y_axle_list:
                    before_cal_list =string_list_to_int_list(
                        death_dict[x][date_list.index(date[1]):date_list.index(date[0]) - 1])
                else:
                    before_cal_list = string_list_to_int_list(
                        case_dict[x][date_list.index(date[1]):date_list.index(date[0]) - 1])
                count = sum(before_cal_list)
                y_data.append(count)
            elif x == '시간':
                x_data.append(date_list[date_list.index(date[1]):date_list.index(date[0]) - 1])
                if '사망' in y_axle_list:
                    y_data.append(
                        string_list_to_int_list(death_dict['한국'][date_list.index(date[1]):date_list.index(date[0]) - 1]))
                else:
                    y_data.append(
                        string_list_to_int_list(case_dict['한국'][date_list.index(date[1]):date_list.index(date[0]) - 1]))


        graph_list.append([comments, x_data, y_data, info, data.id])
    #print(graph_list)x
    """
    return render(request, "graph/chart_ajax.html", {'graph_list': graph_init})

@csrf_exempt
def graph_specific(request, id):
    data = Graph.objects.get(id=id)
    comments = remove_dot_in_string(data.comments)
    x_axle_list = get_string_to_list(data.x_axle)
    y_axle_list = get_string_to_list(data.y_axle)
    date = string_to_date(data.pub_date)
    info = data.graph_info

    x_data = None
    y_data = None

    print(y_axle_list)
    for x in x_axle_list:
        if x in case_dict.keys():
            if type(x_data) != list:
                x_data = []
                y_data = []
            x_data.append(x)
            if '사망' in y_axle_list:
                before_cal_list = string_list_to_int_list(
                    death_dict[x][date_list.index(date[1]):date_list.index(date[0]) - 1])
            else:
                before_cal_list = string_list_to_int_list(
                    case_dict[x][date_list.index(date[1]):date_list.index(date[0]) - 1])
            count = sum(before_cal_list)
            y_data.append(count)
        elif x == '시간':
            x_data = date_list[date_list.index(date[1]):date_list.index(date[0]) - 1]
            if '사망' in y_axle_list:
                y_data = string_list_to_int_list(
                    death_dict['한국'][date_list.index(date[1]):date_list.index(date[0]) - 1])
            else:
                y_data = string_list_to_int_list(
                    case_dict['한국'][date_list.index(date[1]):date_list.index(date[0]) - 1])

    if info == 'line_graph':
        #print(x_data)
        #print(y_data)
        x_data.reverse()
        y_data.reverse()
        print(x_data)
        print(y_data)
        plt.plot(x_data, y_data)
        plt.xlabel('날짜', fontproperties=fontprop)
        plt.ylabel(y_axle_list[0], fontproperties=fontprop)
        plt.xticks(rotation=0)
        ax = plt.subplot()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(45))

        f = io.BytesIO()
        plt.savefig(f, format='png')
        f.seek(0)

        q = base64.b64encode(f.read()).decode()

        pass
    elif info == 'bar_graph':
        x = np.arange(len(x_data))

        plt.bar(x, y_data)
        ax = plt.subplot()
        ax.set_xticks(x)
        ax.set_xticklabels(x_data,
                           rotation=0, fontproperties=fontprop)

        plt.xticks(x, x_data)

        f = io.BytesIO()
        plt.savefig(f, format='png')
        f.seek(0)

        q = base64.b64encode(f.read()).decode()
    else:
        q = None

    graph_list = [comments, x_data, y_data, info]

    plt.clf()

    return render(request, "graph/chart_detail.html", {'graph_list': graph_list, 'graph':q})