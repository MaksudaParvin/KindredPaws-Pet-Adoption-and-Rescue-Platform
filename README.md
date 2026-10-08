# 🐾 Pet Adoption & Rescue API

A Django REST Framework (DRF) based REST API for managing pets, user adoption requests, authentication, and adoption workflows.

The project provides JWT-based authentication, pet management, adoption request management, search, filtering, pagination, and role-based access control for users and administrators.

## ✨ Features

### 🔐 Authentication
- User registration
- JWT-based login
- Access and refresh tokens
- JWT token refresh
- Authenticated user profile
- Protected API endpoints

### 🐶 Pet Management
- List available pets
- Retrieve pet details
- Admin can create pets
- Admin can update pets
- Admin can delete pets
- Pet image upload
- Adoption status management

### 📝 Adoption Requests
- Authenticated users can submit adoption requests
- Users can view only their own requests
- Admins can view all adoption requests
- Prevents applications for adopted/unavailable pets
- Prevents duplicate active requests for the same pet
- Users cannot approve their own requests
- Admins can approve or reject requests
- Approving a request automatically marks the pet as adopted
- Other pending requests for the adopted pet are automatically rejected

### 🔎 Search, Filtering & Ordering
- Search pets by:
  - Name
  - Breed
  - Animal type
  - Location
- Filter by:
  - Animal type
  - Gender
  - Location
  - Adoption status
- Order by:
  - Name
  - Age
  - Created date

### 📄 Pagination
- API pagination using DRF `PageNumberPagination`
- Default page size: 6 pets per page

### 👮 Role-Based Access
- Public users can browse pets
- Authenticated users can submit adoption requests
- Users can access only their own adoption requests
- Staff/admin users can manage pets
- Staff/admin users can manage adoption requests

---

## 🛠️ Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- django-filter
- Pillow

---

## 📁 Project Structure

```text
pet-adoption-rescue/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── adoption/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MaksudaParvin/KindredPaws-Pet-Adoption-and-Rescue-Platform.git
cd "KindredPaws-Pet-Adoption-and-Rescue-Platform"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure PostgreSQL

Create a PostgreSQL database, for example:

```text
Database: pet_adoption_db
```

Update your database configuration in:

```text
config/settings.py
```

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pet_adoption_db",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create an admin user

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🔗 API Endpoints

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| POST | `/api/auth/register/` | Public | Register user |
| POST | `/api/auth/login/` | Public | Obtain JWT tokens |
| POST | `/api/auth/token/refresh/` | Public | Refresh access token |
| GET | `/api/auth/profile/` | Authenticated | View profile |
| GET | `/api/pets/` | Public | List pets |
| POST | `/api/pets/` | Admin | Create pet |
| GET | `/api/pets/<id>/` | Public | Pet details |
| PUT | `/api/pets/<id>/` | Admin | Update pet |
| PATCH | `/api/pets/<id>/` | Admin | Partial update |
| DELETE | `/api/pets/<id>/` | Admin | Delete pet |
| GET | `/api/adoptions/` | Authenticated | List adoption requests |
| POST | `/api/adoptions/` | Authenticated | Submit adoption request |
| GET | `/api/adoptions/<id>/` | Owner/Admin | Request details |
| PUT | `/api/adoptions/<id>/` | Owner/Admin | Update request |
| PATCH | `/api/adoptions/<id>/` | Owner/Admin | Partial update |
| DELETE | `/api/adoptions/<id>/` | Owner/Admin | Delete request |

---

# 🧪 Testing

The API can be tested using tools such as:

- Postman
- Insomnia
- Thunder Client
- DRF Browsable API

Recommended testing flow:

```text
1. Register user
       ↓
2. Login
       ↓
3. Copy JWT access token
       ↓
4. Create/administer pets
       ↓
5. Browse pets
       ↓
6. Submit adoption request
       ↓
7. Login as admin
       ↓
8. Review adoption requests
       ↓
9. Approve/reject request
       ↓
10. Verify pet adoption status
```

---

# 🔐 Environment Variables

For production, sensitive configuration such as database credentials and secret keys should be stored in environment variables instead of directly in `settings.py`.

Example:

```text
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=pet_adoption_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

# 🚀 Future Improvements

Possible future enhancements:
- Frontend integration


---

# 👩‍💻 Author

**Maksuda Parvin**

B.Sc. in Computer Science and Engineering

---

## 📄 License

This project is developed for educational and portfolio purposes.