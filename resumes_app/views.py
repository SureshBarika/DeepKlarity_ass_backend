from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Resume
from .serializers import ResumeSerializer
from .utils import parser, llm_client, nlp_extract


class UploadResume(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        file_obj = request.FILES.get("file")
        if not file_obj:
            return Response({"error": "No file uploaded"}, status=400)

        filename = file_obj.name
        text = parser.extract_text_from_pdf(file_obj)

        contact = parser.extract_contact_fields(text)
        sections = parser.split_sections(text)
        skills = parser.parse_skills(sections.get("skills", text))
        name = nlp_extract.extract_name(text)

        structured = {
            "name": name,
            "contact": contact,
            "sections": sections,
            "skills": skills,
        }

        llm_result = llm_client.call_llm_for_analysis(text, structured)

        resume = Resume.objects.create(
            file=file_obj,
            filename=filename,
            extracted_text=text,
            name=name,
            email=contact.get("email"),
            phone=contact.get("phone"),
            linkedin=contact.get("linkedin"),
            github=contact.get("github"),
            core_skills=skills,
            llm_metadata={"raw": llm_result},
            resume_rating=llm_result.get("resume_rating"),
            improvement_areas="\n".join(llm_result.get("improvement_areas", [])),
            upskill_suggestions="\n".join(llm_result.get("upskill_suggestions", [])),
        )
        serializer = ResumeSerializer(resume)
        return Response(serializer.data, status=201)


class ResumeList(ListAPIView):
    queryset = Resume.objects.all().order_by("-uploaded_at")
    serializer_class = ResumeSerializer


class ResumeDetail(RetrieveAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
