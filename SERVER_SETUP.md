# Настройка сервера

## 1. Установите на сервере:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql redis-server git
Настройте проект:
bash
cd /opt
git clone ваш-репозиторий
cd проект
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Настройте Gunicorn и Nginx
См. документацию Django.
