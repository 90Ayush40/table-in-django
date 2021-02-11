from django.shortcuts import render
from django.db import connection


def createtab(request):
    if request.method == "POST":
        if request.POST.get('x'):
            cursor = connection.cursor()
            cursor.execute(request.POST.get('x'))
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')
