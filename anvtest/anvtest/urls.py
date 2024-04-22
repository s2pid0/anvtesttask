
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from cabinets.views import ShowProfilePageView, RegisterView, UpdateProfileView, ShowContractorProfilePageView, home, logout_view

urlpatterns = [path('', RedirectView.as_view(pattern_name='login', permanent=False)),
                path('admin/', admin.site.urls),
                path('home/', home, name='home'),
                path('login/', LoginView.as_view(), name='login'),
                path('logout/', logout_view, name='logout'),
                path('customer_profile/<int:pk>/', ShowProfilePageView.as_view(), name='customer_profile'),
                path('contractor_profile/<int:pk>/', ShowContractorProfilePageView.as_view(), name='contractor_profile'),
                path('register/', RegisterView.as_view(), name='users-register'),
                path('update_profile/', UpdateProfileView.as_view(), name='update_profile')]
