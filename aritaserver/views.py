from django.http import FileResponse, HttpRequest, HttpResponse

def wordSplitter(request):
    archivo = open("hola.txt", 'w')
    archivo.close()
    return FileResponse(open('goku.zip', 'rb'))