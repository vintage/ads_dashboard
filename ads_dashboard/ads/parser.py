import datetime
import typing
import csv

from ads import services, models


class CampaignStatsParserItem:
    def __init__(self, data: typing.List[str]):
        self.date = datetime.datetime.strptime(data[0], '%d.%m.%Y')
        self.data_source = data[1]
        self.campaign = data[2]
        self.clicks = int(data[3])
        self.impressions = int(data[4] or 0)

    def __str__(self):
        return f"""
            Date: {self.date}
            Data source: {self.data_source}
            Campaign: {self.campaign}
            Clicks: {self.clicks}
            Impressions: {self.impressions}
        """


def parse_file(file) -> typing.Iterable[CampaignStatsParserItem]:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        yield CampaignStatsParserItem(row)


def save_items(items: typing.Iterable[CampaignStatsParserItem]) -> int:
    data_sources = {}
    campaigns = {}

    stats_objects = []
    for item in items:
        data_source_name = item.data_source
        if data_source_name not in data_sources.keys():
            data_sources[data_source_name] = services.get_or_create_data_source(name=data_source_name)

        campaign_name = item.campaign
        if campaign_name not in campaigns.keys():
            campaigns[campaign_name] = services.get_or_create_campaign(name=campaign_name)

        stats_objects.append(
            models.CampaignStats(
                date=item.date,
                data_source_id=data_sources[data_source_name].id,
                campaign_id=campaigns[campaign_name].id,
                clicks=item.clicks,
                impressions=item.impressions,
            )
        )

    return services.create_bulk_campaign_stats(stats_objects)

