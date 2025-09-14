# load_sample.py (run from backend root)
import os
import django, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')
django.setup()

from resumes_app.models import Resume
path = os.path.join('sample_data','Suresh_Resume_with_languages1page.pdf')
with open(path,'rb') as f:
    r = Resume.objects.create(
        file=f,
        filename='Suresh_Resume_with_languages1page.pdf',
        extracted_text='-- run parser and update --',
    )
    print("created", r.id)
