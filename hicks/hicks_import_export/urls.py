from django.conf.urls import include, url

from . import views

urlpatterns = [
    # URL pattern for importing files
    url(  # /import/
        regex=r'^import/$',
        view=views.import_view,
        name='import'
    ),
]
