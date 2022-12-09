from django.urls import path
from Driver.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('all_user/', UserView.as_view(), name='all_user'),
    path('add_address_company_from/', AddressCompanyFromAddView.as_view(), name='add_address_company_from'),
    path('all_address_company_from/', AddressCompanyFromAllView.as_view(), name='all_address_company_from'),
    path('address_company_from/<int:id>/', AddressCompanyFromView.as_view(), name='address_company_from'),
    path('add_address_company_to/', AddressCompanyToAddView.as_view(), name='add_address_company_to'),
    path('all_address_company_to/', AddressCompanyToAllView.as_view(), name='all_address_company_to'),
    path('address_company_to/<int:id>/', AddressCompanyToView.as_view(), name='address_company'),
    path('add_trailer/', TrailerAddView.as_view(), name='add_trailer'),
    path('all_trailer/', TrailerAllView.as_view(), name='all_trailer'),
    path('trailer/<int:id>/', TrailerView.as_view(), name='trailer'),
    path('add_car/', CarAddView.as_view(), name='add_car'),
    path('all_car/', CarAllView.as_view(), name='all_car'),
    path('car/<int:id>/', CarView.as_view(), name='car'),
    path('add_cargo/', CargoAddView.as_view(), name='add_cargo'),
    path('add_plan_cargo/', PlanCargoAddView.as_view(), name='add_plan_cargo'),
    path('add_driver_worker/', DriverWorkerAddView.as_view(), name='add_driver_worker'),
    path('reset_password/<int:pk>/', ResetPasswordView.as_view(), name='reset_password'),
]