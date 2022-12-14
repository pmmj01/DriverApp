from django.urls import path
from Driver.views import *

urlpatterns = [
    path('add/user/', UserAddView.as_view(), name='add_user'),
    path('all/user/', UserAllView.as_view(), name='all_user'),
    path('user/<int:id>/', UserView.as_view(), name='u_user'),
    path('edit/user/<int:id>/', UserEditView.as_view(), name='edit_user'),
    path('delete/user/<int:id>/', UserDeleteView.as_view(), name='delete_user'),
    path('add/address_company_from/', AddressCompanyFromAddView.as_view(), name='add_address_company_from'),
    path('all/address_company_from/', AddressCompanyFromAllView.as_view(), name='all_address_company_from'),
    path('address_company_from/<int:id>/', AddressCompanyFromView.as_view(), name='address_company_from'),
    path('edit/address_company_from/<int:id>/', AddressCompanyFromEditView.as_view(), name='edit_address_company_from'),
    path('delete/address_company_from/<int:id>/', AddressCompanyFromDeleteView.as_view(), name='delete_address_company_from'),
    path('add/address_company_to/', AddressCompanyToAddView.as_view(), name='add_address_company_to'),
    path('all/address_company_to/', AddressCompanyToAllView.as_view(), name='all_address_company_to'),
    path('address_company_to/<int:id>/', AddressCompanyToView.as_view(), name='address_company_to'),
    path('edit/address_company_to/<int:id>/', AddressCompanyToEditView.as_view(), name='edit_address_company_to'),
    path('delete/address_company_to/<int:id>/', AddressCompanyToDeleteView.as_view(), name='delete_address_company_to'),
    path('add/trailer/', TrailerAddView.as_view(), name='add_trailer'),
    path('all/trailer/', TrailerAllView.as_view(), name='all_trailer'),
    path('trailer/<int:id>/', TrailerView.as_view(), name='trailer'),
    path('edit/trailer/<int:id>/', TrailerEditView.as_view(), name='edit_trailer'),
    path('delete/trailer/<int:id>/', TrailerDeleteView.as_view(), name='delete_trailer'),
    path('add/car/', CarAddView.as_view(), name='add_car'),
    path('all/car/', CarAllView.as_view(), name='all_car'),
    path('car/<int:id>/', CarView.as_view(), name='car'),
    path('edit/car/<int:id>/', CarEditView.as_view(), name='edit_car'),
    path('delete/car/<int:id>/', CarDeleteView.as_view(), name='delete_car'),
    path('add/cargo/', CargoAddView.as_view(), name='add_cargo'),
    path('all/cargo/', CargoAllView.as_view(), name='all_cargo'),
    path('edit/cargo/<int:id>/', CargoEditView.as_view(), name='edit_cargo'),
    path('delete/cargo/<int:id>/', CargoDeleteView.as_view(), name='delete_cargo'),
    path('cargo/<int:id>/', CargoView.as_view(), name='cargo'),
    path('add/plan_cargo/', PlanCargoAddView.as_view(), name='add_plan_cargo'),
    path('all/plan_cargo/', PlanCargoAllView.as_view(), name='all_plan_cargo'),
    path('edit/plan_cargo/<int:id>/', PlanCargoEditView.as_view(), name='edit_plan_cargo'),
    path('delete/plan_cargo/<int:id>/', PlanCargoDeleteView.as_view(), name='delete_plan_cargo'),
    path('add/plan_cargo/<int:id>/', PlanCargoView.as_view(), name='plan_cargo'),
    path('add/driver_worker/', DriverWorkerAddView.as_view(), name='add_driver_worker'),
    path('all/driver_worker/', DriverWorkerAllView.as_view(), name='all_driver_worker'),
    path('edit/driver_worker/<int:id>/', DriverWorkerEditView.as_view(), name='edit_driver_worker'),
    path('delete/driver_worker/<int:id>/', DriverWorkerDeleteView.as_view(), name='delete_driver_worker'),
    path('driver_worker/<int:id>/', DriverWorkerView.as_view(), name='driver_worker'),
    path('reset_password/<int:pk>/', ResetPasswordView.as_view(), name='reset_password'),
]