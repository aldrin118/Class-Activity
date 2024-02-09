def authorize(func):
    def wrap(username,password):
        authorized = False;
        if username == "test":
            authorized = True
        else:
            authorized = False
        if password == "test123":
            authorized = True
        else:
            authorized = False
        
        return authorized
    
    return wrap
    

@authorize
def login(username,password):
    print("loging in")

if(login("test","test123")):
    print("authorized")
else:
    print("not authorized")
    
    
if(login("test","test1232222")):
    print("authorized")
else:
    print("not authorized")