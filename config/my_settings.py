DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysqlclient 라이브러리 설치
        'NAME': 'itrencotech',      # 생성한 database의 이름
        'USER': 'root',
        'PASSWORD': '1234',     # mariaDB 설치 시 입력한 root 비밀번호 입력
        'HOST': 'localhost',
        'PORT': '3306',          # Port 번호
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        }
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = {
    'secret': 'h@_vy0dzo!$r03cv*-ff2%+%#62vy_l$zsu0_^8+qtyh)01zov',
}

EMAIL = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_USE_TLS': True,  # TLS 보안 설정
    'EMAIL_PORT': '587',
    'EMAIL_HOST': 'smtp.gmail.com',
    'EMAIL_HOST_USER': 'kodealtest@gmail.com',
    'EMAIL_HOST_PASSWORD': '!zhelf17?',
    'SERVER_EMAIL': 'kodealtest',
    'REDIRECT_PAGE': 'http://127.0.0.1:8000/home/'
}