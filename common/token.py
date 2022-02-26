""" common.token.py - 토큰 생성 파일 """

import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class CommonActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.is_active)


common_activation_token = CommonActivationTokenGenerator()
