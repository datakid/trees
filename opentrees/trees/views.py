from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Tree

class TreeList(ListView):
    model = Tree

class TreeDetail(DetailView):
    model = Tree

class TreeCreate(CreateView):
    model = Tree

class TreeUpdate(UpdateView):
    model = Tree

class TreeDelete(DeleteView):
    model = Tree

    
