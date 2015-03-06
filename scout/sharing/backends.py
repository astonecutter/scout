from djangae.contrib.gauth.backends import AppEngineUserAPI
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from google.appengine.api import users


class CustomAppEngineUserAPI(AppEngineUserAPI):

     def authenticate(self, **credentials):
        """
        Handles authentication of a user from the given credentials.
        Credentials must be a combination of 'request' and 'google_user'.
         If any other combination of credentials are given then we raise a TypeError, see authenticate() in django.contrib.auth.__init__.py.
        """

        User = get_user_model()

        if len(credentials) != 1:
            # Django expects a TypeError if this backend cannot handle the given credentials
            raise TypeError()

        google_user = credentials.get('google_user', None)

        if google_user:
            user_id = google_user.user_id()
            email = google_user.email().lower()
            try:
                user = User.objects.get(username=user_id)
                return user
            except User.DoesNotExist:
                # Check to see if a User object for this email address has been pre-created.
                try:
                    # Convert the pre-created User object so that the user can now login via
                    # Google Accounts, and ONLY via Google Accounts.
                    user = User.objects.get(email=BaseUserManager.normalize_email(email), username=None)
                    user.username = user_id
                    user.last_login = timezone.now()
                    user.save()
                    return user
                except User.DoesNotExist:
                    # create a user if admin
                    if users.is_current_user_admin():
                        return User.objects.create_user(user_id, email)

        else:
            raise TypeError()  # Django expects to be able to pass in whatever credentials it has, and for you to raise a TypeError if they mean nothing to you
