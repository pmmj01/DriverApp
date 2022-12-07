from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserModel, AddressCompanyFromModel, AddressCompanyToModel, DriverModel, ForwarderModel, \
    TrailerModel, CarModel, CargoModel, PlanCargoModel, DriverWorkerModel, MessageModel
from Driver.forms import *
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class UserView(View):
    def get(self, request):
        users = UserModel.objects.exclude(is_superuser=True)
        return render(request, 'all_user.html', locals())


class AddressCompanyFromAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddressCompanyFromForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = AddressCompanyFromForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data.get("company_name")
            address_country = form.cleaned_data.get("address_country")
            address_city = form.cleaned_data.get("address_city")
            address_zip_code = form.cleaned_data.get("address_zip_code")
            address_street = form.cleaned_data.get("address_street")
            address_property_first = form.cleaned_data.get("address_property_first")
            address_property_second = form.cleaned_data.get("address_property_second")
            address_more_info = form.cleaned_data.get("address_more_info")
            companyFrom = AddressCompanyFromModel()
            companyFrom.company_name = company_name
            companyFrom.address_country = address_country
            companyFrom.address_city = address_city
            companyFrom.address_zip_code = address_zip_code
            companyFrom.address_street = address_street
            companyFrom.address_property_first = address_property_first
            companyFrom.address_property_second = address_property_second
            companyFrom.address_more_info = address_more_info
            companyFrom.save()
            return redirect('companyFrom', companyFrom_id=companyFrom.id)
        return render(request, "add.html", locals())


class AddressCompanyFromAllView(View):
    def get(self, request):
        all_address_from = AddressCompanyFromModel.objects.all()
        return render(request, 'all_address_from.html', locals())


class AddressCompanyToAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddressCompanyToForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = AddressCompanyToForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data.get('company_name')
            address_country = form.cleaned_data.get('address_country')
            address_city = form.cleaned_data.get('address_city')
            address_zip_code = form.cleaned_data.get('address_zip_code')
            address_street = form.cleaned_data.get('address_street')
            address_property_first = form.cleaned_data.get('address_property_first')
            address_property_second = form.cleaned_data.get('address_property_second')
            address_more_info = form.cleaned_data.get('address_more_info')
            companyTo = AddressCompanyToModel()
            companyTo.company_name = company_name
            companyTo.address_country = address_country
            companyTo.address_city = address_city
            companyTo.address_zip_code = address_zip_code
            companyTo.address_street = address_street
            companyTo.address_property_first = address_property_first
            companyTo.address_property_second = address_property_second
            companyTo.address_more_info = address_more_info
            companyTo.save()
            return redirect('companyTo', companyTo_id=companyTo.id)
        return render(request, 'add.html', locals())


class AddressCompanyToAllView(View):
    def get(self, request):
        all_address_to = AddressCompanyToModel.objects.all()
        return render(request, 'all_address_to.html', locals())


class TrailerAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = TrailerForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = TrailerForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data.get('model')
            trailer_number = form.cleaned_data.get('trailer_number')
            weighs = form.cleaned_data.get('weighs')
            tons_cal_load = form.cleaned_data.get('tons_can_load')
            cargo_space = form.cleaned_data.get('cargo_space')
            trailer = TrailerModel()
            trailer.model = model
            trailer.trailer_number = trailer_number
            trailer.weighs = weighs
            trailer.tons_can_load = tons_cal_load
            trailer.cargo_space = cargo_space
            trailer.save()
            return redirect('trailer', trailer_id=trailer.id)
        return render(request, 'add.html', locals())


class TrailerAllView(View):
    def get(self, request):
        all_trailer = UserModel.objects.all()
        return render(request, 'all_trailer.html', locals())


class CarAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = CarForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data.get('model')
            have_to = form.cleaned_data.get('have_to')
            car_number = form.cleaned_data.get('car_number')
            weighs = form.cleaned_data.get('weighs')
            tons_cal_load = form.cleaned_data.get('tons_can_load')
            cargo_space = form.cleaned_data.get('cargo_space')
            trailer = form.cleaned_data.get('trailer')
            car = CarModel()
            car.model = model
            car.have_to = have_to
            car.car_number = car_number
            car.weighs = weighs
            car.tons_can_load = tons_cal_load
            car.cargo_space = cargo_space
            car.trailer = trailer
            car.save()
            return redirect('car', car_id=car.id)
        return render(request, 'add.html', locals())


class CarAllView(View):
    def get(self, request):
        all_car = CarModel.objects.all()
        return render(request, 'all_car.html', locals())


class CargoAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = CargoForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = CargoForm(request.POST)
        if form.is_valid():
            company_address_from = form.cleaned_data.get('company_address_from')
            loading_date = form.cleaned_data.get('loading_date')
            loading_hour = form.cleaned_data.get('loading_hour')
            company_address_to = form.cleaned_data.get('company_address_to')
            unloading_date = form.cleaned_data.get('unloading_date')
            unloading_hour = form.cleaned_data.get('unloading_hour')
            description = form.cleaned_data.get('description')
            fix = form.cleaned_data.get('fix')
            customs = form.cleaned_data.get('customs')
            weight = form.cleaned_data.get('weight')
            pallets = form.cleaned_data.get('pallets')
            place_of_pallets = form.cleaned_data.get('place_of_pallets')
            truck = form.cleaned_data.get('truck')
            forwarder = form.cleaned_data.get('forwarder')
            date = form.cleaned_data.get('date')
            cargo = CargoModel()
            cargo.company_address_from = company_address_from
            cargo.loading_date = loading_date
            cargo.loading_hour = loading_hour
            cargo.company_address_to = company_address_to
            cargo.unloading_date = unloading_date
            cargo.unloading_hour = unloading_hour
            cargo.description = description
            cargo.fix = fix
            cargo.customs = customs
            cargo.weight = weight
            cargo.pallets = pallets
            cargo.place_of_pallets = place_of_pallets
            cargo.truck = truck
            cargo.forwarder = forwarder
            cargo.date = date
            cargo.save()
            return redirect('cargo', cargo_id=cargo.id)
        return render(request, 'add.html', locals())


class CargoAllView(View):
    def get(self, request):
        all_Cargo = CargoModel.objects.all()
        return render(request, 'all_cargo.html', locals())


class PlanCargoAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = PlanCargoForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = PlanCargoForm(request.POST)
        if form.is_valid():
            driver = form.cleaned_data.get('driver')
            truck = form.cleaned_data.get('truck')
            forwarder = form.cleaned_data.get('forwarder')
            description = form.cleaned_data.get('description')
            date = form.cleaned_data.get('date')
            plan_cargo = PlanCargoModel()
            plan_cargo.driver = driver
            plan_cargo.truck = truck
            plan_cargo.forwarder = forwarder
            plan_cargo.description = description
            plan_cargo.date = date
            plan_cargo.save()
            return redirect('plan_cargo', plan_cargo_id=plan_cargo.id)
        return render(request, 'add.html', locals())


class PlanCargoAllView(View):
    def get(self, request):
        all_user = UserModel.objects.all()
        return render(request, 'all_user.html', locals())


class DriverWorkerAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = DriverWorkerForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        form = DriverWorkerForm(request.POST)
        if form.is_valid():
            point = form.cleaned_data.get('point')
            date = form.cleaned_data.get('date')
            confirm_arrival = form.cleaned_data.get('confirm_arrival')
            confirm_unloading = form.cleaned_data.get('confirm_unloading')
            confirm_loading = form.cleaned_data.get('confirm_loading')
            raport = form.cleaned_data.get('raport')
            message_to = form.cleaned_data.get('message_to')
            message = form.cleaned_data.get('message')
            driver_worker = DriverWorkerModel()
            driver_worker.point = point
            driver_worker.date = date
            driver_worker.confirm_arrival = confirm_arrival
            driver_worker.confirm_unloading = confirm_unloading
            driver_worker.confirm_loading = confirm_loading
            driver_worker.raport = raport
            driver_worker.message_to = message_to
            driver_worker.message = message
            driver_worker.save()
            return redirect('driver_worker', driver_worker_id=driver_worker.id)
        return render(request, 'add.html', locals())


class DriverWorkerUserView(View):
    def get(self, request):
        all_user = UserModel.objects.all()
        return render(request, 'all_user.html', locals())


class AddUserView(View):
    template_name = 'add.html'
    def get(self, request):
        form = AddUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')
        return render(request, self.template_name, {'form': form})


class ResetPasswordView(PermissionRequiredMixin, View):
    template_name = 'add.html'
    permission_required = 'auth.change_user'

    def get(self, request):
        return render(request, self.template_name, {
            'form': ResetPasswordForm()
        })

    def post(self, request, pk):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = UserModel.objects.get(id=pk)
            user.set_password(form.cleaned_data.get('new_password'))
            user.save()
            return redirect('/login')
        return render(request, self.template_name, {
            'form': form
        })