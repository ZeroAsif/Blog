from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
# HTML pages
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    return render(request, 'home/blog.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>50:
        allPosts = Post.objects.none()
    # allPosts= Post.objects.all()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsBlog= Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsBlog)
    
    
    if allPosts.count() == 0:
        messages.warning(request, "No search result found.")
    params={'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html', params)
    
# authentication APIs
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username) > 10 :
            messages.success(request, "username must be uder 10 character")
            return redirect('home')
        if pass1 != pass2:
            messages.success(request, "password do not match")
            return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate (username = loginusername , password = loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, 'successfully logged in.')
            return redirect('home')

        else:
            messages.error(request, 'invailid credential ! pleas try again')
            return redirect('home')

    return HttpResponse("404 - Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')