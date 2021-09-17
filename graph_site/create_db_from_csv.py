import csv, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graph_site.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from graph.models import Graph



def get_data():
    f = open('comment_and_graph.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    next(rdr)
    for i, line in enumerate(rdr):
        Graph(comments=line[0], graph_info=line[1], x_axle=line[3], y_axle=line[4], pub_date=line[2]).save()

if __name__ == "__main__":
    get_data()