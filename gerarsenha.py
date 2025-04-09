import secrets
import string

caracteres = (string.ascii_letters + string.digits)
senha = [secrets.choice(caracteres) for i in range(15)]
senha = ''.join(senha)
print(senha)
