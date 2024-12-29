def create_user_profile(name,age,**kwargs):
    profile={"name":name, "age":age}
    profile.update(kwargs)
    return profile
user1=create_user_profile('Alice',30,location='New York',profession='Engineer')
print(user1)