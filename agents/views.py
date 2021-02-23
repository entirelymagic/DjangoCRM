from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm


# Create your views here.
class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        """If the creation of agent is successful go to agent list view."""
        return reverse("agents:agent-list")

    def form_valid(self, form):
        """if the form is valid add organization to agent from the user and commit it to database."""
        agent = form.save(commit=False)  # so it is not saved to database now
        agent.organization = self.request.user.userprofile
        agent.save()  # Commit to database
        return super(AgentCreateView, self).form_valid(form)
