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
    fields = ['lat', 'lon', 'genus', 'species', 'dbh', 'ule_min', 'ule_max', 'crown', 'height', 'common', 'location', 'ref', 'maintenance_schedule', 'last_maintenance', 'maturity', 'planted', 'captured', 'health', 'structure']

class TreeUpdate(UpdateView):
    model = Tree

class TreeDelete(DeleteView):
    model = Tree

    
