from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.views import generic

from logEntry.forms import EntryForm
from logEntry.models import Entry


class EntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'log_entry/create_entry.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EntryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Entry
    template_name = 'log_entry/entry_detail.html'


def entry_list(request, user):
    user = User.objects.get(username=request.user)
    name = user.username
    entry_list = Entry.objects.filter(user__username=name)
    return render(request, 'log_entry/entry_list.html', {'entry_list': entry_list})


