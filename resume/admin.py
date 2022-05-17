from django.contrib import admin

from resume.models import Education, Experience, PersonalSkill, SoftwareSkill

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonalSkill)
class PersonSkillAdmin(admin.ModelAdmin):
    pass

@admin.register(SoftwareSkill)
class SoftwareSkillAdmin(admin.ModelAdmin):
    pass
