import codecs, csv

def create_user_dic():
    f = open("user_dic.txt", 'w')
    with codecs.open('dictionary.csv', 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        next(rd)
        for line in rd:
            for number, noun in enumerate(line):
                if noun == "":
                    pass
                elif number == 0:
                    pass
                else:
                    data = ""
                    data += noun
                    data += "\t"
                    data += "NNP"
                    data += "\n"
                    f.write(data)
    f.close()

def dic_creating():
    syn_dict = {}
    state_dict = {}
    with codecs.open('./external/dictionary.csv', 'r', encoding='utf-8') as csvf:
        rd = csv.reader(csvf)
        next(rd)
        for line in rd:
            state = ""
            for number, noun in enumerate(line):
                if noun == "":
                    pass
                elif number == 0:
                    state = noun
                elif number == 1:
                    syn_dict[noun] = noun
                    state_dict[noun] = state
                else:
                    syn_dict[noun] = line[1]
                    state_dict[noun] = state
    return syn_dict, state_dict

if __name__ == "__main__":
    create_user_dic()

