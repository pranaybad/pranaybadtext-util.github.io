# i have created this file -pranay
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>hello pranay</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> django code</a>''')
#
# def about(request):
#     return HttpResponse("about pranay")

def index(request):
    return render(request,'index.html')

    # return HttpResponse("home")
# def ex1(request):
#     s ='''<h2>navigation bar</h2>
#     <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">
#     django video</a><br>
#     <a href="https://www.youtube.com/">YT</a><br>
#     <a href="https://www.instagram.com/">insta</a><br>
#     <a href="https://www.facebook.com/">fb</a><br>
#     <a href="https://www.github.com/">GH</a>
#     '''
#     return HttpResponse(s)

def analyze(request):
    # get the text analize text
    djtext = request.POST.get('text','default')
    print(djtext)

    # check box value
    removepunc = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcap','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercoun = request.POST.get('charactercoun','off')
    # print(removepunc)
    # print(djtext)

    # check which checkbox is on
    if removepunc == "on":
        # analyze = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*-~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        params = {'purpose': 'REmove Punctuation', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)




    elif(fullcap=="on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()

        params = {'purpose': 'change upper case', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)


        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyze = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyze = analyze + char


        params = {'purpose': 'change upper case', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)



    elif (extraspaceremover == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            analyze = analyze + char

        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)

    elif (charactercoun == "on"):
        analyze = len(djtext)
        # for char in djtext:
            # analyze+= 1
            #     analyze = analyze + char


        params = {'purpose': 'charactercoun', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)




    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("capitilize first<a href='/'>back</a>")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove first")
#
# def spacrremove(request):
#     return HttpResponse("spacrremove first")
#
# def charcount(request):
#     return HttpResponse("charcount  first")