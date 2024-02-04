from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field
from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator
from .models.Semester import Semester
from datetime import timedelta

class EventQueryForm(forms.Form):
    start_date = forms.DateField(label='تاریخ شروع')
    end_date = forms.DateField(label='تاریخ پایان')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError('تاریخ شروع نباید بزرگتر از تاریخ پایان باشد.')

        return cleaned_data