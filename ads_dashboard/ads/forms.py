from django import forms

from ads import services


class SelectMultipleSemantic(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["class"] = "ui dropdown"


class CampaignStatsFilterForm(forms.Form):
    campaigns = forms.ModelMultipleChoiceField(
        queryset=services.get_campaigns(),
        widget=SelectMultipleSemantic(),
        required=False,
    )
    data_sources = forms.ModelMultipleChoiceField(
        queryset=services.get_data_sources(),
        widget=SelectMultipleSemantic(),
        required=False,
    )
