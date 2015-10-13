from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from .forms import UploadFileForm

# Create your views here.

#def import_view(request):
    #return render(request, 'hicks_import_export/import.html')

@csrf_protect
def import_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('.')
    else:
        form = UploadFileForm()
    return render_to_response('hicks_import_export/import.html', {'form': form}, RequestContext(request))