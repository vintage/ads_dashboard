from django.views import generic

from ads import forms, services


class CampaignStatsChartView(generic.FormView):
    form_class = forms.CampaignStatsFilterForm
    template_name = "ads/campaign_stats_chart.html"

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_objects(self, form):
        if form.is_valid():
            return services.get_campaign_stats(
                data_sources=form.cleaned_data.get("data_sources"),
                campaigns=form.cleaned_data.get("campaigns"),
            )
        else:
            return services.get_campaign_stats()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"objects": self.get_objects(form=context["form"]),}
        )

        return context
