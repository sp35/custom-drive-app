from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import Upload

@login_required
def home(request):
	uploads = Upload.objects.all().filter(user=request.user)

	return render(request, 'drive/home.html', {'uploads': uploads})

@login_required
def download(request, pk):
	upload = get_object_or_404(Upload, pk=pk)
	file_name = upload.file.name

	response = HttpResponse(upload.file)
	response['Content-Disposition'] = f'attachment; filename={file_name}'
	return response

@login_required
def user_uploads(request):
	try:
		to_be_uploaded = request.FILES['to_be_uploaded']
	except MultiValueDictKeyError:
		return HttpResponse("Upload Failed")
	upload = Upload.objects.create(user=request.user, file=to_be_uploaded)

	return redirect('drive-home')