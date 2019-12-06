import datetime
import typing

from ads import models


def get_or_create_data_source(name: str) -> typing.Optional[models.DataSource]:
    return models.DataSource.objects.get_or_create(name=name)[0]


def get_or_create_campaign(name: str) -> typing.Optional[models.Campaign]:
    return models.Campaign.objects.get_or_create(name=name)[0]


def create_bulk_campaign_stats(stats: typing.List[models.CampaignStats]) -> int:
    return models.CampaignStats.objects.bulk_create(stats, ignore_conflicts=True)


def create_or_update_campaign_stats(
        date: datetime.date,
        data_source: models.DataSource,
        campaign: models.Campaign,
        clicks: int,
        impressions: int,
):
    return models.CampaignStats.objects.update_or_create(
        date=date, data_source=data_source, campaign=campaign,
        defaults={"clicks": clicks, "impressions": impressions},
    )
