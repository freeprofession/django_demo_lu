import hashlib


def password_to_md(password):
    passwd_h_md5 = hashlib.md5()
    passwd_h_md5.update(password.encode('utf-8'))
    return passwd_h_md5.hexdigest()