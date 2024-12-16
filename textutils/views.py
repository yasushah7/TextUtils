# file created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    allcaps = request.POST.get('allcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    numberremove = request.POST.get('numberremove', 'off')

    # check which checkbox is on
    if removepunc == 'on':
        # analyze the text
        analyzed = ''
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if allcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed+char
        params = {'purpose': 'Removing New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremove == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Removing Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if numberremove == 'on':
        analyzed = ''
        num = '0123456789'
        for char in djtext:
            if char not in num:
                analyzed = analyzed + char
        params = {'purpose': 'Removing Extra Space', 'analyzed_text': analyzed}

    if removepunc != "on" and spaceremove != 'on' and newlineremove != 'on' and allcaps != 'on' and numberremove != 'on':
        return HttpResponse('Please select any operation')

    return render(request, 'analyze.html', params)

def about(request):
    return render(request,'about.html')
