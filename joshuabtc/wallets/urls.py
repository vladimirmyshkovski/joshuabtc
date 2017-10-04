from django.conf.urls import url

from joshuabtc.wallets import views

urlpatterns = [
    url(
        regex=r'^btc/$',
        view=views.BTCListView.as_view(),
        name='btc_list'
    ),
    url(
        regex=r'^btc/(?P<pk>\d+)/~redirect/$',
        view=views.BTCRedirectView.as_view(),
        name='btc_redirect'
    ),
    url(
        regex=r'^btc/(?P<pk>\d+)/$',
        view=views.BTCDetailView.as_view(),
        name='btc_detail'
    ),
    url(
        regex=r'^btc/(?P<pk>\d+)/~update/$',
        view=views.BTCUpdateView.as_view(),
        name='btc_update'
    ),
    url(
        regex=r'^btc/(?P<pk>\d+)/~delete/$',
        view=views.BTCDeleteView.as_view(),
        name='btc_delete'
    ),
    url(
        regex=r'^btc/~create/$',
        view=views.BTCCreateView.as_view(),
        name='btc_create'
    ),
]
'''
    url(
        regex=r'^eth/$',
        view=views.ETHListView.as_view(),
        name='eth_list'
    ),
    url(
        regex=r'^eth/(?P<pk>\d+)/~redirect/$',
        view=views.ETHRedirectView.as_view(),
        name='eth_redirect'
    ),
    url(
        regex=r'^eth/(?P<pk>\d+)/$',
        view=views.ETHDetailView.as_view(),
        name='eth_detail'
    ),
    url(
        regex=r'^eth/(?P<pk>\d+)/~update/$',
        view=views.ETHUpdateView.as_view(),
        name='eth_update'
    ),
    url(
        regex=r'^eth/(?P<pk>\d+)/~delete/$',
        view=views.ETHDeleteView.as_view(),
        name='eth_delete'
    ),
    url(
        regex=r'^eth/~create/$',
        view=views.ETHCreateView.as_view(),
        name='eth_create'
    ),
]
'''