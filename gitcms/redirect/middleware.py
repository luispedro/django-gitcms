from django.http import HttpResponsePermanentRedirect
from .models import Redirect

class RedirectMiddleware(object):
    '''
    '''
    def process_request(self, request):
        path = request.path
        print 'process_request "%s"' % path
        if path[0] == '/': path = path[1:]
        redirect = Redirect.objects.filter(source=path)
        if not redirect:
            return None
        return HttpResponsePermanentRedirect('/'+redirect[0].target)
