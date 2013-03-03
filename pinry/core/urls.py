from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from tastypie.api import Api

from .api import ImageResource, ThumbnailResource, PinResource, UserResource
from .views import CreateImage


v1_api = Api(api_name='v1')
v1_api.register(ImageResource())
v1_api.register(ThumbnailResource())
v1_api.register(PinResource())
v1_api.register(UserResource())


urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls, namespace='api')),

    url(r'^pin-form/$', TemplateView.as_view(template_name='core/pin_form.html'),
        name='pin-form'),
    url(r'^create-image/$', CreateImage.as_view(), name='create-image'),
    url(r'^tag/(?P<tag>(\w|-)+)/$', TemplateView.as_view(template_name='core/pins.html'),
        name='tag-pins'),
    url(r'^private/$', 'pinry.core.views.private', name='private'),
    url(r'^$', TemplateView.as_view(template_name='core/pins.html'),
        name='recent-pins'),
)
