from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .models import MachineImages
# Create your views here.


class ConsoleDashboardView(TemplateView):
    template_name = 'console/console.html'


class CEInstanceGroupsView(TemplateView):
    template_name = 'console/compute-engine/ceinstance-groups.html'


class AEInstanceGroupsView(TemplateView):
    template_name = 'console/app-engine/aeinstance-groups.html'


class DBInstanceGroupsView(TemplateView):
    template_name = 'console/database/dbinstance-groups.html'


class ISInstanceGroupsView(TemplateView):
    template_name = 'console/infastructure/isinstance-groups.html'


class CMSInstanceGroupsView(TemplateView):
    template_name = 'console/cms/cmsinstance-groups.html'


class DTInstanceGroupsView(TemplateView):
    template_name = 'console/developer_tools/dtinstance-groups.html'


class ECInstanceGroupsView(TemplateView):
    template_name = 'console/e_commerce/ecinstance-groups.html'


class CRMInstanceGroupsView(TemplateView):
    template_name = 'console/crm/crminstance-groups.html'


class BIInstanceGroupsView(TemplateView):
    template_name = 'console/business_intelligence/biinstance-groups.html'


class ChatInstanceGroupsView(TemplateView):
    template_name = 'console/chat/chatinstance-groups.html'


class AnalyticsInstanceGroupsView(TemplateView):
    template_name = 'console/analytics/analyticsinstance-groups.html'


class BTInstanceGroupsView(TemplateView):
    template_name = 'console/bug_tracking/btinstance-groups.html'


class VCInstanceGroupsView(TemplateView):
    template_name = 'console/version_control/vcinstance-groups.html'


class EInstanceGroupsView(TemplateView):
    template_name = 'console/email_service/einstance-groups.html'


class FInstanceGroupsView(TemplateView):
    template_name = 'console/forum/finstance-groups.html'


class CRInstanceGroupsView(TemplateView):
    template_name = 'console/code_review/crinstance-groups.html'


class BRInstanceGroupsView(TemplateView):
    template_name = 'console/binaryrepository/brinstance-groups.html'


class HRMInstanceGroupsView(TemplateView):
    template_name = 'console/human_resource_management/hrminstance-groups.html'


class MSInstanceGroupsView(TemplateView):
    template_name = 'console/media_sharing/msinstance-groups.html'


class SInstanceGroupsView(TemplateView):
    template_name = 'console/search/sinstance-groups.html'


class PSInstanceGroupsView(TemplateView):
    template_name = 'console/photo_sharing/psinstance-groups.html'


class CInstanceGroupsView(TemplateView):
    template_name = 'console/collaboration/cinstance-groups.html'


class MAInstanceGroupsView(TemplateView):
    template_name = 'console/marketing_automation/mainstance-groups.html'


class PMInstanceGroupsView(TemplateView):
    template_name = 'console/poll_management/pminstance-groups.html'


class PortsInstanceGroupsView(TemplateView):
    template_name = 'console/portal_server/portsinstance-groups.html'


class ELInstanceGroupsView(TemplateView):
    template_name = 'console/e_learning/elinstance-groups.html'


class WInstanceGroupsView(TemplateView):
    template_name = 'console/wiki/winstance-groups.html'


class TTInstanceGroupsView(TemplateView):
    template_name = 'console/translation_tools/ttinstance-groups.html'


class RDInstanceGroupsView(TemplateView):
    template_name = 'console/remote_desktop/rdinstance-groups.html'


class TInstanceGroupsView(TemplateView):
    template_name = 'console/testing/tinstance-groups.html'


class OCInstanceGroupsView(TemplateView):
    template_name = 'console/online_classifieds/ocinstance-groups.html'


class SNInstanceGroupsView(TemplateView):
    template_name = 'console/social_networking/sninstance-groups.html'


class CIInstanceGroupsView(TemplateView):
    template_name = 'console/continuous_integration/ciinstance-groups.html'


class PromInstanceGroupsView(TemplateView):
    template_name = 'console/project_management/prominstance-groups.html'


class NAInstanceGroupsView(TemplateView):
    template_name = 'console/news_aggregator/nainstance-groups.html'


class AccInstanceGroupsView(TemplateView):
    template_name = 'console/accounting/accinstance-groups.html'


class NMInstanceGroupsView(TemplateView):
    template_name = 'console/newsletter_manager/nminstance-groups.html'


class ERPInstanceGroupsView(TemplateView):
    template_name = 'console/erp/erpinstance-groups.html'


class BPMInstanceGroupsView(TemplateView):
    template_name = 'console/bpm/bpminstance-groups.html'


class SupportOverviewView(TemplateView):
    template_name = 'console/support/support-overview.html'


class ChatSupportView(TemplateView):
    template_name = 'console/support/chat-support.html'


class GettingStartedView(TemplateView):
    template_name = 'console/getting-started.html'


class DocumentationView(TemplateView):
    template_name = 'console/documentation.html'


class AboutConsoleView(TemplateView):
    template_name = 'console/about-console.html'


class PhoneSupportView(TemplateView):
    template_name = 'console/support/phone-support.html'


def machine_image_view(request):
    context = {
        'images': MachineImages.objects.all()
    }

    return render(request, 'console/machine-images.html', context)
