from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # To show pop-up messages if we are login 



def home(request):
    # check to see if logging in
    if request.method == 'POST':  # 'POST' means they are filling up the form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate : >>>>>>>>>>>>> authentication is used to verify the identity of users accessing your application
        #               will check if the user is real , password is corect ?, should we log them in
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in !")
            return redirect('home')
        else:
            messages.success(request, "There was an error loggin ! Please try again... ")
            return redirect('home')
    else:
        # the client is just visiting the page
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')


def register_user(request):
    # # condition to check if the method is 
    # # 'post' request, it is a 'regular form'
    # if request.method == 'POST':
    #     form = UserRegistrationForm(request.POST)  # Then Creating a form(registration form)
    #     if form.is_valid():
    #         user = form.save(commit=False)  
    #         user.set_password(form.cleaned_data['password1'])
    #         user.save()  # after saving the user, we want to login as well so,
    #         login(request, user)  # imported this method from 'contrib.auth'
    #         return redirect('tweet_list')
        
    # else:
    #     form = UserRegistrationForm()
        
    # return render(request, 'registration/register.html', 
    # {'form': form})
    return render(request, 'register.html', {})
