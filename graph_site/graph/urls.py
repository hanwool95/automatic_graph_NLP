from django.urls import path

from . import views

app_name = 'graph'

urlpatterns = [
    path('', views.chart_bar, name='chart_bar'),
    path('specific/<int:id>', views.graph_specific, name='graph_specific'),
]