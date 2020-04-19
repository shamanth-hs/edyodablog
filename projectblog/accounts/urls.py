from django.urls import path,include
from accounts.views import UserCreateView,AuthorCreateView
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('login/',LoginView.as_view(template_name = "account/login.html"),name="login"),
    path('', include('django.contrib.auth.urls')),
    path('signup',UserCreateView.as_view()),
    path('bio/<int:pk>',AuthorCreateView.as_view()),
    path('password-reset',PasswordResetView.as_view(template_name = "account/password_reset_form.html",email_template_name="account/password_reset_email.html"),name='password_reset'),
    path('/password_reset/done/',PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name = 'account/password_confirm.html'),name='password_reset_confirm'),
    path('password_change/', PasswordChangeView.as_view(template_name = "account/password_change.html"), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name = 'account/password_change_done.html'), name='password_change_done'),

]