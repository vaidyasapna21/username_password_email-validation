def login_user(name,password,email):
    print(f"login user name is {name}")
    print(f"login user password is {password}")
    print(f"login user email is {email}")
    
    if len(name)>=3 and len(password)>=8 and "@" in email:
        print("wlcome to portal")
    else:
        print("try agian ") 
    

nam =input("enter users name:")  
psw = input("enter users password:")
email = input("enter users email:")


login_user(nam,psw,email)