from django.urls import path
from .views import UploadResume, ResumeList, ResumeDetail

urlpatterns = [
    path("upload/", UploadResume.as_view(), name="upload_resume"),
    path("", ResumeList.as_view(), name="resume_list"),
    path("<int:pk>/", ResumeDetail.as_view(), name="resume_detail"),
]
