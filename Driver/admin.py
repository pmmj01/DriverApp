from django.contrib import admin
from .models import AddressCompanyFromModel, AddressCompanyToModel, DriverModel, ForwarderModel, TrailerModel, CarModel, CargoModel, PlanCargoModel

admin.site.register(AddressCompanyFromModel)
admin.site.register(AddressCompanyToModel)
admin.site.register(DriverModel)
admin.site.register(ForwarderModel)
admin.site.register(TrailerModel)
admin.site.register(CarModel)
admin.site.register(CargoModel)
admin.site.register(PlanCargoModel)
