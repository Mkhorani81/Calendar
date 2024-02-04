from django.urls import path
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
    SemesterUpdate,
    Profile,

)

app_name = 'account'


urlpatterns = [
    path('', AllSubject.as_view(), name='home'),
    path('allpersonal', AllPersonal.as_view(), name='allpersonal'),
    path('semester', AllSemester.as_view(), name='semester'),
    path('updatesubject/<int:pk>', SubjectUpdate.as_view(), name='updatesubject'),
    path('updatepersonal/<int:pk>', PersonalUpdate.as_view(), name='updatepersonal'),
    path('updatesemester/<int:pk>', SemesterUpdate.as_view(), name='updatesemester'),
    path('deletesubject/<int:pk>', SubjectDelete.as_view(), name='deletesubject'),
    path('deletepersonal/<int:pk>', PersonalDelete.as_view(), name='deletepersonal'),
    path('profile/', Profile.as_view(), name='profile'),
    path('createpersonal/', PersonalCreate.as_view(), name='createpersonal'),
    path('createsubject/', SubjectCreate.as_view(), name='createsubject'),
    path('createsemester/', SemesterCreate.as_view(), name='createsemester'),
]
