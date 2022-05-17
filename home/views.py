from django.shortcuts import render
from about.models import About

from resume.models import Education, Experience, PersonalSkill, SoftwareSkill

def index(request):
    about = About.objects.first()

    education = Education.objects.order_by('start_date').all()
    experience = Experience.objects.order_by('start_date').all()
    personal_skills = PersonalSkill.objects.all()
    software_skills = SoftwareSkill.objects.all()

    content = {
            'content': {
                'about': about,
                'resume': {
                    'education': education,
                    'experience': experience,
                    'personal_skills': personal_skills,
                    'software_skills': software_skills
                }
            }
        }

    return render(
        request,
        'index.html',
        content
    )
