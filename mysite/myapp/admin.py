from django.contrib import admin
from .models import PersonalDetailsModel, SignUpModel, PersonalEducationDetails, AdditionalEducation,\
    ExperienceAndProjects, SkillsAndTechnology, Document, DocumentDataInJsonFile
# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(SignUpModel)


admin.site.register(PersonalDetailsModel)
admin.site.register(PersonalEducationDetails)
admin.site.register(AdditionalEducation)
admin.site.register(ExperienceAndProjects)
admin.site.register(SkillsAndTechnology)
admin.site.register(Document)
admin.site.register(DocumentDataInJsonFile)
