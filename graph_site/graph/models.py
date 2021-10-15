from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Graph(models.Model):
    comments = models.CharField(max_length=200)
    graph_info = models.CharField(max_length=200)
    x_axle = models.CharField(max_length=200)
    y_axle = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_id = models.IntegerField(default=0)

    def __str__(self):
        return self.comment