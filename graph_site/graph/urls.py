from django.urls import path

from . import views

app_name = 'graph'

urlpatterns = [
    path('', views.chart_bar, name='chart_bar'),
    path('specific/<int:id>', views.graph_specific, name='graph_specific'),
    path('article/<int:post_id>', views.article, name='article'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
]