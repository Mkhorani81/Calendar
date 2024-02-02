from django.urls import path
from .views import DailySubjectReport,OddWeekSubjectReport,EvenWeekSubjectReport,DailyPersonalReport,PeriodPersonalEvent


app_name = 'eventCal'

urlpatterns = [
    path('dailysubreport',DailySubjectReport.as_view(),name='dailysubreport'),
    path('even',EvenWeekSubjectReport.as_view(),name='even'),
    path('odd',OddWeekSubjectReport.as_view(),name='odd'),
    path('dailypersonalevent',DailyPersonalReport.as_view(),name='dailypersonalevent'),
    path('periodpersonalevent',PeriodPersonalEvent.as_view(),name='periodpersonalevent')
]