from django.conf.urls import include, url

from . import views

urlpatterns = [
    # URL pattern for the LangListView
    url(
        regex=r'^$',
        view=views.LangListView.as_view(),
        name='list'
    ),
    # URL pattern for the LangDetailView
    url(  # /de-de/
          regex=r'^(?P<code>[^/]*)/$',
          view=views.LangDetailView.as_view(),
          name='detail'
          )
]
