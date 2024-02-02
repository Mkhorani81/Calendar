from django.views.generic import ListView
from django.db.models import Q
from .models.Events import SubjectEvent, PersonalEvent
from jdatetime import datetime
from django.utils import timezone
from .forms import EventQueryForm
from django.shortcuts import get_object_or_404


class DailySubjectReport(ListView):
    # paginate_by = 6
    model = SubjectEvent
    template_name = 'calendar/daily_subject_report.html'
    context_object_name = 'dailysubreport'

    def get_queryset(self):
        current_user = self.request.user
        current_day = datetime.now().weekday()
        queryset = SubjectEvent.objects.daily_report().filter(user=current_user, day=str(current_day)).order_by(
            'status')
        return queryset


class EvenWeekSubjectReport(ListView):
    model = SubjectEvent
    template_name = 'calendar/even_week_subject_report.html'
    context_object_name = 'even_week_subreport'

    def get_queryset(self):
        current_user = self.request.user
        queryset = SubjectEvent.objects.even_week_report().filter(user=current_user).order_by('day', 'start_time',
                                                                                              'end_time')
        return queryset


class OddWeekSubjectReport(ListView):
    model = SubjectEvent
    template_name = 'calendar/odd_week_subject_report.html'
    context_object_name = 'odd_week_subreport'

    def get_queryset(self):
        current_user = self.request.user
        queryset = SubjectEvent.objects.odd_week_report().filter(user=current_user).order_by('day', 'start_time',
                                                                                             'end_time')
        return queryset


class DailyPersonalReport(ListView):
    model = PersonalEvent
    template_name = 'calendar/daily_personal_event.html'
    context_object_name = 'dailypersonalevent'

    def get_queryset(self):
        current_user = self.request.user
        queryset = PersonalEvent.objects.filter(user=current_user, date=timezone.now().date()).order_by('date',
                                                                                                        'start_time',
                                                                                                        'end_time')

        return queryset


class PeriodPersonalEvent(ListView):
    model = PersonalEvent
    template_name = 'calendar/period_personal_event.html'
    context_object_name = 'periodpersonalevent'

    def get_queryset(self):
        current_user = self.request.user
        form = EventQueryForm(self.request.GET)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            queryset = PersonalEvent.objects.filter(user=current_user, date__gte=start_date,
                                                    date__lte=end_date).order_by('date',
                                                                                 'start_time',
                                                                                 'end_time')
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventQueryForm(self.request.GET)
        return context
