## DeepSeek Resume Analyzer Backend

This backend is a Django-based application for analyzing resumes. It provides APIs for uploading, parsing, and extracting information from resumes using NLP and LLM techniques.

### Setup Instructions

1. **Clone the repository** and navigate to the `backend` folder:
	```powershell
	cd backend
	```

2. **Create a virtual environment** (recommended):
	```powershell
	python -m venv venv
	.\venv\Scripts\activate
	```

3. **Install dependencies**:
	```powershell
	pip install -r requirements.txt
	```

4. **Apply migrations**:
	```powershell
	python manage.py migrate
	```

5. **(Optional) Load sample data**:
	```powershell
	python load_sample.py
	```

6. **Run the development server**:
	```powershell
	python manage.py runserver
	```

### Folder Structure & Key Files

- `backend/` - Django project settings and configuration
- `resumes_app/` - Main app for resume management and analysis
- `media/resumes/` - Folder for uploaded resumes
- `utils/` - Contains NLP and LLM utilities for resume parsing
- `sample_data/` - Example resumes for testing
- `db.sqlite3` - Default SQLite database
- `requirements.txt` - Python dependencies

### Main Functionalities

- **Resume Upload**: Upload PDF resumes via API.
- **Resume Parsing**: Extracts key information (skills, experience, education) using NLP.
- **LLM Integration**: Uses LLMs for advanced information extraction (see `utils/llm_client.py`).
- **API Endpoints**: Provides RESTful APIs for resume management and analysis (see `resumes_app/views.py`).
- **Admin Panel**: Django admin for managing resumes and extracted data.

### Notes

- Make sure to configure any required environment variables for LLM or NLP services in `settings.py` or via `.env`.
- For production deployment, refer to the `procfile` and update settings as needed.

---
For frontend setup, see the frontend folder's README.
