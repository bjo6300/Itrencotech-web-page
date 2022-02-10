""" common/text.py - 이메일로 발송되는 텍스트 """


def message(domain, uidb64, token):
    return f"링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n" \
           f"회원가입 링크 : http://{domain}/common/activate/{uidb64}/{token}\n\n" \
           f"감사합니다."

# 위에서 회원가입 링크는 active를 담당하는 엔드포인트 URL 주소임
