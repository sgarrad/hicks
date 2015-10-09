from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .forms import UploadFileForm

# Create your views here.

#def import_view(request):
    #return render(request, 'hicks_import_export/import.html')

def import_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('hicks_import_export/import.html', {'form': form})