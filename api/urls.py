from django.urls import path

from api.views import ListAgentView

urlpatterns = [
    path("agents", ListAgentView.as_view(), name="list-agents"),
]
