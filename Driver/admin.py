from django.contrib import admin
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

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["user_type", "phone_number", "first_name", "last_name"]
    list_filter = ["user_type"]


@admin.register(AddressCompanyFromModel)
class AddressCompanyFromAdmin(admin.ModelAdmin):
    search_fields = ["company_name", "address_country", "address_zip_code"]
    list_filter = ["company_name", "address_country"]


@admin.register(AddressCompanyToModel)
class AddressCompanyToAdmin(admin.ModelAdmin):
    search_fields = ["company_name", "address_country", "address_zip_code"]
    list_filter = ["company_name", "address_country"]


@admin.register(DriverModel)
class DriverAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(ForwarderModel)
class ForwarderAdmin(admin.ModelAdmin):
    fields = ['__all__']


@admin.register(TrailerModel)
class TrailerAdmin(admin.ModelAdmin):
    search_fields = ["model", "trailer_number", "cargo_space"]
    list_filter = ["model", "cargo_space"]


@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model", "car_number", "cargo_space"]
    list_filter = ["model", "have_to", "car_number", "cargo_space"]


@admin.register(CargoModel)
class CargoAdmin(admin.ModelAdmin):
    search_fields = ["pk", "truck", "forwarder"]
    list_filter = ["forwarder", "fix", "customs"]


@admin.register(PlanCargoModel)
class PlanCargoAdmin(admin.ModelAdmin):
    search_fields = ["driver", "truck", "forwarder"]
    list_filter = ["forwarder", "truck", "driver"]


@admin.register(DriverWorkerModel)
class DriverWorkerAdmin(admin.ModelAdmin):
    search_fields = ["point", "confirm_arrival", "confirm_unloading", "confirm_loading", "raport"]
    list_filter = ["confirm_arrival", "confirm_unloading", "confirm_loading", "raport"]


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ["message_to"]
    list_filter = ["message_to"]