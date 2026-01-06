import re

def parse_poetry_lock():
    """Parse poetry.lock and extract package versions"""
    with open('poetry.lock', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Находим все пакеты и их версии
    packages = re.findall(r'name = "([^"]+)"\s+version = "([^"]+)"', content)
    
    return dict(packages)

def main():
    packages = parse_poetry_lock()
    
    # Основные зависимости (исключаем dev и python)
    main_packages = [
        'Django', 'djangorestframework', 'django-cors-headers',
        'celery', 'redis', 'psycopg2-binary', 'gunicorn',
        'django-celery-beat', 'python-dotenv'
    ]
    
    # Dev зависимости
    dev_packages = ['pytest', 'pytest-django']
    
    # Пишем requirements.txt
    with open('requirements.txt', 'w') as f:
        for pkg in main_packages:
            if pkg.lower() in packages:
                f.write(f"{pkg}=={packages[pkg.lower()]}\n")
            elif pkg in packages:
                f.write(f"{pkg}=={packages[pkg]}\n")
    
    # Пишем requirements-dev.txt
    with open('requirements-dev.txt', 'w') as f:
        for pkg in dev_packages:
            if pkg.lower() in packages:
                f.write(f"{pkg}=={packages[pkg.lower()]}\n")
            elif pkg in packages:
                f.write(f"{pkg}=={packages[pkg]}\n")
    
    print("Generated requirements.txt and requirements-dev.txt")

if __name__ == '__main__':
    main()
