from django.contrib import admin

from ads import models


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.CampaignStats)
class CampaignStatsAdmin(admin.ModelAdmin):
    list_display = ("date", "campaign", "data_source", "clicks", "impressions",)
    list_select_related = ("campaign", "data_source",)
