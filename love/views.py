from django.shortcuts import render,redirect
from django.contrib import messages

def home(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        second_name=request.POST['lname']
        first_name=first_name.lower().replace(" ","")
        second_name=second_name.lower().replace(" ","")
        s=list(second_name)
        n=0
        f=["f","l","a","m","e","s"]
        for i in first_name:
            if i in s:
                s.remove(i)
                n+=1
        n=len(first_name)+len(second_name)-2*n
        i=0
        while len(f) > 1:
            l = n % len(f) - 1
            if l >= 0:
                right=f[l+1:]
                left=f[:l]
                f=right+left
            else:
                f=f[:len(f)-1]
        
        if f[0] == 'f':
            messages.success(request,"Friends😘")
        elif f[0] == 'l':
            messages.success(request,"Love💖")
        elif f[0] == 'm':
            messages.success(request,"Marriage💞")
        elif f[0] == 'a':
            messages.success(request,"Affection🥰")
        elif f[0] == 'e':
            messages.success(request,"Enemies😡")
        else:
            messages.success(request,"Siblings👥")
        return redirect('home')
    else:
        return render(request,'flames.html')

