import re

def parse_poetry_lock():
    """Parse poetry.lock and extract package versions"""
    try:
        with open('poetry.lock', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("poetry.lock not found, creating basic requirements")
        return {}
    
    # Находим все пакеты и их версии
    packages = re.findall(r'name = "([^"]+)"\s+version = "([^"]+)"', content)
    
    return dict(packages)

def main():
    packages = parse_poetry_lock()
    
    # Основные зависимости
    main_packages = [
        'Django', 'djangorestframework', 'django-cors-headers',
        'celery', 'redis', 'psycopg2-binary', 'gunicorn',
        'django-celery-beat', 'python-dotenv'
    ]
    
    # Dev зависимости (включая flake8)
    dev_packages = ['pytest', 'pytest-django', 'flake8']
    
    # Пишем requirements.txt
    with open('requirements.txt', 'w') as f:
        for pkg in main_packages:
            pkg_lower = pkg.lower()
            if pkg_lower in packages:
                f.write(f"{pkg_lower}=={packages[pkg_lower]}\n")
            else:
                # Fallback если нет в poetry.lock
                f.write(f"{pkg_lower}\n")
    
    # Пишем requirements-dev.txt
    with open('requirements-dev.txt', 'w') as f:
        for pkg in dev_packages:
            pkg_lower = pkg.lower()
            if pkg_lower in packages:
                f.write(f"{pkg_lower}=={packages[pkg_lower]}\n")
            else:
                # Fallback если нет в poetry.lock
                f.write(f"{pkg_lower}\n")
    
    print("Generated requirements.txt and requirements-dev.txt")

if __name__ == '__main__':
    main()
