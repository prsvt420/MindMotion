from django.views.generic import TemplateView


class AboutProjectView(TemplateView):
    """Представление для страницы "О проекте"."""

    template_name: str = "info/about_project.html"


class AboutTeamView(TemplateView):
    """Представление для страницы "О команде"."""

    template_name: str = "info/about_team.html"


class PolicyView(TemplateView):
    """Представление для страницы "Политика конфиденциальности"."""

    template_name: str = "info/policy.html"


class TermsView(TemplateView):
    """Представление для страницы "Пользовательское соглашение"."""

    template_name: str = "info/terms.html"
