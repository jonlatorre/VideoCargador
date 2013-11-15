from jqueryfileupload.views import *
from django.views.generic import CreateView, DeleteView, ListView, TemplateView

from serialize import serialize
from models import *

class UploadVideoView(CreateView):
    model = Video
    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
    
class DeleteVideoView(DeleteFileView):  
    model = Video

class VideoListView(ListView):
    model = Video

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

