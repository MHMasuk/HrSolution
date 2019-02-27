from django import forms
from .models import Entry
import datetime


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('project', 'task_date', 'location', 'detail', 'working_hour', 'is_cod', 'note')

    def clean(self):
        cleaned_data = super(EntryForm, self).clean()
        task_date = cleaned_data.get("task_date")
        today = datetime.datetime.today()
        print(today)
        if task_date == datetime.datetime.today():
            raise forms.ValidationError("You need to give today entry.")
        return cleaned_data
