from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import UploadedFile
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            download_url = request.build_absolute_uri(reverse('download_file', args=[uploaded_file.id]))
            return render(request, 'upload/success.html', {'download_url': download_url})
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

def download_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    response = HttpResponse(file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
    return response
