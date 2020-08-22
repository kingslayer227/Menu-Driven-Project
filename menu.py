import os

                 

while True:
    print(""" ╔╗╔╗╔╗──╔╗
 ║║║║║║──║║
 ║║║║║╠══╣║╔══╦══╦╗╔╦══╗
 ║╚╝╚╝║║═╣║║╔═╣╔╗║╚╝║║═╣
 ╚╗╔╗╔╣║═╣╚╣╚═╣╚╝║║║║║═╣
 ─╚╝╚╝╚══╩═╩══╩══╩╩╩╩══╝ """)   
    print()
    print('==============================') 
    print()     
    p = input("Hey user what you want to run:-> ")
    print()
    print('==============================') 
    if ("date" in p): 
        
        os.system("date")
    elif ("time" in p): 
        
        os.system("time")
    elif ("chrome" in p): 
        
        os.system("start chrome")
    elif ("spotify" in p): 
        
        os.system("spotify")
    elif ("Hello" in p) or ("hy" in p) or ("hey" in p):
        print("..Hello..")

    elif ("azure" in p) or ("ms cloud" in p):
        os.system("start chrome azure.microsoft.com")

    elif ("google" in p) or ("gcp" in p):
        os.system("start chrome cloud.google.com")

    elif ("aws" in p) or ("aws cloud services" in p):
        os.system("start chrome aws.amazon.com")

    elif ("gmail" in p):
        os.system("start chrome www.gmail.com")

    elif ("yahoo search" in p) or ("yahoo" in p):
        os.system("start chrome www.yahoo.com")

    elif ("youtube" in p):
        os.system("start chrome www.youtube.com")

    elif ("twitter" in p):
        os.system("start chrome www.twitter.com")

    elif ("whatsapp" in p):
        os.system("start chrome web.whatsapp.com")

    elif ("facebook" in p):
        os.system("start chrome www.facebook.com")

    elif ("linkedin" in p):
        os.system("start chrome www.linkedin.com")

    elif ("amazon" in p):
        os.system("start chrome www.amazon.in")  

    elif ("flipkart" in p):
        os.system("start chrome www.flipkart.com")

    elif ("notepad" in p) or ("text editor" in p): 
        os.system("notepad")

    elif ("puttygen" in p): 
        os.system("puttygen")

    elif ("putty" in p): 
        os.system("putty")

    elif ("virtualbox" in p) or ("virtual box" in p) or ("VM" in p) or ("vbox" in p) or ("vm" in p): 
        os.system("virtualbox")

    elif ("discord" in p): 
        os.system("discord")

    elif ("slack" in p): 
        os.system("slack")

    elif ("steam" in p): 
        os.system("steam")

    elif ("anydesk" in p): 
        os.system("anydesk")

    elif ("valorant" in p) or ("valo" in p): 
        os.system("valorant")

    elif ("exit" in p) or ("quit" in p) or ("bye" in p):
        print("𝑩𝒚𝒆")
        break

    elif ("zoom" in p): 
        os.system("zoom")

    else: 
        print("Not Supported/Invalid")
    input("Press any key to continue: ")
    os.system("cls")
