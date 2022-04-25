from django.views.generic import CreateView, ListView, TemplateView, UpdateView
import crm.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class IndexView(TemplateView):
    template_name = "index.html"

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = models.Company
    template_name = "company/create_company.html"
    fields = ["name", "status", "phone_number", "email", "identification_number"]
    success_url = reverse_lazy("index")

class OpportunityCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "crm.add_opportunity"
    model = models.Opportunity
    template_name = "company/create_company.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")

class CompanyListView(ListView):
    model = models.Company
    template_name = "company/list_company.html"

class OpportunityUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "crm.change_opportunity"
    model = models.Opportunity
    template_name = "opportunity/update_opportunity.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")
from django.contrib.messages.views import SuccessMessageMixin
class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ["department"]
    template_name = "employee/update_employee.html"
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."

    def get_object(self, queryset=None):
        return self.request.user.employee

