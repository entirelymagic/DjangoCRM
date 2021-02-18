from django.core.mail import send_mail
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Lead, Agent
from .forms import LeadModelForm, CustomUserCreationForm


class SingnupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(generic.TemplateView):
    """A generic landing page for landing.html"""
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, generic.ListView):
    """Used Django List View Class instead of function view lead_list
    LoginRequiredMixin manage the page to be allowed or not based on the user authentication - Must be first Parent.
    """
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"  # to overwrite the default object_list and not change leads in HTML templates.


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """Replaced lead_detail with a django class based view """
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    """Replaced lead_create with a django class based view """
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')  # instead of just returning  hardcoded url '/leads'

    def form_valid(self, form):
        # TODO configure email provider host provider details
        send_mail(
            subject="A lead has been created",
            message='Go to site to see the new lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com'],

        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Replaced lead_update with a django class based view """
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()  # filter the model based on how the detail view works
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Replaced lead_delete with a django class based view """
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()  # filter the model based on how the detail view works

    def get_success_url(self):
        return reverse('leads:lead-list')


