from django.contrib.auth import login
from account.models import UserInfo
from django.http import HttpResponse
from account.forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_str, force_bytes
from django.contrib.auth.views import LoginView
from account.forms import CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from eventCal.models.Events import SubjectEvent, PersonalEvent
from eventCal.models.Semester import Semester
from account.mixins import (
    SubjectFieldMixin,
    PersonalFieldMixin,
    FormValidMixin,
    UserAccessMixin,
    UserPAccessMixin,
    SemesterFieldMixin,
    UserSAccessMixin)


# ----------------------SUBJECTS EVENT------------------------------------------------------

class SubjectCreate(LoginRequiredMixin, SubjectFieldMixin, FormValidMixin, CreateView):
    model = SubjectEvent
    template_name = 'calendar/subject-create-update.html'


class SubjectUpdate(UserAccessMixin, SubjectFieldMixin, FormValidMixin, UpdateView):
    model = SubjectEvent
    template_name = 'calendar/subject-create-update.html'


class SubjectDelete(UserAccessMixin, DeleteView):
    model = SubjectEvent
    success_url = reverse_lazy("account:home")
    template_name = 'calendar/subjectevent_confirm_delete.html'


# ----------------------PERSONAL EVENT----------------------------
class PersonalCreate(LoginRequiredMixin, PersonalFieldMixin, FormValidMixin, CreateView):
    model = PersonalEvent
    template_name = 'calendar/personal-create-update.html'


class PersonalUpdate(UserPAccessMixin, PersonalFieldMixin, FormValidMixin, UpdateView):
    model = PersonalEvent
    template_name = 'calendar/personal-create-update.html'


class PersonalDelete(UserPAccessMixin, DeleteView):
    model = PersonalEvent
    success_url = reverse_lazy("account:allpersonal")
    template_name = 'calendar/personalevent_confirm_delete.html'


# -------------------------SEMESTER-----------------------------
class SemesterCreate(LoginRequiredMixin, SemesterFieldMixin, FormValidMixin, CreateView):
    model = Semester
    template_name = 'calendar/semester-create-update.html'


class SemesterUpdate(UserSAccessMixin, SemesterFieldMixin, FormValidMixin, UpdateView):
    model = Semester
    template_name = 'calendar/semester-create-update.html'


# ------------------------------------------------------

class AllSubject(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        current_user = self.request.user
        return SubjectEvent.objects.filter(user=current_user).order_by('day', 'status')


class AllPersonal(LoginRequiredMixin, ListView):
    template_name = 'registration/allpersonal.html'

    def get_queryset(self):
        current_user = self.request.user
        return PersonalEvent.objects.filter(user=current_user).order_by('date', 'start_time', 'end_time')


class AllSemester(LoginRequiredMixin, ListView):
    template_name = 'registration/semester.html'

    def get_queryset(self):
        current_user = self.request.user
        return Semester.objects.filter(user=current_user).order_by('name', 'start_date', 'end_date')


# ------------------------------------------------------------------

class Register(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse("لینک فعالسازی به ایمیل شما ارسال شد، بعد از فعالسازی میتوانید به حساب خود وارد شوید.")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserInfo.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserInfo.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('اکانت شما با موفقیت فعال شد، اکنون میتوانید به خساب خود وارد شوید.')
    else:
        return HttpResponse('لینک فعالسازی منقضی شده است،فرآیند ثبت نام خود را مجددا انجام دهید.')


class Login(LoginView):
    form_class = CustomLoginForm

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)
