from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    lineremover = request.GET.get('lineremover','off')
    fullcaps = request.GET.get('fullcaps','off')
    charcount = request.GET.get('charcount','off')
    spaceremove = request.GET.get('spaceremove','off')

    params = {'analyzed': '', 'purpose': ''}

    if removepunc=='on':
        analyzed_text = ''
        pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in pun:
                analyzed_text+=char
        params['purpose']+='Remove Punctuation '
        params['analyzed']=analyzed_text

    if lineremover == 'on':
        analyzed_text = ''
        if params['analyzed']!='':
            djtext=params['analyzed']
        for char in djtext:
            if char !='\n':
                analyzed_text+=char
        params['purpose']+='Remove Lines'
        params['analyzed']=analyzed_text

    if fullcaps == 'on':
        analyzed_text = ''
        if params['analyzed']!='':
            djtext=params['analyzed']
        for char in djtext:
            analyzed_text += char.upper()
        params['purpose'] += 'Capitalize the string '
        params['analyzed'] = analyzed_text

    if charcount == 'on':
        analyzed_text = ''
        if params['analyzed']!='':
            djtext=params['analyzed']
        params['purpose'] += 'Character counter '
        params['analyzed'] += ' and the character count is --> '+str(len(djtext))

    if spaceremove == 'on':
        analyzed_text = ''
        if params['analyzed']!='':
            djtext=params['analyzed']
        print('djtext ',djtext)
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' ') :
                analyzed_text += char
        params['purpose'] += 'Remove Spaces '
        params['analyzed'] = analyzed_text

    return render(request, 'analyze.html', params)

