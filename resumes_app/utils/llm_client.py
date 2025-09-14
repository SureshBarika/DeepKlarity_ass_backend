import json

LLM_PROMPT = """
You are a resume reviewer. Given the resume text and extracted data,
return JSON only in this schema:

{
  "resume_rating": float,
  "improvement_areas": ["..."],
  "upskill_suggestions": ["..."]
}
"""

def call_llm_for_analysis(resume_text, structured_json):
    # Normally call Gemini API here using LangChain or google-generativeai
    # For development/demo, return mock data
    return {
        "resume_rating": 7.5,
        "improvement_areas": [
            "Add quantified achievements to work experience.",
            "Include a professional summary at the top.",
            "Highlight technical projects in more detail.",
        ],
        "upskill_suggestions": [
            "Learn TypeScript for stronger React apps.",
            "Practice SQL query optimization.",
            "Add unit testing experience with Jest or Pytest.",
        ],
    }
