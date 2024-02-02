from django.http import Http404
from django.shortcuts import get_object_or_404
from eventCal.models.Events import SubjectEvent, PersonalEvent
from eventCal.models.Semester import Semester


class SubjectFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['title', 'start_time', 'end_time', 'day', 'status', ]
        if request.user.is_superuser:
            self.fields.append('user')
        return super().dispatch(request, *args, **kwargs)


class PersonalFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['title', 'date', 'start_time', 'end_time', ]
        if request.user.is_superuser:
            self.fields.append('user')
        return super().dispatch(request, *args, **kwargs)


class SemesterFieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['name', 'start_date', 'end_date', ]
        if request.user.is_superuser:
            self.fields.append('user')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super().form_valid(form)


class UserAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        subject = get_object_or_404(SubjectEvent, pk=pk)
        if subject.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You don't have access to this page")


class UserPAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        events = get_object_or_404(PersonalEvent, pk=pk)
        if events.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You don't have access to this page")


class UserSAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        semester = get_object_or_404(Semester, pk=pk)
        if semester.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You don't have access to this page")
