from django.urls import path
from Driver.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('all_user/', UserView.as_view(), name='all_user'),
    path('add_address-company-from', AddressCompanyFromAddView.as_view(), name='add_address_company_from'),
    path('add_address-company-to', AddressCompanyToAddView.as_view(), name='add_address_company_to'),
    path('add_trailer/', TrailerView.as_view(), name='add_trailer'),
    path('add_car/', CarView.as_view(), name='add_car'),
    path('add_cargo/', CargoView.as_view(), name='add_cargo'),
    path('add_plan_cargo/', PlanCargoView.as_view(), name='add_plan_cargo'),
    path('add_driver_worker/', DriverWorkerView.as_view(), name='add_driver_worker'),

]