from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from .services import send_email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.
def signup_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())
            subject = 'Activate Your Account'
            send_email('registration/send_email.html',
                       subject, user.email, {
                'uid': uid,
                'token': token,
            })

            return redirect(reverse_lazy('verify'))
    return render(request, 'registration/signup.html', {'form': form})

def verify_email_view(request):
    return render(request, 'registration/verify.html')

def confirm_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account is now active. Please login.')
        return redirect('login')
    else:
        messages.error(request, 'The confirmation link is invalid or has expired.')
        return redirect('signup')



def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect(reverse_lazy('home'))
            else:
                messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html', {'form': form})

# def email_send_view(request):
#     subject = request.GET.get('subject')
#     email = request.GET.get('email')
#
#     if not subject:
#         return JsonResponse({'status':False, 'error': 'Subject cannot be empty'}, status=400)
#     elif not email:
#         return JsonResponse({'status':False, 'error': 'Email cannot be empty'}, status=400)
#
#     send_email('registration/send_email.html', subject, email)
#     return JsonResponse({'status': 'Successfully sent email'}, status=200)