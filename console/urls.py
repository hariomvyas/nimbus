from django.urls import path
from users.views import profile, ProfilePageView
from services.views import *
from . views import *


urlpatterns = [
    path('', ConsoleDashboardView.as_view(), name='console'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('settings/', profile, name='settings'),
    # ------------------------------------------------------------------------------------------------------------
    path('compute-engine/vm-instances/',
         CEListView.as_view(), name='ceinstance'),
    path('compute-engine/vm-instances/new/',
         CECreateView.as_view(), name='ceinstance-create'),
    path('compute-engine/vm-instances/<int:pk>/update/', CEUpdateView.as_view(),
         name='ceinstance-update'),
    path('compute-engine/vm-instances/<int:pk>/delete/',
         CEDeleteView.as_view(), name='ceinstance-delete'),
    path('compute-engine/vm-instances/<int:pk>/',
         CEDetailView.as_view(), name='ceinstance-detail'),
    path('compute-engine/instance-groups/',
         CEGroupListView.as_view(), name='ceinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('app-engine/vm-instances/',
         AEListView.as_view(), name='aeinstance'),
    path('app-engine/vm-instances/new/',
         AECreateView.as_view(), name='aeinstance-create'),
    path('app-engine/vm-instances/<int:pk>/update/', AEUpdateView.as_view(),
         name='aeinstance-update'),
    path('app-engine/vm-instances/<int:pk>/delete/',
         AEDeleteView.as_view(), name='aeinstance-delete'),
    path('app-engine/vm-instances/<int:pk>/',
         AEDetailView.as_view(), name='aeinstance-detail'),
    path('app-engine/instance-groups/',
         AEGroupListView.as_view(), name='aeinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------

    path('database/databases/',
         DBListView.as_view(), name='dbinstance'),
    path('database/databases/new/',
         DBCreateView.as_view(), name='dbinstance-create'),
    path('database/databases/<int:pk>/update/', DBUpdateView.as_view(),
         name='dbinstance-update'),
    path('database/databases/<int:pk>/delete/',
         DBDeleteView.as_view(), name='dbinstance-delete'),
    path('database/databases/<int:pk>/',
         DBDetailView.as_view(), name='dbinstance-detail'),
    path('database/database-groups/',
         DBGroupListView.as_view(), name='dbinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------

    path('infastructure/infastructures/',
         ISListView.as_view(), name='isinstance'),
    path('infastructure/infastructures/new/',
         ISCreateView.as_view(), name='isinstance-create'),
    path('infastructure/infastructures/<int:pk>/update/', ISUpdateView.as_view(),
         name='isinstance-update'),
    path('infastructure/infastructures/<int:pk>/delete/',
         ISDeleteView.as_view(), name='isinstance-delete'),
    path('infastructure/infastructures/<int:pk>/',
         ISDetailView.as_view(), name='isinstance-detail'),
    path('infastructure/infastructure-groups/',
         ISGroupListView.as_view(), name='isinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('cms/cms/',
         CMSListView.as_view(), name='cmsinstance'),
    path('cms/cms/new/',
         CMSCreateView.as_view(), name='cmsinstance-create'),
    path('cms/cms/<int:pk>/update/', CMSUpdateView.as_view(),
         name='cmsinstance-update'),
    path('cms/cms/<int:pk>/delete/',
         CMSDeleteView.as_view(), name='cmsinstance-delete'),
    path('cms/cms/<int:pk>/',
         CMSDetailView.as_view(), name='cmsinstance-detail'),
    path('cms/cms-groups/',
         CMSGroupListView.as_view(), name='cmsinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('developer-tools/developer-tools/',
         DTListView.as_view(), name='dtinstance'),
    path('developer-tools/developer-tools/new/',
         DTCreateView.as_view(), name='dtinstance-create'),
    path('developer-tools/developer-tools/<int:pk>/update/', DTUpdateView.as_view(),
         name='dtinstance-update'),
    path('developer-tools/developer-tools/<int:pk>/delete/',
         DTDeleteView.as_view(), name='dtinstance-delete'),
    path('developer-tools/developer-tools/<int:pk>/',
         DTDetailView.as_view(), name='dtinstance-detail'),
    path('developer-tools/developer-tools-groups/',
         DTGroupListView.as_view(), name='dtinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('e-commerce/e-commerces/',
         ECListView.as_view(), name='ecinstance'),
    path('e-commerce/e-commerces/new/',
         ECCreateView.as_view(), name='ecinstance-create'),
    path('e-commerce/e-commerces/<int:pk>/update/', ECUpdateView.as_view(),
         name='ecinstance-update'),
    path('e-commerce/e-commerces/<int:pk>/delete/',
         ECDeleteView.as_view(), name='ecinstance-delete'),
    path('e-commerce/e-commerces/<int:pk>/',
         ECDetailView.as_view(), name='ecinstance-detail'),
    path('e-commerce/e-commerce-groups/',
         ECGroupListView.as_view(), name='ecinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('crm/crms/',
         CRMListView.as_view(), name='crminstance'),
    path('crm/crms/new/',
         CRMCreateView.as_view(), name='crminstance-create'),
    path('crm/crms/<int:pk>/update/', CRMUpdateView.as_view(),
         name='crminstance-update'),
    path('crm/crms/<int:pk>/delete/',
         CRMDeleteView.as_view(), name='crminstance-delete'),
    path('crm/crms/<int:pk>/',
         CRMDetailView.as_view(), name='crminstance-detail'),
    path('crm/crm-groups/',
         CRMGroupListView.as_view(), name='crminstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('business-intelligence/business-intelligences/',
         BIListView.as_view(), name='biinstance'),
    path('business-intelligence/business-intelligences/new/',
         BICreateView.as_view(), name='biinstance-create'),
    path('business-intelligence/business-intelligences/<int:pk>/update/', BIUpdateView.as_view(),
         name='biinstance-update'),
    path('business-intelligence/business-intelligences/<int:pk>/delete/',
         BIDeleteView.as_view(), name='biinstance-delete'),
    path('business-intelligence/business-intelligences/<int:pk>/',
         BIDetailView.as_view(), name='biinstance-detail'),
    path('business-intelligence/business-intelligence-groups/',
         BIGroupListView.as_view(), name='biinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('chat/chats/',
         ChatListView.as_view(), name='chatinstance'),
    path('chat/chats/new/',
         ChatCreateView.as_view(), name='chatinstance-create'),
    path('chat/chats/<int:pk>/update/', ChatUpdateView.as_view(),
         name='chatinstance-update'),
    path('chat/chats/<int:pk>/delete/',
         ChatDeleteView.as_view(), name='chatinstance-delete'),
    path('chat/chats/<int:pk>/',
         ChatDetailView.as_view(), name='chatinstance-detail'),
    path('chat/chat-groups/',
         ChatGroupListView.as_view(), name='chatinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('analytics/analytics/',
         AnalyticsListView.as_view(), name='analyticsinstance'),
    path('analytics/analytics/new/',
         AnalyticsCreateView.as_view(), name='analyticsinstance-create'),
    path('analytics/analytics/<int:pk>/update/', AnalyticsUpdateView.as_view(),
         name='analyticsinstance-update'),
    path('analytics/analytics/<int:pk>/delete/',
         AnalyticsDeleteView.as_view(), name='analyticsinstance-delete'),
    path('analytics/analytics/<int:pk>/',
         AnalyticsDetailView.as_view(), name='analyticsinstance-detail'),
    path('analytics/analytics-groups/',
         AnalyticsGroupListView.as_view(), name='analyticsinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('bug-tracking/bug-trackings/',
         BTListView.as_view(), name='btinstance'),
    path('bug-tracking/bug-trackings/new/',
         BTCreateView.as_view(), name='btinstance-create'),
    path('bug-tracking/bug-trackings/<int:pk>/update/', BTUpdateView.as_view(),
         name='btinstance-update'),
    path('bug-tracking/bug-trackings/<int:pk>/delete/',
         BTDeleteView.as_view(), name='btinstance-delete'),
    path('bug-tracking/bug-trackings/<int:pk>/',
         BTDetailView.as_view(), name='btinstance-detail'),
    path('bug-tracking/bug-tracking-groups/',
         BTGroupListView.as_view(), name='btinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('version-control/version-controls/',
         VCListView.as_view(), name='vcinstance'),
    path('version-control/version-controls/new/',
         VCCreateView.as_view(), name='vcinstance-create'),
    path('version-control/version-controls/<int:pk>/update/', VCUpdateView.as_view(),
         name='vcinstance-update'),
    path('version-control/version-controls/<int:pk>/delete/',
         VCDeleteView.as_view(), name='vcinstance-delete'),
    path('version-control/version-controls/<int:pk>/',
         VCDetailView.as_view(), name='vcinstance-detail'),
    path('version-control/version-control-groups/',
         VCGroupListView.as_view(), name='vcinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('email-service/email-services/',
         EListView.as_view(), name='einstance'),
    path('email-service/email-services/new/',
         ECreateView.as_view(), name='einstance-create'),
    path('email-service/email-services/<int:pk>/update/', EUpdateView.as_view(),
         name='einstance-update'),
    path('email-service/email-services/<int:pk>/delete/',
         EDeleteView.as_view(), name='einstance-delete'),
    path('email-service/email-services/<int:pk>/',
         EDetailView.as_view(), name='einstance-detail'),
    path('email-service/email-service-groups/',
         EGroupListView.as_view(), name='einstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('forum/forums/',
         FListView.as_view(), name='finstance'),
    path('forum/forums/new/',
         FCreateView.as_view(), name='finstance-create'),
    path('forum/forums/<int:pk>/update/', FUpdateView.as_view(),
         name='finstance-update'),
    path('forum/forums/<int:pk>/delete/',
         FDeleteView.as_view(), name='finstance-delete'),
    path('forum/forums/<int:pk>/',
         FDetailView.as_view(), name='finstance-detail'),
    path('forum/forums-groups/',
         FGroupListView.as_view(), name='finstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('code-review/code-reviews/',
         CRListView.as_view(), name='crinstance'),
    path('code-review/code-reviews/new/',
         CRCreateView.as_view(), name='crinstance-create'),
    path('code-review/code-reviews/<int:pk>/update/', CRUpdateView.as_view(),
         name='crinstance-update'),
    path('code-review/code-reviews/<int:pk>/delete/',
         CRDeleteView.as_view(), name='crinstance-delete'),
    path('code-review/code-reviews/<int:pk>/',
         CRDetailView.as_view(), name='crinstance-detail'),
    path('code-review/code-review-groups/',
         CRGroupListView.as_view(), name='crinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('binary-repisotory/binary-repisotories/',
         BRListView.as_view(), name='brinstance'),
    path('binary-repisotory/binary-repisotories/new/',
         BRCreateView.as_view(), name='brinstance-create'),
    path('binary-repisotory/binary-repisotories/<int:pk>/update/', BRUpdateView.as_view(),
         name='brinstance-update'),
    path('binary-repisotory/binary-repisotories/<int:pk>/delete/',
         BRDeleteView.as_view(), name='brinstance-delete'),
    path('binary-repisotory/binary-repisotories/<int:pk>/',
         BRDetailView.as_view(), name='brinstance-detail'),
    path('binary-repisotory/binary-repisotory-groups/',
         BRGroupListView.as_view(), name='brinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('human-resource-management/human-resource-managements/',
         HRMListView.as_view(), name='hrminstance'),
    path('human-resource-management/human-resource-managements/new/',
         HRMCreateView.as_view(), name='hrminstance-create'),
    path('human-resource-management/human-resource-managements/<int:pk>/update/', HRMUpdateView.as_view(),
         name='hrminstance-update'),
    path('human-resource-management/human-resource-managements/<int:pk>/delete/',
         HRMDeleteView.as_view(), name='hrminstance-delete'),
    path('human-resource-management/human-resource-managements/<int:pk>/',
         HRMDetailView.as_view(), name='hrminstance-detail'),
    path('human-resource-management/human-resource-management-groups/',
         HRMGroupListView.as_view(), name='hrminstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('media-sharing/media-sharings/',
         MSListView.as_view(), name='msinstance'),
    path('media-sharing/media-sharings/new/',
         MSCreateView.as_view(), name='msinstance-create'),
    path('media-sharing/media-sharings/<int:pk>/update/', MSUpdateView.as_view(),
         name='msinstance-update'),
    path('media-sharing/media-sharings/<int:pk>/delete/',
         MSDeleteView.as_view(), name='msinstance-delete'),
    path('media-sharing/media-sharings/<int:pk>/',
         MSDetailView.as_view(), name='msinstance-detail'),
    path('media-sharing/media-sharing-groups/',
         MSGroupListView.as_view(), name='msinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('search/search/',
         SListView.as_view(), name='sinstance'),
    path('search/search/new/',
         SCreateView.as_view(), name='sinstance-create'),
    path('search/search/<int:pk>/update/', SUpdateView.as_view(),
         name='sinstance-update'),
    path('search/search/<int:pk>/delete/',
         SDeleteView.as_view(), name='sinstance-delete'),
    path('search/search/<int:pk>/',
         SDetailView.as_view(), name='sinstance-detail'),
    path('search/search-groups/',
         SGroupListView.as_view(), name='sinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('photo-sharing/photo-sharings/',
         PSListView.as_view(), name='psinstance'),
    path('photo-sharing/photo-sharings/new/',
         PSCreateView.as_view(), name='psinstance-create'),
    path('photo-sharing/photo-sharings/<int:pk>/update/', PSUpdateView.as_view(),
         name='psinstance-update'),
    path('photo-sharing/photo-sharings/<int:pk>/delete/',
         PSDeleteView.as_view(), name='psinstance-delete'),
    path('photo-sharing/photo-sharings/<int:pk>/',
         PSDetailView.as_view(), name='psinstance-detail'),
    path('photo-sharing/photo-sharing-groups/',
         PSGroupListView.as_view(), name='psinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('collaboration/collaborations/',
         CListView.as_view(), name='cinstance'),
    path('collaboration/collaborations/new/',
         CCreateView.as_view(), name='cinstance-create'),
    path('collaboration/collaborations/<int:pk>/update/', CUpdateView.as_view(),
         name='cinstance-update'),
    path('collaboration/collaborations/<int:pk>/delete/',
         CDeleteView.as_view(), name='cinstance-delete'),
    path('collaboration/collaborations/<int:pk>/',
         CDetailView.as_view(), name='cinstance-detail'),
    path('collaboration/collaboration-groups/',
         CGroupListView.as_view(), name='cinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('marketing-automation/marketing-automations/',
         MAListView.as_view(), name='mainstance'),
    path('marketing-automation/marketing-automations/new/',
         MACreateView.as_view(), name='mainstance-create'),
    path('marketing-automation/marketing-automations/<int:pk>/update/', MAUpdateView.as_view(),
         name='mainstance-update'),
    path('marketing-automation/marketing-automations/<int:pk>/delete/',
         MADeleteView.as_view(), name='mainstance-delete'),
    path('marketing-automation/marketing-automations/<int:pk>/',
         MADetailView.as_view(), name='mainstance-detail'),
    path('marketing-automation/marketing-automation-groups/',
         MAGroupListView.as_view(), name='mainstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('poll-management/poll-managements/',
         PMListView.as_view(), name='pminstance'),
    path('poll-management/poll-managements/new/',
         PMCreateView.as_view(), name='pminstance-create'),
    path('poll-management/poll-managements/<int:pk>/update/', PMUpdateView.as_view(),
         name='pminstance-update'),
    path('poll-management/poll-managements/<int:pk>/delete/',
         PMDeleteView.as_view(), name='pminstance-delete'),
    path('poll-management/poll-managements/<int:pk>/',
         PMDetailView.as_view(), name='pminstance-detail'),
    path('poll-management/poll-managements/',
         PMGroupListView.as_view(), name='pminstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('portal-server/portal-servers/',
         PortsListView.as_view(), name='portsinstance'),
    path('portal-server/portal-servers/new/',
         PortsCreateView.as_view(), name='portsinstance-create'),
    path('portal-server/portal-servers/<int:pk>/update/', PortsUpdateView.as_view(),
         name='portsinstance-update'),
    path('portal-server/portal-servers/<int:pk>/delete/',
         PortsDeleteView.as_view(), name='portsinstance-delete'),
    path('portal-server/portal-servers/<int:pk>/',
         PortsDetailView.as_view(), name='portsinstance-detail'),
    path('portal-server/portal-server-groups/',
         PortsGroupListView.as_view(), name='portsinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('e-learning/e-learnings/',
         ELListView.as_view(), name='elinstance'),
    path('e-learning/e-learnings/new/',
         ELCreateView.as_view(), name='elinstance-create'),
    path('e-learning/e-learnings/<int:pk>/update/', ELUpdateView.as_view(),
         name='elinstance-update'),
    path('e-learning/e-learnings/<int:pk>/delete/',
         ELDeleteView.as_view(), name='elinstance-delete'),
    path('e-learning/e-learnings/<int:pk>/',
         ELDetailView.as_view(), name='elinstance-detail'),
    path('e-learning/e-learning-groups/',
         ELGroupListView.as_view(), name='elinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('wiki/wikis/',
         WListView.as_view(), name='winstance'),
    path('wiki/wikis/new/',
         WCreateView.as_view(), name='winstance-create'),
    path('wiki/wikis/<int:pk>/update/', WUpdateView.as_view(),
         name='winstance-update'),
    path('wiki/wikis/<int:pk>/delete/',
         WDeleteView.as_view(), name='winstance-delete'),
    path('wiki/wikis/<int:pk>/',
         WDetailView.as_view(), name='winstance-detail'),
    path('wiki/wiki-groups/',
         WGroupListView.as_view(), name='winstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('translation-tools/translation-tools/',
         TTListView.as_view(), name='ttinstance'),
    path('translation-tools/translation-tools/new/',
         TTCreateView.as_view(), name='ttinstance-create'),
    path('translation-tools/translation-tools/<int:pk>/update/', TTUpdateView.as_view(),
         name='ttinstance-update'),
    path('translation-tools/translation-tools/<int:pk>/delete/',
         TTDeleteView.as_view(), name='ttinstance-delete'),
    path('translation-tools/translation-tools/<int:pk>/',
         TTDetailView.as_view(), name='ttinstance-detail'),
    path('translation-tools/translation-tools-groups/',
         TTGroupListView.as_view(), name='ttinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('remote-desktop/remote-desktops/',
         RDListView.as_view(), name='rdinstance'),
    path('remote-desktop/remote-desktops/new/',
         RDCreateView.as_view(), name='rdinstance-create'),
    path('remote-desktop/remote-desktops/<int:pk>/update/', RDUpdateView.as_view(),
         name='rdinstance-update'),
    path('remote-desktop/remote-desktops/<int:pk>/delete/',
         RDDeleteView.as_view(), name='rdinstance-delete'),
    path('remote-desktop/remote-desktops/<int:pk>/',
         RDDetailView.as_view(), name='rdinstance-detail'),
    path('remote-desktop/remote-desktop-groups/',
         RDGroupListView.as_view(), name='rdinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('testing/testings/',
         TListView.as_view(), name='tinstance'),
    path('testing/testings/new/',
         TCreateView.as_view(), name='tinstance-create'),
    path('testing/testings/<int:pk>/update/', TUpdateView.as_view(),
         name='tinstance-update'),
    path('testing/testings/<int:pk>/delete/',
         TDeleteView.as_view(), name='tinstance-delete'),
    path('testing/testings/<int:pk>/',
         TDetailView.as_view(), name='tinstance-detail'),
    path('testing/testing-groups/',
         TGroupListView.as_view(), name='tinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('online-classifieds/online-classifieds/',
         OCListView.as_view(), name='ocinstance'),
    path('online-classifieds/online-classifieds/new/',
         OCCreateView.as_view(), name='ocinstance-create'),
    path('online-classifieds/online-classifieds/<int:pk>/update/', OCUpdateView.as_view(),
         name='ocinstance-update'),
    path('online-classifieds/online-classifieds/<int:pk>/delete/',
         OCDeleteView.as_view(), name='ocinstance-delete'),
    path('online-classifieds/online-classifieds/<int:pk>/',
         OCDetailView.as_view(), name='ocinstance-detail'),
    path('online-classifieds/online-classifieds-groups/',
         OCGroupListView.as_view(), name='ocinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('social-networking/social-networkings/',
         SNListView.as_view(), name='sninstance'),
    path('social-networking/social-networkings/new/',
         SNCreateView.as_view(), name='sninstance-create'),
    path('social-networking/social-networkings/<int:pk>/update/', SNUpdateView.as_view(),
         name='sninstance-update'),
    path('social-networking/social-networkings/<int:pk>/delete/',
         SNDeleteView.as_view(), name='sninstance-delete'),
    path('social-networking/social-networkings/<int:pk>/',
         SNDetailView.as_view(), name='sninstance-detail'),
    path('social-networking/social-networking-groups/',
         SNGroupListView.as_view(), name='sninstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('continuous-integration/continuous-integrations/',
         CIListView.as_view(), name='ciinstance'),
    path('continuous-integration/continuous-integrations/new/',
         CICreateView.as_view(), name='ciinstance-create'),
    path('continuous-integration/continuous-integrations/<int:pk>/update/', CIUpdateView.as_view(),
         name='ciinstance-update'),
    path('continuous-integration/continuous-integrations/<int:pk>/delete/',
         CIDeleteView.as_view(), name='ciinstance-delete'),
    path('continuous-integration/continuous-integrations/<int:pk>/',
         CIDetailView.as_view(), name='ciinstance-detail'),
    path('continuous-integration/continuous-integration-groups/',
         CIGroupListView.as_view(), name='ciinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('project-management/project-managements/',
         PromListView.as_view(), name='prominstance'),
    path('project-management/project-managements/new/',
         PromCreateView.as_view(), name='prominstance-create'),
    path('project-management/project-managements/<int:pk>/update/', PromUpdateView.as_view(),
         name='prominstance-update'),
    path('project-management/project-managements/<int:pk>/delete/',
         PromDeleteView.as_view(), name='prominstance-delete'),
    path('project-management/project-managements/<int:pk>/',
         PromDetailView.as_view(), name='prominstance-detail'),
    path('project-management/project-management-groups/',
         PromGroupListView.as_view(), name='prominstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('news-aggregator/news-aggregators/',
         NAListView.as_view(), name='nainstance'),
    path('news-aggregator/news-aggregators/new/',
         NACreateView.as_view(), name='nainstance-create'),
    path('news-aggregator/news-aggregators/<int:pk>/update/', NAUpdateView.as_view(),
         name='nainstance-update'),
    path('news-aggregator/news-aggregators/<int:pk>/delete/',
         NADeleteView.as_view(), name='nainstance-delete'),
    path('news-aggregator/news-aggregators/<int:pk>/',
         NADetailView.as_view(), name='nainstance-detail'),
    path('news-aggregator/news-aggregator-groups/',
         NAGroupListView.as_view(), name='nainstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('accounting/accountings/',
         AccListView.as_view(), name='accinstance'),
    path('accounting/accountings/new/',
         AccCreateView.as_view(), name='accinstance-create'),
    path('accounting/accountings/<int:pk>/update/', AccUpdateView.as_view(),
         name='accinstance-update'),
    path('accounting/accountings/<int:pk>/delete/',
         AccDeleteView.as_view(), name='accinstance-delete'),
    path('accounting/accountings/<int:pk>/',
         AccDetailView.as_view(), name='accinstance-detail'),
    path('accounting/accounting-groups/',
         AccGroupListView.as_view(), name='accinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('newsletter-manager/newsletter-managers/',
         NMListView.as_view(), name='nminstance'),
    path('newsletter-manager/newsletter-managers/new/',
         NMCreateView.as_view(), name='nminstance-create'),
    path('newsletter-manager/newsletter-managers/<int:pk>/update/', NMUpdateView.as_view(),
         name='nminstance-update'),
    path('newsletter-manager/newsletter-managers/<int:pk>/delete/',
         NMDeleteView.as_view(), name='nminstance-delete'),
    path('newsletter-manager/newsletter-managers/<int:pk>/',
         NMDetailView.as_view(), name='nminstance-detail'),
    path('newsletter-manager/newsletter-manager-groups/',
         NMGroupListView.as_view(), name='nminstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('erp/erp/',
         ERPListView.as_view(), name='erpinstance'),
    path('erp/erp/new/',
         ERPCreateView.as_view(), name='erpinstance-create'),
    path('erp/erp/<int:pk>/update/', ERPUpdateView.as_view(),
         name='erpinstance-update'),
    path('erp/erp/<int:pk>/delete/',
         ERPDeleteView.as_view(), name='erpinstance-delete'),
    path('erp/erp/<int:pk>/',
         ERPDetailView.as_view(), name='erpinstance-detail'),
    path('erp/erp-groups/',
         ERPGroupListView.as_view(), name='erpinstancegroups'),
    # ------------------------------------------------------------------------------------------------------------
    path('bpm/bpm/',
         BPMListView.as_view(), name='bpminstance'),
    path('bpm/bpm/new/',
         BPMCreateView.as_view(), name='bpminstance-create'),
    path('bpm/bpm/<int:pk>/update/', BPMUpdateView.as_view(),
         name='bpminstance-update'),
    path('bpm/bpm/<int:pk>/delete/',
         BPMDeleteView.as_view(), name='bpminstance-delete'),
    path('bpm/bpm/<int:pk>/',
         BPMDetailView.as_view(), name='bpminstance-detail'),
    path('bpm/bpm-groups/',
         BPMGroupListView.as_view(), name='bpminstancegroups'),
    # ------------------------------------------------------------------------------------------------------------

    path('support/overview', SupportOverviewView.as_view(), name='supportoverview'),
    path('support/chat-support/', ChatSupportView.as_view(), name='chatsupport'),
    path('support/phone-support/', PhoneSupportView.as_view(), name='phonesupport'),
    path('getting-started/', GettingStartedView.as_view(), name='gettingstarted'),
    path('documentation/', DocumentationView.as_view(), name='documentation'),
    path('about/', AboutConsoleView.as_view(), name='aboutconsole'),
    path('machine-images/', machine_image_view, name='machineimages'),
]
