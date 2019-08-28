from django.apps import AppConfig


class RepoConfig(AppConfig):
    name = 'apps.repo'
    verbose_name = '题库'

    def ready(self):
        from .signal import handler
