from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

 
class TiliView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'tili.html'