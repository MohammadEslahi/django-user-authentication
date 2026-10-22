users=[]

try:
    with open('users.txt','r') as file:
        for user in file:
            users.append(user.strip())
except FileNotFoundError:
    pass

username = input('enter a username:\n').lower().strip()

def register_user(username):
    if not username:
        return 'empty'
    elif len(username) < 4:
        return 'too short'
    else:
        if username not in users:
            users.append(username)
            save_users()
            return 'success'
        else:
            return 'already exists'
        
def save_users():
    with open('users.txt','w') as file:
        for user in users:
            file.write(user+'\n')

result = register_user(username)
print(result)
