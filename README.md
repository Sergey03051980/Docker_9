# Docker 9 - Online Learning Platform

## 🚀 Quick Start

```bash
# 1. Setup environment
cp .env.example .env

# 2. Start all services
docker-compose up -d --build

# 3. Create admin user
docker-compose exec backend python manage.py createsuperuser

# 4. Access application
# Main page: http://localhost:8000/
# Admin panel: http://localhost:8000/admin/
```

## 📦 Services

| Service | Port | Status |
|---------|------|--------|
| Django Backend | 8000 | ✅ |
| PostgreSQL | 5432 | ✅ |
| Redis | 6379 | ✅ |
| Celery Worker | - | ✅ |
| Celery Beat | - | ✅ |

## 🛠 Useful Commands

```bash
# Check service status
docker-compose ps

# View logs
docker-compose logs -f backend

# Run Django commands
docker-compose exec backend python manage.py migrate

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

## 📁 Project Structure

- `docker-compose.yaml` - All Docker services
- `Dockerfile` - Backend container
- `.env.example` - Environment template
- `config/` - Django project
- `README.md` - This file
