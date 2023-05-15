from django.http import FileResponse, HttpRequest, HttpResponse

def wordSplitter(request):
    archivo = open("tmp/hola.txt", 'w')
    archivo.close()

    return HttpResponse("hola")