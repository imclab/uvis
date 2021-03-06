from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('diag.views',
        url(r'^api/get_plot_package', 'get_plot_package'),
        url(r'^api/run', 'run'),
        url(r'^api/get_status', 'get_status'),
        url(r'^api/load_output/(?P<task_id>\d+\.?\d+)/$', 'load_output'),
	url(r'^api/get_plot_set', 'get_plot_set'),
	url(r'^api/get_plot_seasons', 'get_plot_seasons'),
	url(r'^api/get_plot_variable', 'get_plot_variable'),
	url(r'^api/get_plot_aux_options', 'get_plot_aux_options'),
	url(r'^api/get_plot_obs', 'get_plot_obs'),
	url(r'^submit', 'submit_job'),

        )

