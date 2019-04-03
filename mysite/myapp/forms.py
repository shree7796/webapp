from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import PersonalDetailsModel, PersonalEducationDetails, AdditionalEducation, ExperienceAndProjects,\
    SkillsAndTechnology, Document
# from django_countries import countries
# from django_countries import fields
from django.forms import modelformset_factory


# AdditionalFormSet = modelformset_factory(AdditionalEducation, extra=1)


class SignUpForm(UserCreationForm):
    """
    UserCreationForm class for SignUp Form..
    """
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class PersonalDetailsForm(ModelForm):
    """
    ModelForm class for Personal Details Form..
    """
    DOB = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))
    # current_country = fields.CountryField(countries.name()).formfield()

    class Meta:
        model = PersonalDetailsModel
        fields = '__all__'


class EducationDetailForm(ModelForm):
    """
    ModelForm class for Education Details form..
    """
    year_passing_10th = forms.ChoiceField(choices=[(x, x) for x in range(1990, 2020)])
    year_passing_12th = forms.ChoiceField(choices=[(x, x) for x in range(1990, 2020)])
    year_of_graduation = forms.ChoiceField(choices=[(x, x) for x in range(1990, 2020)])
    subject_in_10th = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 6}))
    subject_in_12th = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 6}))
    course = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 6}))

    class Meta:
        model = PersonalEducationDetails
        fields = '__all__'


class AdditionalEducationForm(ModelForm):
    """
    ModelForm class for Additional Eduction Form..
    """
    course_completion_year = forms.ChoiceField(choices=[(x, x) for x in range(1990, 2020)])
    type_of_course = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))

    class Meta:
        model = AdditionalEducation
        fields = '__all__'


AdditionalFormSet = modelformset_factory(AdditionalEducation, form=AdditionalEducationForm, fields='__all__', extra=1)


class ExperienceAndProjectForm(ModelForm):
    dates_from = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))
    dates_to = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = ExperienceAndProjects
        fields = '__all__'


class SkillsAndTechnologyForm(ModelForm):

    class Meta:
        model = SkillsAndTechnology
        fields = '__all__'


class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ('docFile',)


