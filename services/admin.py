from django.contrib import admin
from .models import *

# Register your models here.


class CEAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "os", "ram",
                    "harddisk", "cpu", "system_group")


class AEAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "os", "ram",
                    "storage", "cpu", "system_group")


class DBAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "database", "ram",
                    "storage", "cpu", "system_group")


class ISAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "infastructure", "ram",
                    "storage", "cpu", "system_group")


class CMSAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "cms", "ram",
                    "storage", "cpu", "system_group")


class DTAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "developer_tools", "ram",
                    "storage", "cpu", "system_group")


class ECAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "e_commerce", "ram",
                    "storage", "cpu", "system_group")


class CRMAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "crm", "ram",
                    "storage", "cpu", "system_group")


class BIAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "business_intelligence", "ram",
                    "storage", "cpu", "system_group")


class ChatAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "chat_service", "ram",
                    "storage", "cpu", "system_group")


class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "analytics", "ram",
                    "storage", "cpu", "system_group")


class BTAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "bug_tracking", "ram",
                    "storage", "cpu", "system_group")


class VCAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "version_control", "ram",
                    "storage", "cpu", "system_group")


class EAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "email_service", "ram",
                    "storage", "cpu", "system_group")


class FAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "forum", "ram",
                    "storage", "cpu", "system_group")


class CRAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "code_review", "ram",
                    "storage", "cpu", "system_group")


class BRAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "binary_repository", "ram",
                    "storage", "cpu", "system_group")


class HRMAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "human_resource_management", "ram",
                    "storage", "cpu", "system_group")


class MSAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "media_sharing", "ram",
                    "storage", "cpu", "system_group")


class SAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "search", "ram",
                    "storage", "cpu", "system_group")


class PSAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "photo_sharing", "ram",
                    "storage", "cpu", "system_group")


class CAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "collaboration", "ram",
                    "storage", "cpu", "system_group")


class MAAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "marketing_automation", "ram",
                    "storage", "cpu", "system_group")


class PMAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "poll_management", "ram",
                    "storage", "cpu", "system_group")


class PortsAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "portal_server", "ram",
                    "storage", "cpu", "system_group")


class ELAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "e_learning", "ram",
                    "storage", "cpu", "system_group")


class WAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "wiki", "ram",
                    "storage", "cpu", "system_group")


class TTAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "translation_tools", "ram",
                    "storage", "cpu", "system_group")


class RDAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "remote_desktop", "ram",
                    "storage", "cpu", "system_group")


class TAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "testing", "ram",
                    "storage", "cpu", "system_group")


class OCAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "online_classifieds", "ram",
                    "storage", "cpu", "system_group")


class SNAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "social_networking", "ram",
                    "storage", "cpu", "system_group")


class CIAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "continuous_integration", "ram",
                    "storage", "cpu", "system_group")


class PromAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "project_management", "ram",
                    "storage", "cpu", "system_group")


class NAAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "news_aggregator", "ram",
                    "storage", "cpu", "system_group")


class AccAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "accounting", "ram",
                    "storage", "cpu", "system_group")


class NMAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "newsletter_manager", "ram",
                    "storage", "cpu", "system_group")


class ERPAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "erp", "ram",
                    "storage", "cpu", "system_group")


class BPMAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "status", "running_ip", "running_port", "bpm", "ram",
                    "storage", "cpu", "system_group")


admin.site.register(Services)
admin.site.register(ComputeEngine, CEAdmin)
admin.site.register(AppEngine, AEAdmin)
admin.site.register(Database, DBAdmin)
admin.site.register(Infastructure, ISAdmin)
admin.site.register(CMS, CMSAdmin)
admin.site.register(DeveloperTools, DTAdmin)
admin.site.register(ECommerce, ECAdmin)
admin.site.register(CRM, CRMAdmin)
admin.site.register(BusinessIntelligence, BIAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Analytics, AnalyticsAdmin)
admin.site.register(BugTracking, BTAdmin)
admin.site.register(VersionControl, VCAdmin)
admin.site.register(EmailService, EAdmin)
admin.site.register(Forum, FAdmin)
admin.site.register(CodeReview, CRAdmin)
admin.site.register(BinaryRepository, BRAdmin)
admin.site.register(HumanResourceManagement, HRMAdmin)
admin.site.register(MediaSharing, MSAdmin)
admin.site.register(Search, SAdmin)
admin.site.register(PhotoSharing, PSAdmin)
admin.site.register(Collaboration, CAdmin)
admin.site.register(MarketingAutomation, MAAdmin)
admin.site.register(PollManagement, PMAdmin)
admin.site.register(PortalServer, PortsAdmin)
admin.site.register(ELearning, ELAdmin)
admin.site.register(Wiki, WAdmin)
admin.site.register(TranslationTools, TTAdmin)
admin.site.register(RemoteDesktop, RDAdmin)
admin.site.register(Testing, TAdmin)
admin.site.register(OnlineClassifieds, OCAdmin)
admin.site.register(SocialNetworking, SNAdmin)
admin.site.register(ContinuousIntegration, CIAdmin)
admin.site.register(ProjectManagement, PromAdmin)
admin.site.register(NewsAggregator, NAAdmin)
admin.site.register(Accounting, AccAdmin)
admin.site.register(NewsletterManager, NMAdmin)
admin.site.register(ERP, ERPAdmin)
admin.site.register(BPM, BPMAdmin)
