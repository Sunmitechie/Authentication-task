from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomPasswordResetConfirmView, CustomPasswordResetView, SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]