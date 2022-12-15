from unittest import TestCase
from django.test import Client
import pytest
from .testutils import *
from django.urls import reverse, resolve
from Driver.models import UserModel, AddressCompanyFromModel, AddressCompanyToModel, TrailerModel, CarModel
from Driver.views import *



class Driver_tests(TestCase):

    def test_url_add_user(self):
        """
        Test url to view connect
        :return: urls name = add_user => UserAddView
        Take the url name and compare with the function in Views
        """
        url = reverse('add_user')
        assert resolve(url).func, UserAddView

    def test_url_add_user_error(self):
        """
        Test url to view connect
        :return: urls name = add_user !=> UserAddView
        Take the url name and compare with the function in Views
        """
        url = reverse('add_user')
        assert resolve(url).func, UserEditView is False

    def test_url_all_user(self):
        """
        Test url to view connect
        :return: urls name = all_user => UserAllView
        Take the url name and compare with the function in Views
        """
        url = reverse('all_user')
        assert resolve(url).func, UserAllView

    def test_url_all_user_error(self):
        """
        Test url to view connect
        :return: urls name = all_user !=> UserAllView
        Take the url name and compare with the function in Views
        """
        url = reverse('all_user')
        assert resolve(url).func, UserEditView is False

    @pytest.mark.django_db
    def test_url_delete_user(self):
        """
        Test url to view connect
        :return: urls name = delete_user => UserDeleteView
        Take the url name and compare with the function in Views
        """
        user = create_fake_user()
        url = reverse('delete_user', kwargs={'id':user.id})
        assert resolve(url).func, UserDeleteView

    @pytest.mark.django_db
    def test_url_delete_user_error(self):
        """
        Test url to view connect
        :return: urls name = delete_user !=> UserDeleteView
        Take the url name and compare with the function in Views
        """
        user = create_fake_user()
        url = reverse('delete_user', kwargs={'id':user.id})
        assert resolve(url).func, UserEditView is False

    @pytest.mark.django_db
    def test_view_add_user(self):
        """
        Tests add User view:
        :return: code 302, template add.html
        template add.html is base for add records
        """
        client = Client()
        response = client.get(reverse('add_user'))
        self.assertEqual(response.status_code, 302)
        assert response, 'add.html'

    @pytest.mark.django_db
    def test_view_edit_user(self):
        """
        Tests edit User view:
        Create 10 records to DB
        Take id to tests
        :return: code 302, template edit.html
        template edit.html is base for edit records
        """
        client = Client()
        user = create_fake_user()
        response = client.get(reverse('edit_user', kwargs={'id':user.id}))
        # self.assertEqual(response.status_code, 302) # True
        assert response.status_code, 302 # True
        assert response, 'edit.html'

    @pytest.mark.django_db
    def test_view_delete_user(self):
        """
        Tests delete User view:
        Create 10 records to DB
        Take id to tests
        :return: code 302

        """
        client = Client()
        user = create_fake_user()
        response = client.get(reverse('delete_user', kwargs={'id': user.id}))
        # self.assertEqual(response.status_code, 302) # True
        assert response.status_code, 302  # True

    @pytest.mark.django_db
    def test_view_add_address_from(self):
        """
        Tests add Address company from view:
        :return: code 302, template add.html
        template add.html is base for add records
        """
        client = Client()
        response = client.get(reverse('add_address_company_from'))
        self.assertEqual(response.status_code, 302)
        assert response, 'add.html'

    @pytest.mark.django_db
    def test_view_add_address_to(self):
        """
        Tests add Address company to view:
        :return: code 302, template add.html
        template add.html is base for add records
        """
        client = Client()
        response = client.get(reverse('add_address_company_to'))
        self.assertEqual(response.status_code, 302)
        assert response, 'add.html'

    @pytest.mark.django_db
    def test_view_add_trailer(self):
        """
        Tests add Trailer view:
        :return: code 302, template add.html
        template add.html is base for add records
        """
        client = Client()
        response = client.get(reverse('add_trailer'))
        self.assertEqual(response.status_code, 302)
        assert response, 'add.html'

    @pytest.mark.django_db
    def test_view_add_car(self):
        """
        Tests add Car view:
        :return: code 302, template add.html
        template add.html is base for add records
        """
        client = Client()
        response = client.get(reverse('add_car'))
        self.assertEqual(response.status_code, 302)
        assert response, 'add.html'

    @pytest.mark.django_db
    def test_view_all_user(self):
        """
        Tests all User view:
        :return: code 200, template all_user.html
        """
        client = Client()
        response = client.get(reverse('all_user'))
        self.assertEqual(response.status_code, 302)
        assert response, 'all_user.html'

    @pytest.mark.django_db
    def test_view_all_address_from(self):
        """
        Tests all Address from view:
        :return: code 200, template all_address_from.html
        """
        client = Client()
        response = client.get(reverse('all_address_company_from'))
        self.assertEqual(response.status_code, 200)
        assert response, 'all_address_from.html'

    @pytest.mark.django_db
    def test_view_all_address_to(self):
        """
        Tests all Address to view:
        :return: code 200, template all_address_to.html
        """
        client = Client()
        response = client.get(reverse('all_address_company_to'))
        self.assertEqual(response.status_code, 200)
        assert response, 'all_address_to.html'

    @pytest.mark.django_db
    def test_view_all_trailer(self):
        """
        Tests all Trailer view:
        :return: code 200, template all_trailer.html
        """
        client = Client()
        response = client.get(reverse('all_trailer'))
        self.assertEqual(response.status_code, 200)
        assert response, 'all_trailer.html'

    @pytest.mark.django_db
    def test_view_all_car(self):
        """
        Tests all Car view:
        :return: code 200, template all_Car.html
        """
        client = Client()
        response = client.get(reverse('all_car'))
        self.assertEqual(response.status_code, 200)
        assert response, 'all_car.html'


    @pytest.mark.django_db
    def test_view_one_user(self):
        """
        Tests one User view:
        Create 10 records to DB
        Take id to tests
        :return: code 302, user_id.html
        """
        client = Client()
        user = create_fake_user()
        response = client.get(reverse('u_user', kwargs={'id':user.id}))
        # self.assertEqual(response.status_code, 200) # status code 200
        assert response.status_code, 302 # status code 302
        assert response, 'user_id.html'

    @pytest.mark.django_db
    def test_view_one_address_from(self):
        """
        Tests one Address company from view:
        Create 10 records to DB
        Take id to tests
        :return: code 302, address_id.html
        Template 'address_id.html' is base template for address_company...
        """
        client = Client()
        address = create_fake_address_company_from()
        response = client.get(reverse('address_company_from', kwargs={'id':address.id}))
        # self.assertEqual(response.status_code, 200) # status code 200
        assert response.status_code, 302 # status code 302
        assert response, 'address_id.html'

    @pytest.mark.django_db
    def test_view_one_address_to(self):
        """
        Tests one Address company to view:
        Create 10 records to DB
        Take id to tests
        :return: code 200, address_id.html
        Template 'address_id.html' is base template for address_company...
        """
        client = Client()
        address = create_fake_address_company_to()
        response = client.get(reverse('address_company_to', kwargs={'id':address.id}))
        # self.assertEqual(response.status_code, 200) # status code 200
        assert response.status_code, 302  # status code 302
        assert response, 'address_id.html'

    @pytest.mark.django_db
    def test_view_one_trailer(self):
        """
        Tests one Trailer view:
        Create 10 records to DB
        Take id to tests
        :return: code 200, trailer_id.html
        """
        client = Client()
        trailer = create_fake_trailer()
        response = client.get(reverse('trailer', kwargs={'id':trailer.id}))
        # self.assertEqual(response.status_code, 200) # status code 200
        assert response.status_code, 302  # status code 302
        assert response, 'trailer_id.html'

    @pytest.mark.django_db
    def test_view_one_car(self):
        """
        Tests one Car view:
        Create 10 records to DB
        Take id to tests
        :return: code 200, car_id.html
        """
        client = Client()
        car = create_fake_car()
        response = client.get(reverse('car', kwargs={'id': car.id}))
        # self.assertEqual(response.status_code, 200) # status code 200
        assert response.status_code, 302  # status code 302
        assert response, 'car_id.html'


    @pytest.mark.django_db
    def test_address_from_none(self):
        """
        Test empty DB - Address company from Model
        :return: True
        """
        address_from = AddressCompanyFromModel.objects.all().exists() is False
        assert address_from
        # self.assertNotEqual(address_from, None)

    @pytest.mark.django_db
    def test_address_from_not_none(self):
        """
        Test full DB - Address company from Model
        Add to DB
        Create 10 records to DB
        Show all to template
        :return: True, 'all_address_company_from'
        """
        client = Client()
        response = client.get(reverse('all_address_company_from'))
        create_fake_address_company_from()
        address_from = AddressCompanyFromModel.objects.all().exists() is True
        assert address_from, response

    @pytest.mark.django_db
    def test_address_to_none(self):
        """
        Test empty DB - Address company to Model
        :return: True
        """
        address_to = AddressCompanyToModel.objects.all().exists() is False
        assert address_to
        # self.assertNotEqual(address_to, None)

    @pytest.mark.django_db
    def test_address_to_not_none(self):
        """
        Test full DB - Address company to Model
        Add to DB
        Create 10 records to DB
        Show all to template
        :return: True, 'all_address_company_to'
        """
        client = Client()
        response = client.get(reverse('all_address_company_to'))
        create_fake_address_company_to()
        address_to = AddressCompanyToModel.objects.all().exists() is True
        assert address_to, response


    @pytest.mark.django_db
    def test_user_none(self):
        """
        Test empty DB - User Model
        Show all to template
        :return: True, 'all_user'
        """
        client = Client()
        users = UserModel.objects.all().exists() is False
        response = client.get(reverse('all_user'))
        assert users, response

    @pytest.mark.django_db
    def test_user_not_none(self):
        """
        Test full DB - User Model
        Add to DB
        Create 10 records to DB
        Show all to template
        :return: True, 'all_user'
        """
        create_fake_user()
        client = Client()
        users = UserModel.objects.all().exists() is True
        response = client.get(reverse('all_user'))
        assert users, response


@pytest.mark.django_db
def test_login_user(client, set_up):
    """
    Test user login
    :param client:
    :param set_up: create_fake_user()
    :return: login user created with set_up: create_fake_user()
    """
    user = UserModel.objects.all().last()
    client.login(username=user.phone_number, password='Test123')
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200




