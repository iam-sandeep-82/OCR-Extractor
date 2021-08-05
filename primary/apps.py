from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PrimaryConfig(AppConfig):
    name = 'primary'
    verbose_name = _('Primary Application')

    def ready(self):
        import primary.signals