from django.apps import AppConfig



class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.user'

    def ready(self):
        """
        Registra os signals quando o app está pronto.
        Isso garante que o UserProfile seja criado automaticamente.
        """
        import app.user.signals  # noqa