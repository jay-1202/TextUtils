# from MODULE import OBJECT
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('home page')
    return render(request, 'index.html')

def analyze(request):
    # post text
    text = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    if removepunc == 'on':
        punctuations = '''`~!@#$%^&*()-_=+[]{}\|;:'"<>,./?'''
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removing Punctuations', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)
    
    if fullcaps == 'on':
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)
    
    if newlineremove == 'on':
        analyzed = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)
    
    if extraspaceremove == 'on':
        analyzed = ''
        for index, char in enumerate(text):
            if not(text[index] == ' ' and text[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)

    else:
        return HttpResponse('ERROR')
    
    return render(request, 'analyze.html', params)