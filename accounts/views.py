from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

CustomUser = get_user_model()

def register_view(request):
    google_prefill = request.session.get("google_prefill", {})

    if request.method == 'POST':
        fn = request.POST.get('first_name') or google_prefill.get("first_name")
        ln = request.POST.get('last_name') or google_prefill.get("last_name")
        email = request.POST.get('email') or google_prefill.get("email")
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        phone = request.POST.get('phone')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        secondary_contact = request.POST.get('secondary_contact')
        terms = request.POST.get('terms')

        if not email:
            messages.error(request, "Email is required.")
            return render(request, 'register.html', {"prefill": google_prefill})

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'register.html', {"prefill": google_prefill})

        if password != password1:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html', {"prefill": google_prefill})

        if not terms:
            messages.error(request, "You must agree to the terms and conditions.")
            return render(request, 'register.html', {"prefill": google_prefill})

        user = CustomUser(
            first_name=fn,
            last_name=ln,
            email=email,
            username=email,
            phone=phone,
            street_address=street_address,
            city=city,
            zip_code=zip_code,
            secondary_contact=secondary_contact,
        )
        user.set_password(password)
        user = user.save()
        login(request, user)


        # Link Google account if present
        if google_prefill:
            SocialAccount.objects.create(
                user=user,
                provider=google_prefill["provider"],
                uid=google_prefill["uid"],
                extra_data={
                    "email": email,
                    "first_name": fn,
                    "last_name": ln,
                }
            )
            request.session.pop("google_prefill", None)

        messages.success(request, "Account created successfully.")
        return redirect("account_login")

    # GET request → prefill form
    return render(request, 'register.html', {"prefill": google_prefill})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff and not user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_superuser:
                return redirect('admin:index')
            else:   
                return redirect('user_dashboard')
            
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

from .forms import CustomUserUpdationForm

@login_required
def profile_view(request):
    if request.method == 'POST':

        form = CustomUserUpdationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(request, "Please correct the errors below.",extra_tags='danger')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}",extra_tags='danger')
        return redirect('profile')
    else:
        form = CustomUserUpdationForm(instance=request.user)

    return render(request, 'profile.html',context={"form": form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Please correct the errors below.",extra_tags='danger')
            for _, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}",extra_tags='danger')
            return redirect('change_password')
        messages.success(request, "Password changed successfully. Please log in again.")
        logout(request)
        return redirect('login')

    return render(request, 'change-password.html')