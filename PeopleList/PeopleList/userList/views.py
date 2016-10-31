from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import User, Skill
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'userList/index.html'

    def get_queryset(self):
        return User.objects.all()


class SkillListView(generic.DetailView):
    model = User
    template_name = 'userList/detail.html'

    
