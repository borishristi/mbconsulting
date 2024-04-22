from mbconsulting import settings
from django.conf.urls.static import static
from django.urls import path

from .views import home_view, contact_view, service_view, about_view, project_view, feature_view, quote_view, team_view
from .views import testimonial_view, error_404_view

urlpatterns = [
    path('', home_view, name="home"),
    path('contact/', contact_view, name="contact"),
    path('service/', service_view, name="service"),
    path('about/', about_view, name="about"),
    path('project/', project_view, name="project"),
    path('feature/', feature_view, name="feature"),
    path('quote/', quote_view, name="quote"),
    path('team/', team_view, name="team"),
    path('testimonial/', testimonial_view, name="testimonial"),
    path('error_404/', error_404_view, name="404"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
