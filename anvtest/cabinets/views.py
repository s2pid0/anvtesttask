from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views import View
from django.urls import reverse
from .forms import RegisterForm, UpdateProfileForm, UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    current_user = request.user
    return render(request, 'home.html', {'id': current_user})


def logout_view(request):
    logout(request)
    return redirect('/login')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                username = form.cleaned_data.get('name')
                user.save()
                profile_of_user = Profile(id=user.pk, user=user, first_name=user.first_name)
                profile_of_user.save()
                print(Profile.objects.get(pk=user.id))
                messages.success(request, f'Account created for {username}')
                login(request, user)
                pk = user.id
                print(pk)
                return redirect('customer_profile', pk=pk)
            else:
                print('form is not valid')
        return render(request, self.template_name, {'form': form})


class ShowProfilePageView(View):
    model = Profile
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        page_user = Profile.objects.get(pk=request.user.pk)
        return render(request, self.template_name, {'profile': page_user})

class ShowContractorProfilePageView(View):
    model = Profile
    template_name = 'contractor-profile.html'

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        page_user = Profile.objects.get(pk=request.user.pk)
        return render(request, self.template_name, {'profile': page_user})


class UpdateProfileView(View):
    form_class = UpdateProfileForm
    initial = {'key': 'value'}
    template_name = 'profile_update.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'profile_form': form})

    def post(self, request, *args, **kwargs):
        print(request)
        current_user = request.user
        if request.method == 'POST':
            form = self.form_class(request.POST, instance=request.user)

            if form.is_valid():
                print(current_user.pk)
                user_profile = Profile.objects.get(pk=current_user.pk)
                user_profile.contact = form.cleaned_data['contact']
                user_profile.exp = form.cleaned_data['exp']
                user_profile.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='customer_profile', pk=current_user.pk)
        else:
            form = self.form_class()

        return render(request, self.template_name, {'profile_form': form})


