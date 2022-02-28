import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # mysqlclient 라이브러리 설치
        # ----- heroku -----
        'NAME': 'heroku_2c03059b0a4530f',        # database 이름
        'USER': 'b2c6dff0779745',                # user 이름
        'PASSWORD': 'd18964d1',                  # 비밀번호
        'HOST': 'us-cdbr-east-05.cleardb.net',   # 호스트
        # ----- local -----
        # 'NAME': 'itrencotech_database',        # database의 이름
        # 'USER': 'root',                        # user 이름
        # 'PASSWORD': '',                        # 비밀번호
        # 'HOST': '127.0.0.1',                   # 호스트

        'PORT': '3306',                          # Port 번호
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8',
            'use_unicode': True,
        }
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'c=%dig$7ojo8cksb_p+q!)^98te@$e$-jzna&l#6*+)36t369c')

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


