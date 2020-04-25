from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse


# Create your views here.
class ServicesView(ListView):
    model = Services
    template_name = 'services/services.html'
    context_object_name = 'objects'


class ServicesDetailView(DetailView):
    model = Services

# ------------------------------------------------------------------------------------------------------------------------------------------------


class CEListView(ListView):
    model = ComputeEngine
    template_name = 'console/compute-engine/cevm-instance.html'
    context_object_name = 'ceinstance'
    ordering = ['-date_posted']


class CEGroupListView(ListView):
    model = ComputeEngine
    template_name = 'console/compute-engine/ceinstance-groups.html'
    context_object_name = 'ceinstance'
    ordering = ['-date_posted']


class CEDetailView(DetailView):
    model = ComputeEngine


class CECreateView(LoginRequiredMixin, CreateView):
    model = ComputeEngine
    fields = ['title', 'os', 'ram',
              'harddisk', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CEUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ComputeEngine
    fields = ['title', 'os', 'ram',
              'harddisk', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ceinstance = self.get_object()
        if self.request.user == ceinstance.user:
            return True
        return False


class CEDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ComputeEngine
    success_url = "/console/"

    def test_func(self):
        ceinstance = self.get_object()
        if self.request.user == ceinstance.user:
            return True
        return False

# ------------------------------------------------------------------------------------------------------------------------------------------------


class AEListView(ListView):
    model = AppEngine
    template_name = 'console/app-engine/aevm-instance.html'
    context_object_name = 'aeinstance'
    ordering = ['-date_posted']


class AEGroupListView(ListView):
    model = AppEngine
    template_name = 'console/app-engine/aeinstance-groups.html'
    context_object_name = 'aeinstance'
    ordering = ['-date_posted']


class AEDetailView(DetailView):
    model = AppEngine


class AECreateView(LoginRequiredMixin, CreateView):
    model = AppEngine
    fields = ['title', 'os', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AEUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AppEngine
    fields = ['title', 'os', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        aeinstance = self.get_object()
        if self.request.user == aeinstance.user:
            return True
        return False


class AEDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AppEngine
    success_url = "/console/"

    def test_func(self):
        aeinstance = self.get_object()
        if self.request.user == aeinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class DBListView(ListView):
    model = Database
    template_name = 'console/database/db-instance.html'
    context_object_name = 'dbinstance'
    ordering = ['-date_posted']


class DBGroupListView(ListView):
    model = Database
    template_name = 'console/database/dbinstance-groups.html'
    context_object_name = 'dbinstance'
    ordering = ['-date_posted']


class DBDetailView(DetailView):
    model = Database


class DBCreateView(LoginRequiredMixin, CreateView):
    model = Database
    fields = ['title', 'database', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DBUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Database
    fields = ['title', 'database', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        dbinstance = self.get_object()
        if self.request.user == dbinstance.user:
            return True
        return False


class DBDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Database
    success_url = "/console/"

    def test_func(self):
        dbinstance = self.get_object()
        if self.request.user == dbinstance.user:
            return True
        return False

# ------------------------------------------------------------------------------------------------------------------------------------------------


class ISListView(ListView):
    model = Infastructure
    template_name = 'console/infastructure/is-instance.html'
    context_object_name = 'isinstance'
    ordering = ['-date_posted']


class ISGroupListView(ListView):
    model = Infastructure
    template_name = 'console/infastructure/isinstance-groups.html'
    context_object_name = 'isinstance'
    ordering = ['-date_posted']


class ISDetailView(DetailView):
    model = Infastructure


class ISCreateView(LoginRequiredMixin, CreateView):
    model = Infastructure
    fields = ['title', 'infastructure', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ISUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Infastructure
    fields = ['title', 'infastructure', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        isinstance = self.get_object()
        if self.request.user == isinstance.user:
            return True
        return False


class ISDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Infastructure
    success_url = "/console/"

    def test_func(self):
        isinstance = self.get_object()
        if self.request.user == isinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class CMSListView(ListView):
    model = CMS
    template_name = 'console/cms/cms-instance.html'
    context_object_name = 'cmsinstance'
    ordering = ['-date_posted']


class CMSGroupListView(ListView):
    model = CMS
    template_name = 'console/cms/cmsinstance-groups.html'
    context_object_name = 'cmsinstance'
    ordering = ['-date_posted']


class CMSDetailView(DetailView):
    model = CMS


class CMSCreateView(LoginRequiredMixin, CreateView):
    model = CMS
    fields = ['title', 'cms', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CMSUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CMS
    fields = ['title', 'cms', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cmsinstance = self.get_object()
        if self.request.user == cmsinstance.user:
            return True
        return False


class CMSDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CMS
    success_url = "/console/"

    def test_func(self):
        cmsinstance = self.get_object()
        if self.request.user == cmsinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class DTListView(ListView):
    model = DeveloperTools
    template_name = 'console/developer_tools/dt-instance.html'
    context_object_name = 'dtinstance'
    ordering = ['-date_posted']


class DTGroupListView(ListView):
    model = DeveloperTools
    template_name = 'console/developer_tools/dtinstance-groups.html'
    context_object_name = 'dtinstance'
    ordering = ['-date_posted']


class DTDetailView(DetailView):
    model = DeveloperTools


class DTCreateView(LoginRequiredMixin, CreateView):
    model = DeveloperTools
    fields = ['title', 'developer_tools', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DTUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DeveloperTools
    fields = ['title', 'developer_tools', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        dtinstance = self.get_object()
        if self.request.user == dtinstance.user:
            return True
        return False


class DTDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DeveloperTools
    success_url = "/console/"

    def test_func(self):
        dtinstance = self.get_object()
        if self.request.user == dtinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class ECListView(ListView):
    model = ECommerce
    template_name = 'console/e_commerce/ec-instance.html'
    context_object_name = 'ecinstance'
    ordering = ['-date_posted']


class ECGroupListView(ListView):
    model = ECommerce
    template_name = 'console/e_commerce/ecinstance-groups.html'
    context_object_name = 'ecinstance'
    ordering = ['-date_posted']


class ECDetailView(DetailView):
    model = ECommerce


class ECCreateView(LoginRequiredMixin, CreateView):
    model = ECommerce
    fields = ['title', 'e_commerce', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ECUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ECommerce
    fields = ['title', 'e_commerce', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ecinstance = self.get_object()
        if self.request.user == ecinstance.user:
            return True
        return False


class ECDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ECommerce
    success_url = "/console/"

    def test_func(self):
        ecinstance = self.get_object()
        if self.request.user == ecinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class CRMListView(ListView):
    model = CRM
    template_name = 'console/crm/crm-instance.html'
    context_object_name = 'crminstance'
    ordering = ['-date_posted']


class CRMGroupListView(ListView):
    model = CRM
    template_name = 'console/crm/crminstance-groups.html'
    context_object_name = 'crminstance'
    ordering = ['-date_posted']


class CRMDetailView(DetailView):
    model = CRM


class CRMCreateView(LoginRequiredMixin, CreateView):
    model = CRM
    fields = ['title', 'crm', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CRMUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CRM
    fields = ['title', 'crm', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        crminstance = self.get_object()
        if self.request.user == crminstance.user:
            return True
        return False


class CRMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CRM
    success_url = "/console/"

    def test_func(self):
        crminstance = self.get_object()
        if self.request.user == crminstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class BIListView(ListView):
    model = BusinessIntelligence
    template_name = 'console/business_intelligence/bi-instance.html'
    context_object_name = 'biinstance'
    ordering = ['-date_posted']


class BIGroupListView(ListView):
    model = BusinessIntelligence
    template_name = 'console/business_intelligence/biinstance-groups.html'
    context_object_name = 'biinstance'
    ordering = ['-date_posted']


class BIDetailView(DetailView):
    model = BusinessIntelligence


class BICreateView(LoginRequiredMixin, CreateView):
    model = BusinessIntelligence
    fields = ['title', 'business_intelligence', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BIUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BusinessIntelligence
    fields = ['title', 'business_intelligence', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        biinstance = self.get_object()
        if self.request.user == biinstance.user:
            return True
        return False


class BIDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BusinessIntelligence
    success_url = "/console/"

    def test_func(self):
        biinstance = self.get_object()
        if self.request.user == biinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class ChatListView(ListView):
    model = Chat
    template_name = 'console/chat/chat-instance.html'
    context_object_name = 'chatinstance'
    ordering = ['-date_posted']


class ChatGroupListView(ListView):
    model = Chat
    template_name = 'console/chat/chatinstance-groups.html'
    context_object_name = 'chatinstance'
    ordering = ['-date_posted']


class ChatDetailView(DetailView):
    model = Chat


class ChatCreateView(LoginRequiredMixin, CreateView):
    model = Chat
    fields = ['title', 'chat', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chat
    fields = ['title', 'chat', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        chatinstance = self.get_object()
        if self.request.user == chatinstance.user:
            return True
        return False


class ChatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chat
    success_url = "/console/"

    def test_func(self):
        chatinstance = self.get_object()
        if self.request.user == chatinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class AnalyticsListView(ListView):
    model = Analytics
    template_name = 'console/analytics/analytics-instance.html'
    context_object_name = 'analyticsinstance'
    ordering = ['-date_posted']


class AnalyticsGroupListView(ListView):
    model = Analytics
    template_name = 'console/analytics/analyticsinstance-groups.html'
    context_object_name = 'analyticsinstance'
    ordering = ['-date_posted']


class AnalyticsDetailView(DetailView):
    model = Analytics


class AnalyticsCreateView(LoginRequiredMixin, CreateView):
    model = Analytics
    fields = ['title', 'analytics', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnalyticsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Analytics
    fields = ['title', 'analytics', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        analyticsinstance = self.get_object()
        if self.request.user == analyticsinstance.user:
            return True
        return False


class AnalyticsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Analytics
    success_url = "/console/"

    def test_func(self):
        analyticsinstance = self.get_object()
        if self.request.user == analyticsinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class BTListView(ListView):
    model = BugTracking
    template_name = 'console/bug_tracking/bt-instance.html'
    context_object_name = 'btinstance'
    ordering = ['-date_posted']


class BTGroupListView(ListView):
    model = BugTracking
    template_name = 'console/bug_tracking/btinstance-groups.html'
    context_object_name = 'btinstance'
    ordering = ['-date_posted']


class BTDetailView(DetailView):
    model = BugTracking


class BTCreateView(LoginRequiredMixin, CreateView):
    model = BugTracking
    fields = ['title', 'bug_tracking', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BTUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BugTracking
    fields = ['title', 'bug_tracking', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        btinstance = self.get_object()
        if self.request.user == btinstance.user:
            return True
        return False


class BTDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BugTracking
    success_url = "/console/"

    def test_func(self):
        btinstance = self.get_object()
        if self.request.user == btinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class VCListView(ListView):
    model = VersionControl
    template_name = 'console/version_control/vc-instance.html'
    context_object_name = 'vcinstance'
    ordering = ['-date_posted']


class VCGroupListView(ListView):
    model = VersionControl
    template_name = 'console/version_control/vcinstance-groups.html'
    context_object_name = 'vcinstance'
    ordering = ['-date_posted']


class VCDetailView(DetailView):
    model = VersionControl


class VCCreateView(LoginRequiredMixin, CreateView):
    model = VersionControl
    fields = ['title', 'version_control', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VCUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VersionControl
    fields = ['title', 'version_control', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        vcinstance = self.get_object()
        if self.request.user == vcinstance.user:
            return True
        return False


class VCDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VersionControl
    success_url = "/console/"

    def test_func(self):
        vcinstance = self.get_object()
        if self.request.user == vcinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class EListView(ListView):
    model = EmailService
    template_name = 'console/email_service/e-instance.html'
    context_object_name = 'einstance'
    ordering = ['-date_posted']


class EGroupListView(ListView):
    model = EmailService
    template_name = 'console/email_service/einstance-groups.html'
    context_object_name = 'einstance'
    ordering = ['-date_posted']


class EDetailView(DetailView):
    model = EmailService


class ECreateView(LoginRequiredMixin, CreateView):
    model = EmailService
    fields = ['title', 'email_service', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EmailService
    fields = ['title', 'email_service', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        einstance = self.get_object()
        if self.request.user == einstance.user:
            return True
        return False


class EDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EmailService
    success_url = "/console/"

    def test_func(self):
        einstance = self.get_object()
        if self.request.user == einstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class FListView(ListView):
    model = Forum
    template_name = 'console/forum/f-instance.html'
    context_object_name = 'finstance'
    ordering = ['-date_posted']


class FGroupListView(ListView):
    model = Forum
    template_name = 'console/forum/finstance-groups.html'
    context_object_name = 'finstance'
    ordering = ['-date_posted']


class FDetailView(DetailView):
    model = Forum


class FCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    fields = ['title', 'forum', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Forum
    fields = ['title', 'forum', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        finstance = self.get_object()
        if self.request.user == finstance.user:
            return True
        return False


class FDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Forum
    success_url = "/console/"

    def test_func(self):
        finstance = self.get_object()
        if self.request.user == finstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class CRListView(ListView):
    model = CodeReview
    template_name = 'console/code_review/cr-instance.html'
    context_object_name = 'crinstance'
    ordering = ['-date_posted']


class CRGroupListView(ListView):
    model = CodeReview
    template_name = 'console/code_review/crinstance-groups.html'
    context_object_name = 'crinstance'
    ordering = ['-date_posted']


class CRDetailView(DetailView):
    model = CodeReview


class CRCreateView(LoginRequiredMixin, CreateView):
    model = CodeReview
    fields = ['title', 'code_review', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CRUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CodeReview
    fields = ['title', 'code_review', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        crinstance = self.get_object()
        if self.request.user == crinstance.user:
            return True
        return False


class CRDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CodeReview
    success_url = "/console/"

    def test_func(self):
        crinstance = self.get_object()
        if self.request.user == crinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class BRListView(ListView):
    model = BinaryRepository
    template_name = 'console/binary_repository/br-instance.html'
    context_object_name = 'brinstance'
    ordering = ['-date_posted']


class BRGroupListView(ListView):
    model = BinaryRepository
    template_name = 'console/binary_repository/brinstance-groups.html'
    context_object_name = 'brinstance'
    ordering = ['-date_posted']


class BRDetailView(DetailView):
    model = BinaryRepository


class BRCreateView(LoginRequiredMixin, CreateView):
    model = BinaryRepository
    fields = ['title', 'binary_repository', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BRUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BinaryRepository
    fields = ['title', 'binary_repository', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        brinstance = self.get_object()
        if self.request.user == brinstance.user:
            return True
        return False


class BRDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BinaryRepository
    success_url = "/console/"

    def test_func(self):
        brinstance = self.get_object()
        if self.request.user == brinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class HRMListView(ListView):
    model = HumanResourceManagement
    template_name = 'console/human_resource_management/hrm-instance.html'
    context_object_name = 'hrminstance'
    ordering = ['-date_posted']


class HRMGroupListView(ListView):
    model = HumanResourceManagement
    template_name = 'console/human_resource_management/hrminstance-groups.html'
    context_object_name = 'hrminstance'
    ordering = ['-date_posted']


class HRMDetailView(DetailView):
    model = HumanResourceManagement


class HRMCreateView(LoginRequiredMixin, CreateView):
    model = HumanResourceManagement
    fields = ['title', 'human_resource_management', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HRMUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HumanResourceManagement
    fields = ['title', 'human_resource_management', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        hrminstance = self.get_object()
        if self.request.user == hrminstance.user:
            return True
        return False


class HRMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HumanResourceManagement
    success_url = "/console/"

    def test_func(self):
        hrminstance = self.get_object()
        if self.request.user == hrminstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class MSListView(ListView):
    model = MediaSharing
    template_name = 'console/media_sharing/ms-instance.html'
    context_object_name = 'msinstance'
    ordering = ['-date_posted']


class MSGroupListView(ListView):
    model = MediaSharing
    template_name = 'console/media_sharing/msinstance-groups.html'
    context_object_name = 'msinstance'
    ordering = ['-date_posted']


class MSDetailView(DetailView):
    model = MediaSharing


class MSCreateView(LoginRequiredMixin, CreateView):
    model = MediaSharing
    fields = ['title', 'media_sharing', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MSUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MediaSharing
    fields = ['title', 'media_sharing', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        msinstance = self.get_object()
        if self.request.user == msinstance.user:
            return True
        return False


class MSDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MediaSharing
    success_url = "/console/"

    def test_func(self):
        msinstance = self.get_object()
        if self.request.user == msinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class SListView(ListView):
    model = Search
    template_name = 'console/search_service/s-instance.html'
    context_object_name = 'sinstance'
    ordering = ['-date_posted']


class SGroupListView(ListView):
    model = Search
    template_name = 'console/search_service/sinstance-groups.html'
    context_object_name = 'sinstance'
    ordering = ['-date_posted']


class SDetailView(DetailView):
    model = Search


class SCreateView(LoginRequiredMixin, CreateView):
    model = Search
    fields = ['title', 'search_service', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Search
    fields = ['title', 'search_service', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        sinstance = self.get_object()
        if self.request.user == sinstance.user:
            return True
        return False


class SDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Search
    success_url = "/console/"

    def test_func(self):
        sinstance = self.get_object()
        if self.request.user == sinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class PSListView(ListView):
    model = PhotoSharing
    template_name = 'console/photo_sharing/ps-instance.html'
    context_object_name = 'psinstance'
    ordering = ['-date_posted']


class PSGroupListView(ListView):
    model = PhotoSharing
    template_name = 'console/photo_sharing/psinstance-groups.html'
    context_object_name = 'psinstance'
    ordering = ['-date_posted']


class PSDetailView(DetailView):
    model = PhotoSharing


class PSCreateView(LoginRequiredMixin, CreateView):
    model = PhotoSharing
    fields = ['title', 'photo_sharing', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PSUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PhotoSharing
    fields = ['title', 'photo_sharing', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        psinstance = self.get_object()
        if self.request.user == psinstance.user:
            return True
        return False


class PSDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PhotoSharing
    success_url = "/console/"

    def test_func(self):
        psinstance = self.get_object()
        if self.request.user == psinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class CListView(ListView):
    model = Collaboration
    template_name = 'console/collaboration/c-instance.html'
    context_object_name = 'cinstance'
    ordering = ['-date_posted']


class CGroupListView(ListView):
    model = Collaboration
    template_name = 'console/collaboration/cinstance-groups.html'
    context_object_name = 'cinstance'
    ordering = ['-date_posted']


class CDetailView(DetailView):
    model = Collaboration


class CCreateView(LoginRequiredMixin, CreateView):
    model = Collaboration
    fields = ['title', 'collaboration', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Collaboration
    fields = ['title', 'collaboration', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cinstance = self.get_object()
        if self.request.user == cinstance.user:
            return True
        return False


class CDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Collaboration
    success_url = "/console/"

    def test_func(self):
        cinstance = self.get_object()
        if self.request.user == cinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class MAListView(ListView):
    model = MarketingAutomation
    template_name = 'console/marketing_automation/ma-instance.html'
    context_object_name = 'mainstance'
    ordering = ['-date_posted']


class MAGroupListView(ListView):
    model = MarketingAutomation
    template_name = 'console/marketing_automation/mainstance-groups.html'
    context_object_name = 'mainstance'
    ordering = ['-date_posted']


class MADetailView(DetailView):
    model = MarketingAutomation


class MACreateView(LoginRequiredMixin, CreateView):
    model = MarketingAutomation
    fields = ['title', 'marketing_automation', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MAUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MarketingAutomation
    fields = ['title', 'omarketing_automations', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        mainstance = self.get_object()
        if self.request.user == mainstance.user:
            return True
        return False


class MADeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MarketingAutomation
    success_url = "/console/"

    def test_func(self):
        mainstance = self.get_object()
        if self.request.user == mainstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class PMListView(ListView):
    model = PollManagement
    template_name = 'console/poll_management/pm-instance.html'
    context_object_name = 'pminstance'
    ordering = ['-date_posted']


class PMGroupListView(ListView):
    model = PollManagement
    template_name = 'console/poll_management/pminstance-groups.html'
    context_object_name = 'pminstance'
    ordering = ['-date_posted']


class PMDetailView(DetailView):
    model = PollManagement


class PMCreateView(LoginRequiredMixin, CreateView):
    model = PollManagement
    fields = ['title', 'poll_management', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PMUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PollManagement
    fields = ['title', 'poll_management', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pminstance = self.get_object()
        if self.request.user == pminstance.user:
            return True
        return False


class PMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PollManagement
    success_url = "/console/"

    def test_func(self):
        pminstance = self.get_object()
        if self.request.user == pminstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class PortsListView(ListView):
    model = PortalServer
    template_name = 'console/portal_server/ports-instance.html'
    context_object_name = 'portsinstance'
    ordering = ['-date_posted']


class PortsGroupListView(ListView):
    model = PortalServer
    template_name = 'console/portal_server/portsinstance-groups.html'
    context_object_name = 'portsinstance'
    ordering = ['-date_posted']


class PortsDetailView(DetailView):
    model = PortalServer


class PortsCreateView(LoginRequiredMixin, CreateView):
    model = PortalServer
    fields = ['title', 'portal_server', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PortalServer
    fields = ['title', 'portal_server', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        portsinstance = self.get_object()
        if self.request.user == portsinstance.user:
            return True
        return False


class PortsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PortalServer
    success_url = "/console/"

    def test_func(self):
        portsinstance = self.get_object()
        if self.request.user == portsinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class ELListView(ListView):
    model = ELearning
    template_name = 'console/e_learning/el-instance.html'
    context_object_name = 'elinstance'
    ordering = ['-date_posted']


class ELGroupListView(ListView):
    model = ELearning
    template_name = 'console/e_learning/elinstance-groups.html'
    context_object_name = 'elinstance'
    ordering = ['-date_posted']


class ELDetailView(DetailView):
    model = ELearning


class ELCreateView(LoginRequiredMixin, CreateView):
    model = ELearning
    fields = ['title', 'e_learning', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ELUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ELearning
    fields = ['title', 'e_learning', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        elinstance = self.get_object()
        if self.request.user == elinstance.user:
            return True
        return False


class ELDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ELearning
    success_url = "/console/"

    def test_func(self):
        elinstance = self.get_object()
        if self.request.user == elinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class WListView(ListView):
    model = Wiki
    template_name = 'console/wiki/w-instance.html'
    context_object_name = 'winstance'
    ordering = ['-date_posted']


class WGroupListView(ListView):
    model = Wiki
    template_name = 'console/wiki/winstance-groups.html'
    context_object_name = 'winstance'
    ordering = ['-date_posted']


class WDetailView(DetailView):
    model = Wiki


class WCreateView(LoginRequiredMixin, CreateView):
    model = Wiki
    fields = ['title', 'wiki', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wiki
    fields = ['title', 'wiki', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        winstance = self.get_object()
        if self.request.user == winstance.user:
            return True
        return False


class WDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wiki
    success_url = "/console/"

    def test_func(self):
        winstance = self.get_object()
        if self.request.user == winstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class TTListView(ListView):
    model = TranslationTools
    template_name = 'console/translation_tools/tt-instance.html'
    context_object_name = 'ttinstance'
    ordering = ['-date_posted']


class TTGroupListView(ListView):
    model = TranslationTools
    template_name = 'console/translation_tools/ttinstance-groups.html'
    context_object_name = 'ttinstance'
    ordering = ['-date_posted']


class TTDetailView(DetailView):
    model = TranslationTools


class TTCreateView(LoginRequiredMixin, CreateView):
    model = TranslationTools
    fields = ['title', 'translation_tools', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TTUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TranslationTools
    fields = ['title', 'translation_tools', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ttinstance = self.get_object()
        if self.request.user == ttinstance.user:
            return True
        return False


class TTDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TranslationTools
    success_url = "/console/"

    def test_func(self):
        ttinstance = self.get_object()
        if self.request.user == ttinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class RDListView(ListView):
    model = RemoteDesktop
    template_name = 'console/remote_desktop/rd-instance.html'
    context_object_name = 'rdinstance'
    ordering = ['-date_posted']


class RDGroupListView(ListView):
    model = RemoteDesktop
    template_name = 'console/remote_desktop/rdinstance-groups.html'
    context_object_name = 'rdinstance'
    ordering = ['-date_posted']


class RDDetailView(DetailView):
    model = RemoteDesktop


class RDCreateView(LoginRequiredMixin, CreateView):
    model = RemoteDesktop
    fields = ['title', 'remote_desktop', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RDUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RemoteDesktop
    fields = ['title', 'remote_desktop', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        rdinstance = self.get_object()
        if self.request.user == rdinstance.user:
            return True
        return False


class RDDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = RemoteDesktop
    success_url = "/console/"

    def test_func(self):
        rdinstance = self.get_object()
        if self.request.user == rdinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class TListView(ListView):
    model = Testing
    template_name = 'console/testing/t-instance.html'
    context_object_name = 'tinstance'
    ordering = ['-date_posted']


class TGroupListView(ListView):
    model = Testing
    template_name = 'console/testing/tinstance-groups.html'
    context_object_name = 'tinstance'
    ordering = ['-date_posted']


class TDetailView(DetailView):
    model = Testing


class TCreateView(LoginRequiredMixin, CreateView):
    model = Testing
    fields = ['title', 'testing', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Testing
    fields = ['title', 'testing', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        tinstance = self.get_object()
        if self.request.user == tinstance.user:
            return True
        return False


class TDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Testing
    success_url = "/console/"

    def test_func(self):
        tinstance = self.get_object()
        if self.request.user == tinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class OCListView(ListView):
    model = OnlineClassifieds
    template_name = 'console/online_classifieds/oc-instance.html'
    context_object_name = 'ocinstance'
    ordering = ['-date_posted']


class OCGroupListView(ListView):
    model = OnlineClassifieds
    template_name = 'console/online_classifieds/ocinstance-groups.html'
    context_object_name = 'ocinstance'
    ordering = ['-date_posted']


class OCDetailView(DetailView):
    model = OnlineClassifieds


class OCCreateView(LoginRequiredMixin, CreateView):
    model = OnlineClassifieds
    fields = ['title', 'online_classifieds', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OCUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OnlineClassifieds
    fields = ['title', 'online_classifieds', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ocinstance = self.get_object()
        if self.request.user == ocinstance.user:
            return True
        return False


class OCDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = OnlineClassifieds
    success_url = "/console/"

    def test_func(self):
        ocinstance = self.get_object()
        if self.request.user == ocinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class SNListView(ListView):
    model = SocialNetworking
    template_name = 'console/social_networking/sn-instance.html'
    context_object_name = 'sninstance'
    ordering = ['-date_posted']


class SNGroupListView(ListView):
    model = SocialNetworking
    template_name = 'console/social_networking/sninstance-groups.html'
    context_object_name = 'sninstance'
    ordering = ['-date_posted']


class SNDetailView(DetailView):
    model = SocialNetworking


class SNCreateView(LoginRequiredMixin, CreateView):
    model = SocialNetworking
    fields = ['title', 'social_networking', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SNUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SocialNetworking
    fields = ['title', 'social_networking', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        sninstance = self.get_object()
        if self.request.user == sninstance.user:
            return True
        return False


class SNDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SocialNetworking
    success_url = "/console/"

    def test_func(self):
        sninstance = self.get_object()
        if self.request.user == sninstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class CIListView(ListView):
    model = ContinuousIntegration
    template_name = 'console/continuous_integration/ci-instance.html'
    context_object_name = 'ciinstance'
    ordering = ['-date_posted']


class CIGroupListView(ListView):
    model = ContinuousIntegration
    template_name = 'console/continuous_integration/ciinstance-groups.html'
    context_object_name = 'ciinstance'
    ordering = ['-date_posted']


class CIDetailView(DetailView):
    model = ContinuousIntegration


class CICreateView(LoginRequiredMixin, CreateView):
    model = ContinuousIntegration
    fields = ['title', 'continuous_integration', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CIUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ContinuousIntegration
    fields = ['title', 'continuous_integration', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ciinstance = self.get_object()
        if self.request.user == ciinstance.user:
            return True
        return False


class CIDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ContinuousIntegration
    success_url = "/console/"

    def test_func(self):
        ciinstance = self.get_object()
        if self.request.user == ciinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class PromListView(ListView):
    model = ProjectManagement
    template_name = 'console/project_management/prom-instance.html'
    context_object_name = 'prominstance'
    ordering = ['-date_posted']


class PromGroupListView(ListView):
    model = ProjectManagement
    template_name = 'console/project_management/prominstance-groups.html'
    context_object_name = 'prominstance'
    ordering = ['-date_posted']


class PromDetailView(DetailView):
    model = ProjectManagement


class PromCreateView(LoginRequiredMixin, CreateView):
    model = ProjectManagement
    fields = ['title', 'project_management', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PromUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProjectManagement
    fields = ['title', 'project_management', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        prominstance = self.get_object()
        if self.request.user == prominstance.user:
            return True
        return False


class PromDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProjectManagement
    success_url = "/console/"

    def test_func(self):
        prominstance = self.get_object()
        if self.request.user == prominstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class NAListView(ListView):
    model = NewsAggregator
    template_name = 'console/news_aggregator/na-instance.html'
    context_object_name = 'nainstance'
    ordering = ['-date_posted']


class NAGroupListView(ListView):
    model = NewsAggregator
    template_name = 'console/news_aggregator/nainstance-groups.html'
    context_object_name = 'nainstance'
    ordering = ['-date_posted']


class NADetailView(DetailView):
    model = NewsAggregator


class NACreateView(LoginRequiredMixin, CreateView):
    model = NewsAggregator
    fields = ['title', 'news_aggregator', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NAUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsAggregator
    fields = ['title', 'news_aggregator', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        nainstance = self.get_object()
        if self.request.user == nainstance.user:
            return True
        return False


class NADeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsAggregator
    success_url = "/console/"

    def test_func(self):
        nainstance = self.get_object()
        if self.request.user == nainstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class AccListView(ListView):
    model = Accounting
    template_name = 'console/accounting/acc-instance.html'
    context_object_name = 'accinstance'
    ordering = ['-date_posted']


class AccGroupListView(ListView):
    model = Accounting
    template_name = 'console/accounting/accinstance-groups.html'
    context_object_name = 'accinstance'
    ordering = ['-date_posted']


class AccDetailView(DetailView):
    model = Accounting


class AccCreateView(LoginRequiredMixin, CreateView):
    model = Accounting
    fields = ['title', 'accounting', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Accounting
    fields = ['title', 'accounting', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        accinstance = self.get_object()
        if self.request.user == accinstance.user:
            return True
        return False


class AccDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Accounting
    success_url = "/console/"

    def test_func(self):
        accinstance = self.get_object()
        if self.request.user == accinstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class NMListView(ListView):
    model = NewsletterManager
    template_name = 'console/newsletter_manager/nm-instance.html'
    context_object_name = 'nminstance'
    ordering = ['-date_posted']


class NMGroupListView(ListView):
    model = NewsletterManager
    template_name = 'console/newsletter_manager/nminstance-groups.html'
    context_object_name = 'nminstance'
    ordering = ['-date_posted']


class NMDetailView(DetailView):
    model = NewsletterManager


class NMCreateView(LoginRequiredMixin, CreateView):
    model = NewsletterManager
    fields = ['title', 'newsletter_manager', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NMUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsletterManager
    fields = ['title', 'newsletter_manager', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        nminstance = self.get_object()
        if self.request.user == nminstance.user:
            return True
        return False


class NMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsletterManager
    success_url = "/console/"

    def test_func(self):
        nminstance = self.get_object()
        if self.request.user == nminstance.user:
            return True
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------


class ERPListView(ListView):
    model = ERP
    template_name = 'console/erp/erp-instance.html'
    context_object_name = 'erpinstance'
    ordering = ['-date_posted']


class ERPGroupListView(ListView):
    model = ERP
    template_name = 'console/erp/erpinstance-groups.html'
    context_object_name = 'erpinstance'
    ordering = ['-date_posted']


class ERPDetailView(DetailView):
    model = ERP


class ERPCreateView(LoginRequiredMixin, CreateView):
    model = ERP
    fields = ['title', 'erp', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ERPUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ERP
    fields = ['title', 'erp', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        erpinstance = self.get_object()
        if self.request.user == erpinstance.user:
            return True
        return False


class ERPDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ERP
    success_url = "/console/"

    def test_func(self):
        erpinstance = self.get_object()
        if self.request.user == erpinstance.user:
            return True
        return False

# ------------------------------------------------------------------------------------------------------------------------------------------------


class BPMListView(ListView):
    model = BPM
    template_name = 'console/bpm/bpm-instance.html'
    context_object_name = 'bpminstance'
    ordering = ['-date_posted']


class BPMGroupListView(ListView):
    model = BPM
    template_name = 'console/bpm/bpminstance-groups.html'
    context_object_name = 'bpminstance'
    ordering = ['-date_posted']


class BPMDetailView(DetailView):
    model = BPM


class BPMCreateView(LoginRequiredMixin, CreateView):
    model = BPM
    fields = ['title', 'bpm', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BPMUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BPM
    fields = ['title', 'bpm', 'ram',
              'storage', 'cpu', 'system_group']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        bpminstance = self.get_object()
        if self.request.user == bpminstance.user:
            return True
        return False


class BPMDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BPM
    success_url = "/console/"

    def test_func(self):
        bpminstance = self.get_object()
        if self.request.user == bpminstance.user:
            return True
        return False
