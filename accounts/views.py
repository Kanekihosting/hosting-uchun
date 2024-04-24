from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import UserRegistrationForm

# Create your views here.


def dashboard_view(request):
    user = request.user
    profile = Profile.objects.all()
    context = {
        'user': user,
        'profile': profile,
    }
    return  render(request, 'pages/profile.html', context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})

# class SignUpView(View):
#     def get(self, request):
#         user_form = UserRegistrationForm()
#         return render(request, 'account/register.html', {'user_form': user_form})
#
#     def post(self, request):
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password']
#             )
#             new_user.save()
#             return render(request, 'account/register_done.html', {'new_user': new_user})
#         if user_form is not None:
#             return HttpResponse(render(request, 'account/error.html'))


# class EditUserView(LoginRequiredMixin,View):
#
#     def get(self,request):
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#         context = {
#             'user_form': user_form,
#             'profile_form': profile_form,
#         }
#         return render(request,'account/profile_edit.html',context)
#
#     def post(self,request):
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form= ProfileEditForm(instance=request.user.profile,
#                                       data=request.POST,
#                                       files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('user_profile')

