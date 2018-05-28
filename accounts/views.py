from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):
    '''
    If the request is post then we will take the data that we've 
    got from the form and we want to somehow validate it and the way we do that
    is by following:
    '''
    if request.method == 'POST':
        '''
        What this instance is doing is essentially kind of valid in that data 
        for us.If this data is okay(like user is already exists or not,password in 
        long enough or not etc..).That's going to return us a instance of form 
        that is either valid or invalid.If it is valid save that form to database.
        '''
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #log the user in
            user = form.save()
            #after getting user we will try to login that user
            login(request, user)
            #redirect the user to articles list page
            return redirect('articles:list')
    #if the request is get then create a blank instance of user creation form.
    else:
        #create a new instance of the form
        form = UserCreationForm()
    #send that form to template
    return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    '''
    same as the signup view,in the login we can also have get request or post request
    if the request is post
    '''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            #first of all we need to get what the user is,who's trying to log in 
            user = form.get_user()
            #after getting user we will try to login that user
            login(request, user)

            #for redirecting  
            if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
            else:
               return redirect('articles:list')
            #redirect the user to articles list page
            return redirect('articles:list')
    else:
        #this will be get request.When user clicks on login link or he will go to /accounts/login/ 
        #we will send them a login form to the template and render that form in the browser
        #create a new instance of the form
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        #we don't need to pass the current user becuase he is already logged in as a user.
        #it will logout the current user
        logout(request)
        #once the user is logged out we'll do some kind of redirect.
        return redirect('articles:list')

        
   