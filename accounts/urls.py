from django.urls import path
from .views import user_register, dashboard_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView




urlpatterns =[
    path('signup/', user_register, name='user_register'),
    # path('profile/edit', EditUserView.as_view(), name='edit_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', dashboard_view, name='user_profile'),
]