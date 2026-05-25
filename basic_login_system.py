   #build a basic login system:   

correct_username="ansh"

correct_password = "Nature@123"
name = input("enter your Good Name: ")

username= input("enter username: ")
password= input("enter your password: ")
 
if(username==correct_username and password == correct_password):
    print("login successfull: Mr ",name.capitalize())
else:
    print("invalid username or password: ")    
