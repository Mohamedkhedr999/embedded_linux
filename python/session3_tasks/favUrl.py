import webbrowser



myfavUrl = ["www.google.com","www.facebook.com","www.whatsapp.com","www.yts.mx","www.github.com","www.linkedin.com"]

length = len(myfavUrl) 

def openUrl(x):
    global myfavUrl
    if x < length :
        browser=webbrowser.get("firefox")
        browser.open(myfavUrl[x])
    else:
        print("wrong input")   
        
    
    
    
  