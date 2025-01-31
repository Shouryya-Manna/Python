# *args -> it allows user to pass multiple non key arguments
# **kwargs -> it allows user to pass multiple keyword arguments
#    * is the unpacking operator

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for key,value in kwargs.items():
        print(f"{key}:{value}")


shipping_label("Mr.","Shouryya","Manna",
               item="Rifle",
               type="Sniper",
               name="Dragnoauv")