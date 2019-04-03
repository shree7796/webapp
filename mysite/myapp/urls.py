# from django.contrib import admin
from django.urls import path
# from django.views.generic.base import TemplateView
from myapp.views import ProfileUpdateView, SignUp, DocumentView, ResumeDetailsView
from myapp.views import EducationUpdateView, EducationAddView, ExperienceAndProjectView, SkillsAndTechnologyView
# from myapp.views import DocumentView

# real_path = DocumentView.file_absolute_path
app_name = 'myapp'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('ProfileUpdateView/<int:pk>/', ProfileUpdateView.as_view(), name='ProfileUpdateView'),
    path('EducationUpdateView/<int:pk>/', EducationUpdateView.as_view(), name='EducationUpdateView'),
    path('ExperienceAndProjects/<int:pk>/', ExperienceAndProjectView.as_view(), name='ExperienceAndProjects'),
    path('SkillsAndTechnologyView/<int:pk>/', SkillsAndTechnologyView.as_view(), name='SkillsAndTechnology'),
    path('AdditionalEducation/<int:pk>/', EducationAddView.as_view(), name='AdditionalEducation'),
    path('fileUpload/<int:pk>/', DocumentView.as_view(), name='Uploadfile'),
    path('UploadedResume/<int:pk>/', ResumeDetailsView.as_view(), name='UploadedResumeDetails'),
    path('fileUpload/<int:url>/', DocumentView.as_view(), name='Uploadfile'),

]
