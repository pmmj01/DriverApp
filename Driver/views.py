from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from Driver.forms import *
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class UserView(LoginRequiredMixin, View):
    def get(self, request):
        users = UserModel.objects.exclude(is_superuser=True)
        return render(request, 'all_user.html', locals())


class AddressCompanyFromAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Add Address Company From'
        form = AddressCompanyFromForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Add Address Company From'
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
            company = AddressCompanyFromModel()
            company.company_name = company_name.upper()
            company.address_country = address_country
            company.address_city = address_city.upper()
            company.address_zip_code = address_zip_code
            company.address_street = address_street.upper()
            company.address_property_first = address_property_first
            company.address_property_second = address_property_second
            company.address_more_info = address_more_info
            if AddressCompanyFromModel.objects.filter(company_name=company_name.upper(),
                                                      address_country=address_country,
                                                      address_city=address_city.upper(),
                                                      address_zip_code=address_zip_code,
                                                      address_street=address_street.upper(),
                                                      address_property_first=address_property_first).exists():
                message = 'Objects already exist'
                return render(request, "add.html", locals())
            else:
                company.save()
                message = 'Company added'
                url = f'/driver/address_company_from/{company.id}/'
                return redirect(url, message)
        else:
            message = "Try again"
            request.session['message'] = message
            return render(request, "add.html", locals())


class AddressCompanyFromAllView(View):
    def get(self, request):
        name = 'All Address Company From'
        company = AddressCompanyFromModel.objects.all()
        return render(request, 'all_address_from.html', locals())


class AddressCompanyFromView(View):
    def get(self, request, id):
        name = 'Address Company From'
        company = get_object_or_404(AddressCompanyFromModel, pk=id)
        ctx = {
            'company': company,
            'id': id,
            'name': name,
        }
        return render(request, 'address_id.html', ctx)


class AddressCompanyToAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Add Address Company To'
        form = AddressCompanyToForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Add Address Company To'
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
            company = AddressCompanyToModel()
            company.company_name = company_name.upper()
            company.address_country = address_country
            company.address_city = address_city.upper()
            company.address_zip_code = address_zip_code
            company.address_street = address_street.upper()
            company.address_property_first = address_property_first
            company.address_property_second = address_property_second
            company.address_more_info = address_more_info
            company.save()
            if AddressCompanyToModel.objects.filter(company_name=company_name.upper(),
                                                    address_country=address_country,
                                                    address_city=address_city.upper(),
                                                    address_zip_code=address_zip_code,
                                                    address_street=address_street.upper(),
                                                    address_property_first=address_property_first).exists():
                message = 'Objects already exist'
                return render(request, "add.html", locals())
            else:
                company.save()
                message = 'Company added'
                url = f'/driver/address_company_to/{company.id}/'
                return redirect(url, message)
        else:
            message = "Try again"
            request.session['message'] = message
            return render(request, "add.html", locals())


class AddressCompanyToAllView(View):
    def get(self, request):
        name = 'All Address Company To'
        company = AddressCompanyToModel.objects.all()
        return render(request, 'all_address_to.html', locals())


class AddressCompanyToView(View):
    def get(self, request, id):
        name = 'Address Company To'
        company = get_object_or_404(AddressCompanyToModel, pk=id)
        ctx = {
            'company': company,
            'id': id,
            'name': name,
        }
        return render(request, 'address_id.html', ctx)


class TrailerAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Trailer Add'
        form = TrailerForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Trailer Add'
        form = TrailerForm(request.POST)
        car = CarModel.objects.filter(trailer_id__)
        if form.is_valid():
            model = form.cleaned_data.get('model')
            trailer_number = form.cleaned_data.get('trailer_number')
            weighs = form.cleaned_data.get('weighs')
            tons_cal_load = form.cleaned_data.get('tons_can_load')
            cargo_space = form.cleaned_data.get('cargo_space')
            trailer = TrailerModel()
            trailer.model = model
            trailer.trailer_number = trailer_number.upper()
            trailer.weighs = weighs
            trailer.tons_can_load = tons_cal_load
            trailer.cargo_space = cargo_space
            if TrailerModel.objects.filter(trailer_number=trailer_number.upper()).exists():
                message = 'Objects already exist'
                return render(request, "add.html", locals())
            else:
                trailer.save()
                try:
                    car_trailer_id = CarModel.objects.get(trailer_id=trailer_id)
                    if trailer.id == car_trailer_id:
                        message = 'Company added'
                        url = f'/driver/trailer/{trailer.id}/'
                        car = CarModel.objects.get(car_number=car_number)

                        return redirect(url, message, car)
                except:
                    return redirect(url, message)
                # return redirect('trailer', trailer_id=trailer.id)
        else:
            message = "Try again"
            request.session['message'] = message
            return render(request, "add.html", locals())


class TrailerAllView(View):
    def get(self, request):
        name = 'All Trailer'
        all_trailer = TrailerModel.objects.all()
        return render(request, 'all_trailer.html', locals())


class TrailerView(View):
    def get(self, request, id):
        name = 'Trailer'
        trailer = get_object_or_404(TrailerModel, pk=id)
        ctx = {
            'trailer': trailer,
            'id': id,
            'name': name,
        }
        return render(request, 'trailer_id.html', ctx)


class CarAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Car Add'
        form = CarForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Car Add'
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
            car.car_number = car_number.upper()
            car.weighs = weighs
            car.tons_can_load = tons_cal_load
            car.cargo_space = cargo_space
            car.trailer = trailer
            if CarModel.objects.filter(car_number=car_number.upper()).exists():
                message = 'Objects already exist'
                return render(request, "add.html", locals())
            else:
                car.save()
                message = 'Company added'
                url = f'/driver/car/{car.id}/'
                return redirect(url, message)
        else:
            message = "Try again"
            request.session['message'] = message
            return render(request, "add.html", locals())


class CarAllView(View):
    def get(self, request):
        name = 'Car'
        all_car = CarModel.objects.all()
        return render(request, 'all_car.html', locals())


class CarView(View):
    def get(self, request, id):
        name = 'Car'
        car = get_object_or_404(CarModel, pk=id)
        ctx = {
            'car': car,
            'id': id,
            'name': name,
        }
        return render(request, 'car_id.html', ctx)


class CargoAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Cargo Add'
        form = CargoForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Cargo Add'
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
        name = 'Cargo'
        all_Cargo = CargoModel.objects.all()
        return render(request, 'all_cargo.html', locals())


class PlanCargoAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Plan Cargo Add'
        form = PlanCargoForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Plan Cargo Add'
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
        name = 'Plan Cargo'
        plan_cargo_all = PlanCargoModel.objects.all()
        return render(request, 'all_plan_cargo.html', locals())


class DriverWorkerAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Driver Worker Add'
        form = DriverWorkerForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Driver Worker Add'
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


class DriverWorkerUserView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Driver Worker'
        all_user = UserModel.objects.all()
        return render(request, 'all_user.html', locals())


class AddUserView(LoginRequiredMixin, View):
    template_name = 'add.html'
    name = 'User Add'

    def get(self, request):
        form = AddUserForm()
        return render(request, self.template_name, self.name, locals())

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')
        return render(request, self.template_name, locals())


class ResetPasswordView(LoginRequiredMixin, View):
    name = 'Reset Password'
    template_name = 'add.html'
    permission_required = 'auth.change_user'

    def get(self, request):
        return render(request, self.template_name, self.name, self.permission_required, {'form': ResetPasswordForm()})

    def post(self, request, pk):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = UserModel.objects.get(id=pk)
            user.set_password(form.cleaned_data.get('new_password'))
            user.save()
            return redirect('/login')
        return render(request, self.template_name, self.name, self.permission_required, {'form': form})
