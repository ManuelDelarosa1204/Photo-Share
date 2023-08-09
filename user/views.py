from django.contrib.auth.views import LoginView as Login, LogoutView as Logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import RegistrationForm, LoginForm
from photos.models import Image


class RegisterView(CreateView):
    """Use this view to register new user's"""

    model = User
    template_name = "user/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("user:login")


class LoginView(Login):
    """Use this view to login user's"""

    authentication_form = LoginForm
    template_name = "user/login.html"

    def get_success_url(self) -> str:
        return reverse_lazy("user:profile", args=[self.request.user.slug])


class LogoutView(Logout):
    """User this view to log user's out"""

    pass


class ProfileView(DetailView):
    model = User
    template_name = "user/profile.html"
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get public images from the owner of the profile
        context["public_images"] = Image.objects.filter(user=self.get_object()).filter(status=Image.Status.PUBLIC)
        return context
