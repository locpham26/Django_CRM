from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Agent, Lead
from .forms import LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail

class LandingPageView(TemplateView):
  template_name = 'landing_page.html'

class LeadListView(ListView):
  template_name = "leads/lead_list.html"
  queryset = Lead.objects.all()
  context_object_name = "leads"

class LeadDetailView(DetailView):
  template_name = "leads/lead_detail.html"
  queryset = Lead.objects.all()
  context_object_name = "lead"

class LeadCreateView(CreateView):
  template_name = "leads/lead_create.html"
  form_class = LeadModelForm
  
  def get_success_url(self):
      return reverse("leads:lead-list")
  
  def form_valid(self, form):
    send_mail(
      subject="A lead was created",
      message="Go to the site",
      from_email="test@test.com",
      recipient_list=["test2@test.com"]
    )
    return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
  template_name = "leads/lead_update.html"
  queryset = Lead.objects.all()
  form_class = LeadModelForm

  def get_success_url(self):
    return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
  template_name = "leads/lead_delete.html"
  queryset = Lead.objects.all()

  def get_success_url(self):
    return reverse("leads:lead-list")
