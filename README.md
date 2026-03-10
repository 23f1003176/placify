# Placify
Placify is a comprehensive campus placement management platform designed to connect Students, Companies, and Administrators in a unified, real-time ecosystem.

Here is a short breakdown of what it does:

For Companies: Allows recruiters to create profiles and post "Placement Drives" (job listings) specifying eligibility criteria like minimum CGPA, required branches, and graduation batches.

For Administrators: Provides a dashboard to review and approve incoming job postings, manage user accounts, oversee the ongoing placement processes, and export data/reports (like student applications) asynchronously.

For Students: Offers a portal where students can build profiles, upload details (like CGPA and resumes), view approved job drives they are eligible for, and apply to them directly.

Tech Stack Highlights:

Backend: Built with Python and Flask, utilizing SQLAlchemy (for the SQLite/Postgres database) and Celery + Redis for handling heavy background tasks (like exporting large CSV files).
Frontend: Built with Vue.js 3 and Vite, utilizing Bootstrap 5 for a responsive user interface and Axios for API communication.
Security: Uses JWT (JSON Web Tokens) for stateless, role-based authentication.
