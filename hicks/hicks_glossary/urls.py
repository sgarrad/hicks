from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ProjectListView
    url(
        regex=r'^$',
        view=views.ProjectListView.as_view(),
        name='list'
    ),

    # URL pattern for the ProjectDetailView
    url(
        regex=r'^(?P<slug>[^/]*)/$',
        view=views.ProjectDetailView.as_view(),
        name='detail'
    ),
]
