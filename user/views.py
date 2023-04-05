from django.shortcuts import render,redirect

# Create your views here.
from .forms  import NewUserForm,LoginForm


from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth import logout as auth_logout


def register_request(request):
	print('hi')
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			
			messages.success(request, "Registration successful." )
			return redirect('core:index')
		messages.error(request, "Unsuccessful registration. Invalid information.")
		return render(request,'error.html', {'form': form})
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})





def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('core:index')  # Replace 'home' with your desired URL
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def logout(request):
    if request.user.is_authenticated:
        username = request.user.username
        auth_logout(request)
        messages.success(request, f"Goodbye, {username}! You have been logged out.")
    return redirect('core:index')