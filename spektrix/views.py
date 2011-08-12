from django.conf import settings
from django.http import QueryDict, Http404
from django.views.generic.base import TemplateResponseMixin, View


class SpektrixIFrameMixin(object):

    spektrix_pages = {
        'checkout': 'Checkout',
        'account': 'MyAccount',
        'basket': 'Basket2',
        'login': 'LoginLogout',
        'choose-seats': 'ChooseSeats'}

    def get_context_data(self, **kwargs):
        page_name = self.kwargs.get('page')
        EventId = self.kwargs.get('EventId')

        # Choose spektrix page
        if not (page_name and page_name in self.spektrix_pages.keys()):
            raise Http404

        # Optional extra get params to send to spektrix
        arguments = QueryDict('resize=true', mutable=True)
        if EventId:
            arguments.update({'EventId': EventId})

        # Template context vars
        kwargs.update({
            'arguments': arguments.urlencode(),
            'clientname': settings.SPEKTRIX_CLIENT,
            'page': self.spektrix_pages[page_name],            
            'title': page_name})

        return super(SpektrixIFrameMixin, self).get_context_data(**kwargs)


class TemplateView(TemplateResponseMixin, View):
    """
    A view that renders a template.
    """
    def get_context_data(self, **kwargs):
        # Overwide this to stop it returning kwargs wrapped in params dict
        return kwargs

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class SpektrixIFrameView(SpektrixIFrameMixin, TemplateView):

    template_name = 'spektrix/base.html'
