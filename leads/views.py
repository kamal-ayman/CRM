from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic 
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreateForm
from agents.mixins import OrganisorLoginRequiredMixin


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreateForm  
    
    def get_success_url(self):
        return reverse("login")


class LandingViewPage(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")

# ####################

class LeadListView(LoginRequiredMixin, generic.ListView):
    model = Lead
    context_object_name = "leads"
    template_name = "leads/lead_list.html"

    def get_queryset(self):
        queryset = Lead.objects.all()
        if self.request.uesr.is_agent:
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request, "leads/lead_list.html", context)

# #################

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    model = Lead
    pk_url_kwarg = 'id'
    context_object_name = "lead"
    template_name = "leads/lead_detail.html"
    


def lead_detail(request, id):
    lead = Lead.objects.get(id=id)
    context = {
        "lead":lead
    }
    return render(request, "leads/lead_detail.html", context)

# #################


class LeadCreateView(OrganisorLoginRequiredMixin, generic.CreateView):
    model = Lead
    pk_url_kwarg = 'id'
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created", 
            message="Go to the site to see the new lead",
            from_email="test@test.com", 
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)



def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/leads")
    context = {
        "form":form
    }
    return render(request, "leads/lead_create.html", context)

# #################


class LeadUpdateView(OrganisorLoginRequiredMixin, generic.UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    pk_url_kwarg = 'id'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_update(request, id):
    lead = Lead.objects.get(id=id)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/leads")
    context = {
        "form":form, 
        "lead":lead
    } 
    return render(request, "leads/lead_update.html", context)


# #################

class LeadDeleteView(OrganisorLoginRequiredMixin, generic.DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"
    pk_url_kwarg = 'id'




    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_delete(request, id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    return redirect("/leads")

# def lead_update(request, id):
#     lead = Lead.objects.get(id=id)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form":form,
#         "lead":lead
#     }
#     return render(request, "leads/lead_update.html", context)


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print("Receiving post request")
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print("The form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name, 
#                 last_name=last_name, 
#                 age=age,
#                 agent=agent
#             )
#             print("Done Created")
#             return redirect("/leads")

#     context = {
#         "form":form
#     }
#     return render(request, "leads/lead_create.html", context)