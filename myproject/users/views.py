from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log the user in after registration
            login(request, form.save())
            return redirect('posts:list')  # Redirect to post list
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')  # Redirect to post list
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form })

def logout_view(request):
    if request.method == 'POST':
        # Log the user out
        logout(request)
    return redirect('posts:list')  # Redirect to post list  