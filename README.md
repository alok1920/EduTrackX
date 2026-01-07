EduTrackX/
│
├── services/                    ← ALL applications live here
│   ├── backend_api/             ← FASTAPI (Backend)
│   │   └── app/
│   │       ├── main.py           ← FastAPI starts here
│   │       ├── schemas.py        ← Data validation rules
│   │       ├── models.py         ← Database table structure
│   │       ├── crud.py           ← Create, Read, Update, Delete logic
│   │       └── database.py       ← Database connection
│   ├── admin_portal/             ← FLASK (Admin website)
│   │   ├── app.py                ← Flask app starts here
│   │   ├── templates/            ← HTML files
│   │   │   ├── login.html
│   │   │   └── dashboard.html
│   └── data_dashboard/           ← STREAMLIT (Charts)
│       └── app.py                ← Streamlit app starts here
├── pyproject.toml                ← Poetry dependencies
└── README.md
