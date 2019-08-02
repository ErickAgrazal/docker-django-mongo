# exams/views.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView

from .forms import TakeExamForm


class TakeExamView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/dashboard/'
    form_class = TakeExamForm
    template_name = 'form.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()
        return super(TakeExamView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(TakeExamView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Examen"
        context["buttonText"] = "Enviar"
        return context
