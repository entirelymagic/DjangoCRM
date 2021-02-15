from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic
from .models import Lead, Agent
from .forms import LeadModelForm


class LandingPageView(generic.TemplateView):
    """A generic landing page for landing.html"""
    template_name = 'landing.html'


# def landing_page(request):
#     return render(request, "landing.html")


class LeadListView(generic.ListView):
    """Used Django List View Class instead of function view lead_list"""
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"  # to overwrite the default object_list and not change leads in HTML templates.


# def lead_list(request):
#     leads = Lead.objects.all()
#
#     context = {
#         'leads': leads
#     }
#     return render(request, "leads/lead_list.html", context)


class LeadDetailView(generic.DetailView):
    """Replaced lead_detail with a django class based view """
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead,
#     }
#     return render(request, "leads/lead_detail.html", context)


class LeadCreateView(generic.CreateView):
    """Replaced lead_create with a django class based view """
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')  # instead of just returning  hardcoded url '/leads'


# def lead_create(request):
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Form submission successful')
#             form.save()
#             return redirect("/leads")
#         else:
#             messages.error(request, 'Form submission with errros')
#     context = {
#         "form": LeadModelForm()
#     }
#     return render(request, "leads/lead_create.html", context)


class LeadUpdateView(generic.UpdateView):
    """Replaced lead_update with a django class based view """
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()  # filter the model based on how the detail view works
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)

class LeadDeleteView(generic.DeleteView):
    """Replaced lead_delete with a django class based view """
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()  # filter the model based on how the detail view works

    def get_success_url(self):
        return reverse('leads:lead-list')


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
