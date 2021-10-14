from django.contrib.admin.widgets import AdminDateWidget , AdminSplitDateTime
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeForm(forms.Form):
    # date_time_input = forms.DateField(widget = DateInput)
    date_time_input = forms.DateTimeField(widget = DateInput)