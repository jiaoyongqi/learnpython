#!/usr/bin/python
#-*-coding:UTF-8-*-

from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
