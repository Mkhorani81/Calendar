from django.urls import path
from django.contrib.auth import views
from account.views import (
    AllSubject,
    AllPersonal,
    AllSemester,
    SubjectCreate,
    PersonalCreate,
    SubjectUpdate,
    PersonalUpdate,
    SubjectDelete,
    PersonalDelete,
    SemesterCreate,
    SemesterUpdate
)

app_name = 'account'

urlpatterns = [

    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    # path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done",),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    # path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    # path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
]

urlpatterns += [
    path('', AllSubject.as_view(), name='home'),
    path('allpersonal', AllPersonal.as_view(), name='allpersonal'),
    path('semester', AllSemester.as_view(), name='semester'),
    path('updatesubject/<int:pk>', SubjectUpdate.as_view(), name='updatesubject'),
    path('updatepersonal/<int:pk>', PersonalUpdate.as_view(), name='updatepersonal'),
    path('updatesemester/<int:pk>', SemesterUpdate.as_view(), name='updatesemester'),
    path('deletesubject/<int:pk>', SubjectDelete.as_view(), name='deletesubject'),
    path('deletepersonal/<int:pk>', PersonalDelete.as_view(), name='deletepersonal'),
    path('createpersonal/', PersonalCreate.as_view(), name='createpersonal'),
    path('createsubject/', SubjectCreate.as_view(), name='createsubject'),
    path('createsemester/', SemesterCreate.as_view(), name='createsemester'),
]
