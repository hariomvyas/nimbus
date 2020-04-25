from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
# Create your models here.


class Services(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='media/services', default='media/services/default.jpg',
                             validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    type_choices = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services-detail', kwargs={'pk': self.pk})


class ComputeEngine(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    OS_CHOICE = (
        ('windows', (
            ('windows7', "Windows 7"),
            ('windows 8', "WINDOWS 8"),
            ('windows 10', "WINDOWS 10"),
        )),
        ('linux', (
            ('32bit', "32Bit"),
            ('64bit', "64Bit")
        ))
    )
    os = models.CharField(choices=OS_CHOICE, max_length=25,
                          default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    harddisk_choices = (
        ('10gb', "10GB"),
        ('100gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    harddisk = models.CharField(
        choices=harddisk_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('ai&ml', "AI & ML"),
    )
    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ceinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class AppEngine(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    OS_CHOICE = (
        ('oreo', (
            ('32bit', "32 Bit"),
            ('64bit', "64 Bit"),
        )),
        ('nougat', (
            ('32bit', "32 Bit"),
            ('64bit', "64 Bit"),
        )),
        ('marshmallow', (
            ('32bit', "32 Bit"),
            ('64bit', "64 Bit"),
        )),
    )
    os = models.CharField(choices=OS_CHOICE, max_length=25,
                          default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('ai&ml', "AI & ML"),
    )
    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('aeinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Database(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    DB_CHOICE = (
        ('mongo', "MongoDB"),
        ('couch', "CouchDB"),
        ('maria', "MariaDB"),
        ('neo4j', "Neo4j"),
        ('postgresql', "PostgreSQL"),
        ('mysql', "MySQL"),
        ('redis', "Redis"),
        ('cassandra', "Cassandra")
    )
    database = models.CharField(choices=DB_CHOICE, max_length=25,
                                default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dbinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Infastructure(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    IS_CHOICE = (
        ('lamp', "LAMP"),
        ('django', "Django"),
        ('lapp', "LAPP"),
        ('apachesolr', "Apache Solr"),
        ('mean', "MEAN"),
        ('wildfly', "WildFly"),
        ('rabbitmq', "RabbitMQ"),
        ('memcached', "Memcached"),
        ('kafka', "Kafka"),
        ('hhvm', "HHVM"),
        ('tomcat', "Tomcat"),
        ('ruby', "Ruby"),
        ('zookeeper', "ZooKeeoper"),
        ('tenserflow', "TensorFlow Serving"),
        ('node', "Node.js"),
        ('hashicorp', "HashiCorp Consul"),
        ('nginx', "NGINX Open Source"),
        ('jruby', "JRuby"),
        ('nats', "NATS"),
        ('etcd', "ETCD")
    )
    infastructure = models.CharField(choices=IS_CHOICE, max_length=25,
                                     default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('isinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class CMS(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    CMS_CHOICE = (
        ('wordpress', "Wordpress"),
        ('wordpressmulti', "Wordpress Multisite"),
        ('wordpressnginx', "Wordpress with NGINX"),
        ('wordpressnginxssl', "Wordpress with NGINX and SSL"),
        ('wordpressready', "Wordpress Production-Ready"),
        ('drupal', "Drupal"),
        ('drupalnginx', "Drupal with NGINX"),
        ('joomla', "Joomla!"),
        ('plone', "Plone"),
        ('alfresco', "Alfresco Community"),
        ('cmsmade', "CMS Made Simple"),
        ('modx', "MODX"),
        ('silverstripe', "SilverStripe"),
        ('typo3', "TYPO3"),
        ('xoops', "XOOPS"),
        ('tikiwiki', "Tiki Wiki CMS Groupware"),
        ('concrete5', "concrete5"),
        ('openatrium', "Open Atrium"),
        ('processwire', "ProcessWire"),
        ('pimcore', "Pimcore"),
        ('neos', "Neos"),
        ('shopware', "Shopware"),
        ('ckan', "CKAN"),
        ('composr', "Composr")
    )
    cms = models.CharField(choices=CMS_CHOICE, max_length=25,
                           default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cmsinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class DeveloperTools(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    DT_CHOICE = (
        ('activemq', "ActiveMQ"),
        ('hadoop', "Hadoop"),
        ('parseserver', "ParseServer")
    )
    developer_tools = models.CharField(choices=DT_CHOICE, max_length=25,
                                       default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dtinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class ECommerce(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    EC_CHOICE = (
        ('magento', "Magento"),
        ('spree', "Spree"),
        ('prestashop', "PrestaShop"),
        ('oxid', "OXID eShop"),
        ('opencart', "OpenCart"),
        ('akeneo', "Akeneo"),
        ('shopware', "Shopware")
    )
    e_commerce = models.CharField(choices=EC_CHOICE, max_length=25,
                                  default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ecinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class CRM(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    CRM_CHOICE = (
        ('civi', "CiviCRM"),
        ('fatfree', "Fat Free CRM"),
        ('zurmo', "Zurmo"),
        ('dolibaar', "Dolibaar"),
        ('espo', "EspoCRM"),
        ('suite', "SuiteCRM"),
        ('oro', "OroCRM")
    )
    crm = models.CharField(choices=CRM_CHOICE, max_length=25,
                           default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crminstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class BusinessIntelligence(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    BI_CHOICE = (
        ('rsc', "Report Server Community"),
        ('rse', "Report Server Enterprise"),
        ('jasper', "JasperReports")
    )
    business_intelligence = models.CharField(choices=BI_CHOICE, max_length=25,
                                             default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('biinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Chat(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    CHAT_CHOICE = (
        ('openfire', "Openfire"),
        ('letschat', "Let's Chat"),
        ('livehelper', "Live Helper Chat"),
        ('mattermost', "Mattermost Team Edition")
    )
    chat_service = models.CharField(choices=CHAT_CHOICE, max_length=25,
                                    default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chatinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Analytics(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    A_CHOICE = (
        ('seopanel', "SEO Panel"),
        ('redash', "Re:dash"),
        ('elk', "ELK"),
        ('grafana', "Grafana"),
        ('matoma', "Matoma")
    )
    analytics = models.CharField(choices=A_CHOICE, max_length=25,
                                 default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('analyticsinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class BugTracking(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    BT_CHOICE = (
        ('mantis', "Mantis"),
        ('trac', "Trac"),
        ('redmine', "Redmine"),
        ('phabricator', "Phabricator"),
        ('jetbrains', "JetBrains YouTrack"),
        ('redmine', "Redmine & Agile")
    )
    bug_tracking = models.CharField(choices=BT_CHOICE, max_length=25,
                                    default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('btinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class VersionControl(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    VC_CHOICE = (
        ('subversion', "Subversion"),
        ('gitlab', "GitLab CE")
    )
    version_control = models.CharField(choices=VC_CHOICE, max_length=25,
                                       default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vcinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class EmailService(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    E_CHOICE = (
        ('roundcube', "Roundcube"),
        ('horde', "Horde Groupware Webmail"),
        ('webmail', "WebMail Pro PHP")
    )
    email_service = models.CharField(choices=E_CHOICE, max_length=25,
                                     default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('einstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Forum(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    F_CHOICE = (
        ('phpbb', "phpBB"),
        ('discourse', "Discourse"),
        ('mybb', "MyBB")
    )
    forum = models.CharField(choices=F_CHOICE, max_length=25,
                             default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('finstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class CodeReview(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    CR_CHOICE = (
        ('review', "Review Board"),
        ('sonarqube', "SonarQube"),
        ('rbpp', "Review Board + Power Pack")
    )
    code_review = models.CharField(choices=CR_CHOICE, max_length=25,
                                   default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class BinaryRepository(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    BR_CHOICE = (
        ('jfrog', "JFrog Artifactory Open Source"),
    )
    binary_repository = models.CharField(choices=BR_CHOICE, max_length=25,
                                         default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('brinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class HumanResourceManagement(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    HRM_CHOICE = (
        ('orange', "OrangeHRM"),
    )
    human_resource_management = models.CharField(choices=HRM_CHOICE, max_length=25,
                                                 default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hrminstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class MediaSharing(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    MS_CHOICE = (
        ('resourcespace', "ResourceSpace"),
        ('owncloud', "ownCloud"),
    )
    media_sharing = models.CharField(choices=MS_CHOICE, max_length=25,
                                     default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('msinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Search(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    S_CHOICE = (
        ('elasticsearch', "ElasticSearch"),
    )
    search = models.CharField(choices=S_CHOICE, max_length=25,
                              default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class PhotoSharing(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    PS_CHOICE = (
        ('coppermine', "Coppermine"),
    )
    photo_sharing = models.CharField(choices=PS_CHOICE, max_length=25,
                                     default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('psinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Collaboration(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    C_CHOICE = (
        ('mahara', "Mahara"),
    )
    collaboration = models.CharField(choices=C_CHOICE, max_length=25,
                                     default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class MarketingAutomation(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    MA_CHOICE = (
        ('mautic', "Mautic"),
    )
    marketing_automation = models.CharField(choices=MA_CHOICE, max_length=25,
                                            default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mainstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class PollManagement(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    PM_CHOICE = (
        ('limesurvey', "LimeSurvey"),
    )
    poll_management = models.CharField(choices=PM_CHOICE, max_length=25,
                                       default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pminstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class PortalServer(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    PS_CHOICE = (
        ('liferay', "Liferay"),
    )
    portal_server = models.CharField(choices=PS_CHOICE, max_length=25,
                                     default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portsinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class ELearning(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    EL_CHOICE = (
        ('moodle', "Moodle"),
        ('canvaslms', "Canvas LMS"),
        ('openedx', "Open edX")
    )
    e_learning = models.CharField(choices=EL_CHOICE, max_length=25,
                                  default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('elinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Wiki(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    W_CHOICE = (
        ('doku', "DokuWiki"),
        ('media', "MediaWiki"),
    )
    wiki = models.CharField(choices=W_CHOICE, max_length=25,
                            default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('winstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class TranslationTools(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    TT_CHOICE = (
        ('pootle', "Pootle"),
        ('weblate', "Weblate"),
    )
    translation_tools = models.CharField(choices=TT_CHOICE, max_length=25,
                                         default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ttinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class RemoteDesktop(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    RD_CHOICE = (
        ('guacamole', "Apache Guacamole"),
    )
    remote_desktop = models.CharField(choices=RD_CHOICE, max_length=25,
                                      default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rdinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Testing(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    T_CHOICE = (
        ('testlink', "TestLink"),
    )
    testing = models.CharField(choices=T_CHOICE, max_length=25,
                               default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class OnlineClassifieds(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    OC_CHOICE = (
        ('osclass', "Osclass"),
    )
    online_classifieds = models.CharField(choices=OC_CHOICE, max_length=25,
                                          default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ocinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class SocialNetworking(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    SN_CHOICE = (
        ('jfrog', "JFrog Artifactory Open Source"),
    )
    social_networking = models.CharField(choices=SN_CHOICE, max_length=25,
                                         default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sninstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class ContinuousIntegration(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    CI_CHOICE = (
        ('jenkins', "Jenkins"),
    )
    continuous_integration = models.CharField(choices=CI_CHOICE, max_length=25,
                                              default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ciinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class ProjectManagement(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    PROM_CHOICE = (
        ('openatrium', "Open Atrium"),
    )
    project_management = models.CharField(choices=PROM_CHOICE, max_length=25,
                                          default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prominstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class NewsAggregator(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    NA_CHOICE = (
        ('tiny', "Tiny Tiny RSS"),
    )
    news_aggregator = models.CharField(choices=NA_CHOICE, max_length=25,
                                       default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('nainstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class Accounting(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    ACC_CHOICE = (
        ('noalyss', "Noalyss"),
    )
    accounting = models.CharField(choices=ACC_CHOICE, max_length=25,
                                  default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('accinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class NewsletterManager(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    NM_CHOICE = (
        ('phplist', "phpList"),
    )
    newsletter_manager = models.CharField(choices=NM_CHOICE, max_length=25,
                                          default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('nminstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class ERP(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    ERP_CHOICE = (
        ('erpnext', "ERP Next"),
        ('odoo', "Odoo"),
    )
    erp = models.CharField(choices=ERP_CHOICE, max_length=25,
                           default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement")
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('erpinstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------


class BPM(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    BPM_CHOICE = (
        ('pme', "ProcessMaker Enterprise"),
        ('pmc', "ProcessMaker Community")
    )
    bpm = models.CharField(choices=BPM_CHOICE, max_length=25,
                           default='')

    ram_choices = (
        ('128mb', "128MB"),
        ('512mb', "512MB"),
        ('1024mb', "1024MB"),
        ('2048mb', "2048MB"),
        ('4096mb', "4096MB"),
        ('8192mb', "8192MB")
    )
    ram = models.CharField(max_length=8, choices=ram_choices, default='1024mb')

    storage_choices = (
        ('10gb', "10GB"),
        ('50gb', "100GB"),
        ('500gb', "500GB"),
        ('1tb', "1TB"),
        ('2tb', "2TB")
    )
    storage = models.CharField(
        choices=storage_choices, default='10GB', max_length=8)

    cpu_choices = (
        ('1cpu', "1CPU"),
        ('2cpu', "2CPU"),
        ('3cpu', "3CPU"),
        ('4cpu', "4CPU")
    )
    cpu = models.CharField(choices=cpu_choices, max_length=5, default='1cpu')

    group_choices = (
        ('regular', "Regular"),
        ('testing', "Testing"),
        ('teach', "Teaching"),
        ('dev', "Developement"),
    )

    system_group = models.CharField(choices=group_choices, max_length=10,
                                    default='regular', help_text="Distribute your Systems Group wise.")

    status_choices = (
        ('not created', "Not Created"),
        ('created', "Created"),
        ('running', "Running"),
        ('maintenance', "Under Maintenance"),
    )
    status = models.CharField(choices=status_choices,
                              max_length=11, default='not created')

    running_ip = models.CharField(max_length=15, default='System IP')
    running_port = models.CharField(max_length=5, default='80')

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bpminstance-detail', kwargs={'pk': self.pk})

# --------------------------------------------------------------------------------------------------------------------------------------------
