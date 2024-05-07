from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm, UserEditForm, ProfileEditForm
from .models import Profile

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Создаем профиль для нового пользователя
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, "registration/registration_page.html", {"register_form": form})

@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)  # Создаем профиль, если он не существует

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile edit success!')
            return redirect("home")
        else:
            messages.error(request, 'Some mistakes with profile editing')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
    return render(request, 'profile/edit.html', {'user_form': user_form, 'profile_form': profile_form})
@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, 'profile/edit.html', context)  
