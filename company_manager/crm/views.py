from django.views.generic import CreateView, ListView, TemplateView, UpdateView
import crm.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from crm.forms import CompanyForm

class IndexView(TemplateView):
    template_name = "index.html"

class CompanyCreateView(LoginRequiredMixin, CreateView):
    template_name = "company/create_company.html"
    success_url = reverse_lazy("index")
    form_class = CompanyForm

class OpportunityCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "crm.add_opportunity"
    model = models.Opportunity
    template_name = "company/create_company.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")
    # Translators: This message is shown after successful creation of a company
    success_message = _("Company created!")

class CompanyListView(LoginRequiredMixin, ListView):
    model = models.Company
    template_name = "company/list_company.html"

class OpportunityUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "crm.change_opportunity"
    model = models.Opportunity
    template_name = "opportunity/update_opportunity.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")

class OpportunityUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "crm.change_opportunity"
    model = models.Opportunity
    template_name = "opportunity/update_opportunity.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")

class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ["department", "phone_number", "office_number", "manager"]
    template_name = "employee/update_employee.html"
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."

    def get_object(self, queryset=None):
        return self.request.user.employee

