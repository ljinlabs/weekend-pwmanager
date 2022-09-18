from dotenv import load_dotenv
import random
import pymysql
from secrets import choice
import os


load_dotenv()
# todo
# 1. password generating algorithm

##
NUMS = [str(i) for i in range(10)]
LOWERCASE = [chr(i) for i in range(97,123)]
UPPERCASE = [chr(i) for i in range(65, 91)]
SPECIAL = [chr(i) for i in range(33, 38)] + [chr(j) for j in range(58, 65)] + [chr(k) for k in range(91, 97) if k != 92]
PS1_CHOICES = NUMS + LOWERCASE
PS2_CHOICES = NUMS + LOWERCASE + UPPERCASE + SPECIAL

HOST = os.getenv('HOST')
DBUSER = os.getenv('DBUSER')
DBPASSWORD = os.getenv('DBPASSWORD')
PORT = int(os.getenv('PORT'))

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

# 1.1 get user input? what input?
def choice_security_level():
    security_level = int(input("보안 등급을 선택하세요 (0,1,2) : "))
    if security_level not in [0,1,2]:
        security_level = 0
    return security_level

# 2. show generated password
def show_password():
    security_level = choice_security_level()

    result = True

    while (result): 
        password = generate_password(security_level)
        print(password)

        user_answer = input("이 비밀번호로 할까요? (y/n): ")
        if user_answer in ["y", "Y", "YES", "Yes", "yes"]:
            result = False
            # 4. create database
            conn = pymysql.connect(host=HOST, user=DBUSER, password=DBPASSWORD, port=PORT, charset='utf8')
            cur = conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS passwordDB")
            cur.execute("USE passwordDB")
            cur.execute("CREATE TABLE IF NOT EXISTS passwordTbl (password       CHAR(16))")
            cur.execute("INSERT INTO passwordTbl VALUES (%s)", password)
            conn.commit()
            conn.close()
        print("비밀번호가 저장되었습니다.")
        print("저장된 비밀번호 : ", password)
            

    
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