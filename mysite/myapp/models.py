from django.db import models
# from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
# from django.contrib.sessions.backends.db import SessionStore
# from django.http import HttpRequest
# from django_countries.fields import CountryField
# from django_countries import fields
# Create your models here.


class Country(models.Model):
    name = models.TextField(max_length=50)
    # country = CountryField().formfield()

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SignUpModel(models.Model):
    """
    Sign up  model class

    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)


class PersonalDetailsModel(models.Model):
    """
    Personal Details model class
    User's personal details like first name, last name and Address etc...
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    Mob = models.CharField(default='', max_length=13)
    DOB = models.DateField(null=True)
    Gender = models.CharField(max_length=10, default='', null=True, choices=(('M', 'male'), ('F', 'Female'), ('N', 'N/A'
                                                                                                              )))
    Zip_code = models.IntegerField(null=True)
    Address = models.CharField(null=True, max_length=100)
    objects = models.Manager()

    def __str__(self):
        """
        This function save user's data to database by user name
        :return: user name
        """
        return self.user


class PersonalEducationDetails(models.Model):
    """
    This Class has user's Educational details..
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_passing_10th = models.IntegerField(null=True)
    board_10th = models.CharField(max_length=50, default='')
    subject_in_10th = models.CharField(max_length=50, default='', null=True)
    cgpa_in_10th = models.FloatField(null=True)
    year_passing_12th = models.IntegerField(null=True)
    board_12th = models.CharField(max_length=50, default='')
    subject_in_12th = models.CharField(max_length=50, default='', null=True)
    cgpa_in_12th = models.FloatField(null=True)
    year_of_graduation = models.IntegerField(null=True)
    university = models.CharField(max_length=500, default='')
    course = models.CharField(max_length=500, default='')
    subject = models.CharField(max_length=50, default='', null=True)
    cgpa = models.FloatField(null=True)
    objects = models.Manager()

    def __str__(self):
        """

        :return:
        """
        return self.user


class AdditionalEducation(models.Model):
    """
    Additional Education Class
    This model class has user's Additional Education in case he want's to add more..
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_course = models.TextField(default='', null=True)
    duration = models.IntegerField(default=3, null=True)
    university = models.CharField(default='', max_length=100)
    course_completion_year = models.IntegerField(null=True)
    subject = models.CharField(default='', max_length=100)
    aggregate_percentage = models.FloatField(null=True)
    objects = models.Manager()

    def __str__(self):
        """

        :return:
        """
        return self.user


class ExperienceAndProjects(models.Model):
    """
    Experience And Projects Model Class
    This model class has user's previous work experience and projects details fields..
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.FloatField(null=True)
    Company = models.CharField(max_length=500, default='')
    type_of_industry = models.CharField(max_length=500, default='')
    dates_from = models.DateField(null=True)
    dates_to = models.DateField(null=True)
    job_title = models.CharField(null=True, max_length=100)
    salary = models.IntegerField(null=True)
    project_title = models.CharField(default='', max_length=500)
    project_description = models.TextField(default='', max_length=1000)
    objects = models.Manager()

    def __str__(self):
        """

        :return:
        """
        return self.user


class SkillsAndTechnology(models.Model):
    """
    Skills And Technology model
    This model class has Skills and technology fields..
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=300, default='')
    servers = models.CharField(max_length=300, default='')
    databases = models.CharField(max_length=300, default='')
    other = models.CharField(max_length=500, default='')
    objects = models.Manager()

    def __str__(self):
        """

        :return:
        """
        return self.user


file_path = []


def user_directory_path(instance, filename):
    path = 'user_{0}/{1}'.format(instance.user.id, filename)
    file_path.append(path)
    print("user id---->", path)
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Document(models.Model):
    """
    This model class is to upload documents and save them..
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    docFile = models.FileField(upload_to=user_directory_path)
    Upload_at = models.DateField(auto_now=True)
    objects = models.Manager()

    # def __str__(self):
    #     """
    #
    #     :return:
    #     """
    #     return self.docFile


class DocumentDataInJsonFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documentData = models.TextField(default='')
    # data = JSONField(null=True)
    objects = models.Manager()

