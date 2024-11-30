from string import ascii_lowercase, ascii_uppercase
import random

chars="".join((ascii_lowercase, ascii_uppercase,"0123456789!?@#$*"))

def make_passwd() -> str:
    pass_l = 12
    return "".join(map(lambda _: random.choice(chars), range(pass_l)))

assert len(make_passwd()) == 12

n_passwds = 5
for _ in range(n_passwds):
    print(make_passwd())