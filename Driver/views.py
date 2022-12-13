from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from Driver.forms import *
from django.views import View


#TODO class description
#TODO User
#TODO cargo
#TODO plan
#TODO worker side
#TODO info and contact to me
#TODO tests


class UserAddView(LoginRequiredMixin, View):
    template_name = 'add.html'
    name = 'User Add'

    def get(self, request):
        return render(request, self.template_name, {'form': UserAddForm()})

    def post(self, request):
        form = UserAddForm(request.POST)
        if form.is_valid():
            pk = form.cleaned_data.get('id')
            phone_number = form.cleaned_data.get('phone_number')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            driving_license = form.cleaned_data.get('driving_license')
            user = UserModel()
            user.pk = pk
            user.phone_number = phone_number
            user.first_name = first_name
            user.last_name = last_name
            user.driving_license = driving_license
            form.save()
            return redirect('all_user')
        return render(request, self.template_name, {'form': form})


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


class UserAllView(LoginRequiredMixin, View):
    """
    The function displays all users except "Super User"

    The user should be logged in to be able to see users in the database,
    To see all users, you must have "Manager" permissions

    :return list of users.
    """
    def get(self, request):
        users = UserModel.objects.exclude(is_superuser=True)
        return render(request, 'all_user.html', locals())


class UserEditView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Edit User'
        obj = get_object_or_404(UserModel, pk=id)
        form = UserAddForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit User'
        obj = get_object_or_404(UserModel, pk=id)
        form = UserAddForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            message = 'User edit'
            url = f'/driver/user/{obj.id}/'
            return redirect(url, message)


class UserView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'User'
        user = get_object_or_404(UserModel, pk=id)
        url = f'/driver/user/{id}/'
        ctx = {
            'user': user,
            'id': id,
            'name': name,
        }
        return render(request, 'user_id.html', ctx)


class UserDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete User'
        user = get_object_or_404(UserModel, pk=id)
        user.delete()
        message = 'User delete'
        url = f'/driver/all/user'
        return redirect(url, message)


class AddressCompanyFromAddView(LoginRequiredMixin, View):
    """
    The function allows you to add the client's company address

    It is obligatory to provide: company name, state, city, zip code, street, property number.
    Additionally, you can say:
    more information.

    The function returns the address from large letters.

    :raise If there is a record with the same:
        Name, state, city, postal code, street, property number.
        Returns the message "Objects already exist".

    :return Adderss in a view for one full record.

    """
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
        cod = 'from'
        name = 'Address Company From'
        company = get_object_or_404(AddressCompanyFromModel, pk=id)
        ctx = {
            'company': company,
            'id': id,
            'name': name,
            'cod': cod,
        }
        return render(request, 'address_id.html', ctx)


class AddressCompanyFromEditView(View):
    def get(self, request, id):
        name = 'Edit Address Company From'
        obj = get_object_or_404(AddressCompanyFromModel, pk=id)
        form = AddressCompanyFromForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Address Company From'
        obj = get_object_or_404(AddressCompanyFromModel, pk=id)
        form = AddressCompanyFromForm(request.POST, instance=obj)
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
                                                      address_property_first=address_property_first):
                message = 'Nothing changed'
                return render(request, "edit.html", locals())
            else:
                form.save()
                message = 'Company edit'
                url = f'/driver/address_company_from/{obj.id}/'
                return redirect(url, message)


class AddressCompanyFromDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Address Company From'
        company = get_object_or_404(AddressCompanyFromModel, pk=id)
        company.delete()
        message = 'Company address delete'
        url = f'/driver/all/address_company_from/'
        return redirect(url, message)


class AddressCompanyToAddView(LoginRequiredMixin, View):
    """
    The function allows you to add the client's company address

    It is obligatory to provide: company name, state, city, zip code, street, property number.
    Additionally, you can say:
    more information.

    The function returns the address from large letters.

    :raise If there is a record with the same:
        Name, state, city, postal code, street, property number.
        Returns the message "Objects already exist".

    :return Adderss in a view for one full record.

    """
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
        cod = 'to'
        name = 'Address Company To'
        company = get_object_or_404(AddressCompanyToModel, pk=id)
        ctx = {
            'company': company,
            'id': id,
            'name': name,
            'cod': cod,
        }
        return render(request, 'address_id.html', ctx)


