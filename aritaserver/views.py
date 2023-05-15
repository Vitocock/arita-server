from django.http import FileResponse, HttpRequest, HttpResponse

def wordSplitter(request):
    return FileResponse(open('goku.zip', 'rb'))