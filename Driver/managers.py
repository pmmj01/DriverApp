# from django.contrib.auth.base_user import BaseUserManager
#
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password, user_type, **extra_fields):
#         username = self.phone_number
#         if not username:
#             raise ValueError(username)
#         if not user_type:
#             raise ValueError(user_type)
#         phone_number = username
#         user_type = user_type
#         user = self.model(phone_number=phone_number, **extra_fields)
#         user = self.model(user_type=user_type)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def get_by_natural_key(self, username):
#         return self.get(username=self.phone_number)