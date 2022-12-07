from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import UserModel, AddressCompanyFromModel, AddressCompanyToModel, DriverModel, ForwarderModel, TrailerModel, CarModel, CargoModel, PlanCargoModel, DriverWorkerModel, MessageModel


# admin.site.register(AddressCompanyFromModel)
# admin.site.register(AddressCompanyToModel)
# admin.site.register(DriverModel)
# admin.site.register(ForwarderModel)
# admin.site.register(TrailerModel)
# admin.site.register(CarModel)
# admin.site.register(CargoModel)
# admin.site.register(PlanCargoModel)
# admin.site.register(DriverWorkerModel)
# admin.site.register(MessageModel)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'first_name', 'last_name', 'user_type', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name', 'user_type')
    ordering = ('phone_number',)


admin.site.register(get_user_model(), CustomUserAdmin)

@admin.register(AddressCompanyFromModel)
class AddressCompanyFromAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'address_country', 'address_zip_code']
    list_filter = ['company_name', 'address_country']


@admin.register(AddressCompanyToModel)
class AddressCompanyToAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'address_country', 'address_zip_code']
    list_filter = ['company_name', 'address_country']


@admin.register(DriverModel)
class DriverAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(ForwarderModel)
class ForwarderAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(TrailerModel)
class TrailerAdmin(admin.ModelAdmin):
    search_fields = ['model', 'trailer_number', 'cargo_space']
    list_filter = ['model', 'cargo_space']


@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    search_fields = ['model', 'car_number', 'cargo_space']
    list_filter = ['model', 'have_to', 'car_number', 'cargo_space']


@admin.register(CargoModel)
class CargoAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'truck', 'forwarder']
    list_filter = ['forwarder', 'fix', 'customs']


@admin.register(PlanCargoModel)
class PlanCargoAdmin(admin.ModelAdmin):
    search_fields = ['driver', 'truck', 'forwarder']
    list_filter = ['forwarder', 'truck', 'driver']


@admin.register(DriverWorkerModel)
class DriverWorkerAdmin(admin.ModelAdmin):
    search_fields = ['point', 'confirm_arrival', 'confirm_unloading', 'confirm_loading', 'raport']
    list_filter = ['confirm_arrival', 'confirm_unloading', 'confirm_loading', 'raport']


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ['message_to']
    list_filter = ['message_to']