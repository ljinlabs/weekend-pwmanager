import random
from secrets import choice

# todo
# 1. password generating algorithm

##
NUMS = [str(i) for i in range(10)]
LOWERCASE = [chr(i) for i in range(97,123)]
UPPERCASE = [chr(i) for i in range(65, 91)]
SPECIAL = [chr(i) for i in range(33, 38)] + [chr(j) for j in range(58, 65)] + [chr(k) for k in range(91, 97) if k != 92]
PS1_CHOICES = NUMS + LOWERCASE
PS2_CHOICES = NUMS + LOWERCASE + UPPERCASE + SPECIAL

def get_length(security_level):
    ## password - level0, level1,level2
    ## level0 : length 8 ~ 12, number only.
    ps0_base = choice(NUMS)
    ## level1 : length 8 ~ 16, number and lowercase only.
    ps1_base = choice(NUMS) + choice(LOWERCASE)
    ## level2 : length 12 ~ 16, all.
    ps2_base = choice(NUMS) + choice(LOWERCASE) + choice(UPPERCASE) + choice(SPECIAL)


    if security_level == 1:
        pw_length = random.randint(8,17)
        base = ps1_base
        pw_choices = PS1_CHOICES

    elif security_level == 2:
        pw_length = random.randint(12,17)
        base = ps2_base
        pw_choices = PS2_CHOICES

    else:
        pw_length = random.randint(8,13)
        base = ps0_base
        pw_choices = NUMS


    return pw_length, base, pw_choices

def generate_password(security_level=0):

    pw_length, base, pw_choices = get_length(security_level)
    password = ""
    for i in range(pw_length-len(base)):
        password += choice(pw_choices)
    pw_list = list(password)
    random.shuffle(pw_list)
    password = "".join(pw_list)

    return password

        #미래의 내가 에러 처리를 하겠지...?
# 1.1 get user input? what input?
# 2. show generated password

def choice_security_level():
    security_level = int(input("보안 등급을 선택하세요 (0,1,2) : "))
    if security_level not in [0,1,2]:
        security_level = 0
    return security_level

def show_password():
    security_level = choice_security_level()

    result = True

    while (result): 
        password = generate_password(security_level)
        print(password)

        user_answer = input("이 비밀번호로 할까요? (y/n): ")
        if user_answer in ["y", "Y", "YES", "Yes", "yes"]:
            result = False
            



# sql
# 4. create database
# 5. check input valid
# 6. store data
#
# fetch
# 7. get password by website
# 
# advanced
# 8. password filtering

if __name__ == "__main__":
    show_password()