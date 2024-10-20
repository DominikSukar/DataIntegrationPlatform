# Real-time Data Integration Platform
The platform retrieves and processes live data from Riot Games' public API, stores it in a custom-built database, and
presents detailed insights through an interactive frontend interface. 

Project is still being developed, currently frontend fetches most of the data directly from Riot Games API.

## 🔍 Project Structure
```
.
├── backend/                        # FastAPI backend
│   ├── api_requests/               # API request handlers
│   │   └── mappers/                # Key mappers between Riot's API and database
│   ├── database/                   # Database configuration
│   │   └── models/                 # Models of database tables and relationships
│   ├── middleware/                 # Middlewares
│   ├── routers/                    # API routes
│   ├── routers_services/database/  # Services for specific routers
│   ├── serializers/                # Type hinters and serializers for routers
│   ├── tests/                      # Tests
│   ├── utils/                      # General utility functions
├── frontend/                       # Next.js 14 frontend
│   ├── __tests__/                  # Currently empty tests directory
│   ├── app/                        # Next.js app router pages
│   ├── components/                 # Reusable React components
│   ├── constants/                  # Constant values and configurations
│   ├── contexts/                   # React context providers
│   ├── public/                     # Static files and assets
│   ├── types/                      # TypeScript type definitions
│   ├── utils/                      # Utility functions
│   ├── README.md                   # Frontend documentation
└── README.md                       # Main project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12.7
- Node.js 20.11.0
- PostgreSQL 16.4

### Installation

1. Clone the repository

2. Set up backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up frontend (Next.js)
```bash
cd frontend
npm install
```

4. Environment Variables
- Backend:
```
API_KEY=
DATABASE_LOGIN=
DATABASE_PASSWORD=
DATABASE_URL=


ITEMS_PATH=
SUMMONERS_PATH=
PERKS_PATH=

DOMAIN_EUROPE=
DOMAIN_AMERICAS=
DOMAIN_ASIA=
DOMAIN_SEA=
DOMAIN_ESPORTS=
DOMAIN_BR=
DOMAIN_EUNE=
DOMAIN_EUW=
DOMAIN_JP=
DOMAIN_KR=
DOMAIN_LAN=
DOMAIN_LAS=
DOMAIN_ME=
DOMAIN_NA=
DOMAIN_OCE=
DOMAIN_PH=
DOMAIN_RU=
DOMAIN_SG=
DOMAIN_TH=
DOMAIN_TR=
DOMAIN_TW=
DOMAIN_VN=
```
- Database: 
```
DB_USER=
DB_PASSWORD=
DB_NAME=
```

## 🛠️ Development

### Running Backend
```bash
cd backend
.\venv\Scripts\activate
python -m uvicorn main:app --reload
```
Backend runs on: http://localhost:8000

### Running Frontend
```bash
cd frontend
npm run dev
```
Frontend runs on: http://localhost:3000

## 📚 API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing
```bash
cd backend
python -m pytest

```
---