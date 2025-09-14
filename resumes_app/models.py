from django.db import models

class Resume(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='resumes/')
    filename = models.CharField(max_length=255)
    extracted_text = models.TextField(blank=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    core_skills = models.JSONField(default=list, blank=True)
    soft_skills = models.JSONField(default=list, blank=True)
    languages = models.JSONField(default=list, blank=True)
    education = models.JSONField(default=list, blank=True)
    experience = models.JSONField(default=list, blank=True)
    certifications = models.JSONField(default=list, blank=True)
    projects = models.JSONField(default=list, blank=True)

    resume_rating = models.FloatField(null=True, blank=True)
    improvement_areas = models.TextField(blank=True, null=True)
    upskill_suggestions = models.TextField(blank=True, null=True)
    llm_metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.filename} ({self.name})"
