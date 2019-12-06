from django.db import models


class Campaign(models.Model):
    name = models.CharField("name", unique=True, max_length=255)

    class Meta:
        verbose_name = "campaign"
        verbose_name_plural = "campaigns"

    def __str__(self):
        return self.name


class DataSource(models.Model):
    name = models.CharField("name", unique=True, max_length=255)

    class Meta:
        verbose_name = "data source"
        verbose_name_plural = "data sources"

    def __str__(self):
        return self.name


class CampaignStats(models.Model):
    date = models.DateField("date")
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    clicks = models.IntegerField("clicks")
    impressions = models.IntegerField("impressions")

    class Meta:
        verbose_name = "campaign stats"
        verbose_name_plural = "campaign stats"
        unique_together = (
            ("date", "data_source", "campaign",),
        )

    def __str__(self):
        return f"Stats #{self.pk}"