class AddressCompanyToEditView(View):
    def get(self, request, id):
        name = 'Edit Address Company To'
        obj = get_object_or_404(AddressCompanyToModel, pk=id)
        form = AddressCompanyToForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Address Company To'
        obj = get_object_or_404(AddressCompanyToModel, pk=id)
        form = AddressCompanyToForm(request.POST, instance=obj)
        if form.is_valid():
            company_name = form.cleaned_data.get("company_name")
            address_country = form.cleaned_data.get("address_country")
            address_city = form.cleaned_data.get("address_city")
            address_zip_code = form.cleaned_data.get("address_zip_code")
            address_street = form.cleaned_data.get("address_street")
            address_property_first = form.cleaned_data.get("address_property_first")
            address_property_second = form.cleaned_data.get("address_property_second")
            address_more_info = form.cleaned_data.get("address_more_info")
            company = AddressCompanyToModel()
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
                                                      address_property_first=address_property_first):
                message = 'Nothing changed'
                return render(request, "edit.html", locals())
            else:
                form.save()
                message = 'Company edit'
                url = f'/driver/address_company_to/{obj.id}/'
                return redirect(url, message)


class AddressCompanyToDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Address Company To'
        company = get_object_or_404(AddressCompanyToModel, pk=id)
        company.delete()
        message = 'Company address delete'
        url = f'/driver/all/address_company_to/'
        return redirect(url, message)


class TrailerAddView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Add Trailer'
        form = TrailerForm()
        return render(request, 'add.html', locals())

    def post(self, request):
        name = 'Add Trailer'
        form = TrailerForm(request.POST)
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
                message = 'Trailer added'
                url = f'/driver/trailer/{trailer.id}/'
                return redirect(url, message)
        else:
            message = "Try again"
            request.session['message'] = message
            return render(request, "add.html", locals())


class TrailerAllView(View):
    def get(self, request):
        name = 'All Trailer'
        trailer = TrailerModel.objects.all()
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


class TrailerEditView(View):
    def get(self, request, id):
        name = 'Edit Trailer'
        obj = get_object_or_404(TrailerModel, pk=id)
        form = TrailerForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Trailer'
        obj = get_object_or_404(TrailerModel, pk=id)
        form = TrailerForm(request.POST, instance=obj)
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
            if TrailerModel.objects.filter(model=trailer.model, weighs=trailer.weighs,
                                           tons_can_load=trailer.tons_can_load, cargo_space=trailer.cargo_space):
                message = 'Nothing changed'
                return render(request, "edit.html", locals())
            else:
                form.save()
                message = 'Trailer edit'
                url = f'/driver/trailer/{obj.id}/'
                return redirect(url, message)


class TrailerDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Trailer'
        obj = get_object_or_404(TrailerModel, pk=id)
        obj.delete()
        message = 'Trailer delete'
        url = f'/driver/all/trailer/'
        return redirect(url, message)


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
        car = CarModel.objects.all()
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


class CarEditView(View):
    def get(self, request, id):
        name = 'Edit Car'
        obj = get_object_or_404(CarModel, pk=id)
        form = CarForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Car'
        obj = get_object_or_404(CarModel, pk=id)
        form = CarForm(request.POST, instance=obj)
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
            if CarModel.objects.filter(model=car.model, weighs=car.weighs,
                                           tons_can_load=car.tons_can_load, cargo_space=car.cargo_space):
                message = 'Nothing changed'
                return render(request, "edit.html", locals())
            else:
                form.save()
                message = 'Car edit'
                url = f'/driver/car/{obj.id}/'
                return redirect(url, message)


class CarDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Car'
        obj = get_object_or_404(CarModel, pk=id)
        obj.delete()
        message = 'Car delete'
        url = f'/driver/all/car/'
        return redirect(url, message)


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
            message = 'Cargo added'
            url = f'/driver/cargo/{cargo.id}/'
            return redirect(url, message)
        return render(request, 'add.html', locals())


