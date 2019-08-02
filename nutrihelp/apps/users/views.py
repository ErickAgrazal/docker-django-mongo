# accounts/views.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registro de usuario"
        context["buttonText"] = "Registrarse"
        return context


class LoginRegular(generic.FormView):
    form_class = AuthenticationForm
    success_url = '/dashboard/'
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Iniciar sesión como usuario"
        context["buttonText"] = "Iniciar sesión"
        return context
