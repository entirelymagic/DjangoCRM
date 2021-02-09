from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Lead, Agent
from .forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        'leads': leads
    }
    return render(request, "leads/leads.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Form submission successful')
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads")
        else:
            messages.error(request, 'Form submission with errros')
    context = {
        "form": LeadForm()
    }
    return render(request, "leads/lead_create.html", context)