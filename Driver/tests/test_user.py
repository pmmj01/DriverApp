import pytest
from django.urls import reverse
from Driver.models import UserModel, CustomUserManager
from Driver.forms import UserAddForm
from Driver.views import UserView, UserAddView, UserAllView, UserEditView, UserDeleteView
from Driver.choices import USER, DRIVER_LICENSE

@pytest.mark.django_db
def test_user_add(client):
    response = client.get(reverse('add_user'), {'phone_number':'+48123456789', 'first_name':'Jan', 'last_name':'Kowalski', 'user_type':'driver', 'driving_license':'C'})
    assert response.status_code == 302
    assert len(UserModel.objects.all()) == 1
    user = UserModel.objects.first()
    assert user.phone_numer == '+48123456789'
    assert user.first_name == 'Jan'
    assert user.last_name == 'Kowalski'
    assert user.user_type == 'driver'
    assert user.driving_license == 'C'


@pytest.mark.django_db
def test_user_view_404(client, user_view):
    response = client.get(reverse('u_user', kwargs={'id_': 1000}))
    assert response.status_code == 404


def test_to_fail():
    assert False



@pytest.mark.django_db
def test_phone_number_required():
    user = UserModel(phone_number=None, user_type='Admin', first_name='John', last_name='Doe')
    with pytest.raises(ValueError, match="The given phone number must be set"):
        user.full_clean()


@pytest.mark.django_db
def test_user_type_required():
    user = UserModel(phone_number='+123456789', user_type=None, first_name='John', last_name='Doe')
    with pytest.raises(ValueError, match="The given user type must be set"):
        user.full_clean()


@pytest.mark.django_db
def test_first_name_required():
    user = UserModel(phone_number='+123456789', user_type='Admin', first_name=None, last_name='Doe')
    with pytest.raises(ValueError, match="The given first name must be set"):
        user.full_clean()