class CargoAllView(View):
    def get(self, request):
        name = 'Cargo'
        all_cargo = CargoModel.objects.all()
        return render(request, 'all_cargo.html', locals())


class CargoView(View):
    def get(self, request, id):
        name = 'Cargo'
        cargo = get_object_or_404(CargoModel, pk=id)
        ctx = {
            'cargo': cargo,
            'id': id,
            'name': name,
        }
        return render(request, 'cargo_id.html', ctx)


class CargoEditView(View):
    def get(self, request, id):
        name = 'Edit Cargo'
        obj = get_object_or_404(CargoModel, pk=id)
        form = CargoForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Cargo'
        obj = get_object_or_404(CargoModel, pk=id)
        form = CargoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            message = 'Cargo edit'
            url = f'/driver/Cargo/{obj.id}/'
            return redirect(url, message)


class CargoDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Cargo'
        obj = get_object_or_404(CargoModel, pk=id)
        obj.delete()
        message = 'Cargo delete'
        url = f'/driver/all/cargo/'
        return redirect(url, message)



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
            message = 'Plan Cargo added'
            url = f'/driver/plan_cargo/{plan_cargo.id}/'
            return redirect(url, message)
        return render(request, 'add.html', locals())


class PlanCargoAllView(View):
    def get(self, request):
        name = 'Plan Cargo'
        plan_cargo_all = PlanCargoModel.objects.all()
        return render(request, 'all_plan_cargo.html', locals())


class PlanCargoView(View):
    def get(self, request, id):
        name = 'Trailer'
        trailer = get_object_or_404(TrailerModel, pk=id)
        ctx = {
            'trailer': trailer,
            'id': id,
            'name': name,
        }
        return render(request, 'trailer_id.html', ctx)


class PlanCargoEditView(View):
    def get(self, request, id):
        name = 'Edit Plan Cargo'
        obj = get_object_or_404(PlanCargoModel, pk=id)
        form = PlanCargoForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Plan Cargo'
        obj = get_object_or_404(PlanCargoModel, pk=id)
        form = PlanCargoForm(request.POST, instance=obj)
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
            message = 'Plan Cargo added'
            url = f'/driver/plan_cargo/{plan_cargo.id}/'
            return redirect(url, message)
        return render(request, 'add.html', locals())


class PlanCargoDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Plan Cargo'
        obj = get_object_or_404(PlanCargoModel, pk=id)
        obj.delete()
        message = 'Plan Cargo delete'
        url = f'/driver/all/plan_cargo/'
        return redirect(url, message)


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
            message = 'Driver Worker added'
            url = f'/driver/driver_worker/{driver_worker.id}/'
            return redirect(url, message)
        return render(request, 'add.html', locals())


class DriverWorkerAllView(LoginRequiredMixin, View):
    def get(self, request):
        name = 'Driver Worker'
        all_driver_worker = DriverWorkerModel.objects.all()
        return render(request, 'all_driver_worker.html', locals())


class DriverWorkerView(View):
    def get(self, request, id):
        name = 'Driver Worker'
        driver_worker = get_object_or_404(DriverWorkerModel, pk=id)
        ctx = {
            'driver_worker': driver_worker,
            'id': id,
            'name': name,
        }
        return render(request, 'driver_worker_id.html', ctx)


class DriverWorkerEditView(View):
    def get(self, request, id):
        name = 'Edit Driver Worker'
        obj = get_object_or_404(DriverWorkerModel, pk=id)
        form = DriverWorkerForm(instance=obj)
        return render(request, 'edit.html', locals())

    def post(self, request, id):
        name = 'Edit Driver Worker'
        obj = get_object_or_404(DriverWorkerModel, pk=id)
        form = DriverWorkerForm(request.POST, instance=obj)
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
            message = 'Driver Worker added'
            url = f'/driver/driver_worker/{driver_worker.id}/'
            return redirect(url, message)
        return render(request, 'add.html', locals())


class DriverWorkerDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        name = 'Delete Driver Worker'
        obj = get_object_or_404(DriverWorkerModel, pk=id)
        obj.delete()
        message = 'Driver Worker delete'
        url = f'/driver/all/driver_worker/'
        return redirect(url, message)
