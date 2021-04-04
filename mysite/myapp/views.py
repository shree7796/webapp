from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignUpForm
from django.urls import reverse_lazy, reverse
from .forms import PersonalDetailsForm, EducationDetailForm, AdditionalEducationForm, ExperienceAndProjectForm,\
    AdditionalFormSet, SkillsAndTechnologyForm, DocumentForm
from .models import PersonalDetailsModel, PersonalEducationDetails, AdditionalEducation, ExperienceAndProjects,\
    SkillsAndTechnology, Document, DocumentDataInJsonFile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here


class SignUp(CreateView):
    """
    Sign up view..
    """
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileUpdateView(UpdateView):
    model = PersonalDetailsModel
    form_class = PersonalDetailsForm
    template_name = 'PersonalInfoForm.html'

    def dispatch(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = kwargs['pk']
        self.user = get_object_or_404(User, pk=user_id)
        self.object = self.get_object()
        print('My class get method called')
        return super().dispatch(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     user_id = kwargs['pk']
    #     self.user = get_object_or_404(User, pk=user_id)
    #     self.object = self.get_object()
    #     print('My class get method called')
    #     return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """

        :param queryset:
        :return:
        """
        try:
            return PersonalDetailsModel.objects.get(user=self.user)
        except PersonalDetailsModel.DoesNotExist:
            profile = PersonalDetailsModel(user=self.user)
            profile.save()
            return profile

    def get_success_url(self):
        """

        :return:
        """
        user_id = self.user.id
        # return reverse('ProfileUpdateView', kwargs={'pk': user_id})
        return reverse_lazy('myapp:EducationUpdateView', kwargs={'pk': user_id})


class EducationUpdateView(UpdateView):
    model = PersonalEducationDetails
    form_class = EducationDetailForm
    template_name = 'EducationDetails.html'

    def dispatch(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = kwargs['pk']
        self.user = get_object_or_404(User, pk=user_id)
        self.object = self.get_object()
        print('Education class get method called')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """

        :param queryset:
        :return:
        """
        try:
            print('Try block called')
            return PersonalEducationDetails.objects.get(user=self.user)
        except PersonalEducationDetails.DoesNotExist:
            print('Except block called')
            profile = PersonalEducationDetails(user=self.user)
            profile.save()
            return profile

    def get_success_url(self):
        """

        :return:
        """
        user_id = self.user.id
        return reverse_lazy('myapp:ExperienceAndProjects', kwargs={'pk': user_id})


class EducationAddView(CreateView):
    model = AdditionalEducation
    form_class = AdditionalEducationForm
    template_name = 'AdditionalEducation.html'

    def dispatch(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        self.user = get_object_or_404(User, pk=user_id)
        # self.object = self.get_object()
        print('My class get method called')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return AdditionalEducation.objects.get(user=self.user)
        except AdditionalEducation.DoesNotExist:
            profile = AdditionalEducation(user=self.user)
            profile.save()
            return profile, self.form_class

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        user_id = self.user.id
        # return reverse('ProfileUpdateView', kwargs={'pk': user_id})
        return reverse_lazy('myapp:AdditionalEducation', kwargs={'pk': user_id})


class ExperienceAndProjectView(CreateView):
    model = ExperienceAndProjects
    form_class = ExperienceAndProjectForm
    template_name = 'ExperienceAndProjects.html'

    def dispatch(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        self.user = get_object_or_404(User, pk=user_id)
        # self.object = self.get_object()
        print('My class get method called')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return AdditionalEducation.objects.get(user=self.user)
        except ExperienceAndProjects.DoesNotExist:
            profile = ExperienceAndProjects(user=self.user)
            profile.save()
            return profile

    def get_success_url(self):
        user_id = self.user.id
        return reverse_lazy('myapp:SkillsAndTechnology', kwargs={'pk': user_id})


class SkillsAndTechnologyView(CreateView):
    model = SkillsAndTechnology
    form_class = SkillsAndTechnologyForm
    template_name = 'skillsandtechnology.html'

    def dispatch(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        self.user = get_object_or_404(User, pk=user_id)
        print('My class get method called')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return SkillsAndTechnology.objects.get(user=self.user)
        except SkillsAndTechnology.DoesNotExist:
            profile = SkillsAndTechnology(user=self.user)
            profile.save()
            return profile

    def get_success_url(self):
        user_id = self.user.id
        return reverse_lazy('myapp:SkillsAndTechnology', kwargs={'pk': user_id})


class DocumentView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'fileUpload.html'
    file_absolute_path = []
    print("print", file_absolute_path)

    def dispatch(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        self.user = get_object_or_404(User, pk=user_id)
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            return Document.objects.get(user=self.user)
        except Document.DoesNotExist:
            profile = Document(user=self.user)
            profile.save()
            return profile

    def current_pdf_view(self):
        post = self.file_absolute_path[0]
        return post

    def get_success_url(self):
        user_id = self.user.id
        from .script import OpenPdfFileAndExtractFields  # import module(script.py) only when required
        file_path = Document.objects.get(user=self.user)
        file_url = file_path.docFile.path
        self.file_absolute_path.append(file_url)
        print("url --------->", file_path.docFile.url)
        obj = OpenPdfFileAndExtractFields()
        # obj.name()
        obj.email()
        obj.mobile_no()
        obj.experience()
        obj.skills()
        obj.education()
        obj.address()
        obj.jsonfile()

        return reverse_lazy('myapp:UploadedResumeDetails', kwargs={'pk': user_id})

    def pdf_view(self):
        from django.http import FileResponse, Http404
        try:
            return FileResponse(open(self.file_absolute_path[0], 'wb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404


class DocumentDataInJsonFormat(UpdateView):
    pass


class ResumeDetailsView(CreateView):
    model = PersonalDetailsModel
    form_class = PersonalDetailsForm
    template_name = 'UploadedResumeDetailsView.html'
    success_url = reverse_lazy('UploadedResumeDetailsView')

    # def dispatch(self, request, *args, **kwargs):
    #     user_id = kwargs['pk']
    #     self.user = get_object_or_404(User, pk=user_id)
    #     self.object = self.get_object()
