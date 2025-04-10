from django.views.generic import TemplateView


class AboutProjectView(TemplateView):
    """Представление для страницы "О проекте"."""

    template_name: str = "info/about_project.html"
