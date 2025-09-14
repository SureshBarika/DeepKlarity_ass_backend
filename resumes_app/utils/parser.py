import re
import PyPDF2

EMAIL_RE = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
PHONE_RE = re.compile(r'(\+?\d{1,3}[\s-]?)?(?:\d{10}|\d{3}[-\s]\d{3}[-\s]\d{4})')

def extract_text_from_pdf(file_obj):
    reader = PyPDF2.PdfReader(file_obj)
    text = []
    for p in reader.pages:
        text.append(p.extract_text() or "")
    return "\n".join(text)

def extract_contact_fields(text):
    email = EMAIL_RE.search(text)
    phone = PHONE_RE.search(text)
    linkedin = None
    github = None
    for line in text.splitlines():
        l = line.strip()
        if "linkedin.com" in l.lower():
            linkedin = l
        if "github.com" in l.lower():
            github = l
    return {
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "linkedin": linkedin,
        "github": github,
    }

def split_sections(text):
    sections = {}
    current = "header"
    sections[current] = []
    for line in text.splitlines():
        l = line.strip()
        if not l:
            continue
        up = l.upper()
        if any(h in up for h in ["EDUCATION","EXPERIENCE","PROJECT","SKILL","CERTIFICAT","LANGUAGE"]):
            current = up.split()[0].lower()
            sections[current] = []
        else:
            sections[current].append(l)
    for k in sections:
        sections[k] = "\n".join(sections[k])
    return sections

KNOWN_SKILLS = ["html","css","javascript","react","python","node.js","express","sql","postgresql","sqlite","mongodb","c++","git","power bi","excel"]

def parse_skills(section_text):
    found = []
    s = section_text.lower()
    for skill in KNOWN_SKILLS:
        if skill in s:
            found.append(skill)
    return sorted(set(found))
