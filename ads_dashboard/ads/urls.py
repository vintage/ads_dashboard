from django.urls import path

from ads import views

urlpatterns = [
    path("", views.CampaignStatsChartView.as_view(), name="index"),
]
