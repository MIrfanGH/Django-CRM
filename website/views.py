from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # To show pop-up messages if we are login 
from .forms import SignUpForm, AddRecordForm
from .models import Record # To 'Veiew Record on Website' >>>>>>>>>>> 1:26:00



def home(request):
    records = Record.objects.all() # This will grab all the record on table and assign it to this variable 'records'


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
        # elif user.password != password:
        #     messages.success(request, "You seems to have entered wrong Username or Password")
        #     return redirect('home')
        else:
            messages.success(request, "There was an error loggin ! Please try again... ")
            return redirect('home')
    else:
        # the client is just visiting the page OR alread logged in 
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')


def register_user(request):
    # condition to check if the method is 
    # 'post' request, it is a 'regular form'
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # Then Creating a form(registration form)
        if form.is_valid():
            form.save()

            # Authenticate and Login <<<<<<<<<<<<<< 
            username = form.cleaned_data['username'] # this 'form.cleaned_data' takes 
                                                     # whatever they posted on form and pulls out the username and assigns it to this user variable 
            password = form.cleaned_data['password1'] # Same goes with this password aswell 
            user = authenticate(username=username, password=password)  # authenticating the user here 
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')

        
    else:
        form = SignUpForm() # we are not passing the 'request.POST' here cause the user have not filled up the form YET, 
                            # they're just going to the page, they want to fill up the form
                            # So we need to pass this form onto the page so, providing it while rendering the p 
        
        return render(request, 'register.html', {'form':form} ) # We are rendering this 'register.html' template 
                                                                # and passing the context data to it 
    return render(request, 'register.html', {'form':form} )  # Erro without this line. why...?


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Record
        customer_record = Record.objects.get(id=pk)  # Compare this line with above home() first line 
        return render(request, 'record.html', {'customer_record':customer_record } )
    
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        # Record.objects.filter(id=id).delete()
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully ! ")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that! ")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form} )
    else:
        messages.success(request, "You must be logged in ...")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated: # Means if the user is logged in
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)  # Read the NoteBook for this  
        if form.is_valid(): # Means they have already posted/updated, that's why checking form's validation
            form.save()
            messages.success(request, "Record Has Been Updated! ")
            return redirect('home')
        
        return render(request, 'update_record.html', {'form':form} )
    else:
        messages.success(request, "You must be logged in! ")
        return redirect('home')
    






