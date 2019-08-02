from django.views.generic import TemplateView
from django.shortcuts import redirect


class LandingView(TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        # check if there is some video onsite
        if request.user.is_authenticated:
            return redirect('/dashboard')
        else:
            return super().dispatch(request, *args, **kwargs)
