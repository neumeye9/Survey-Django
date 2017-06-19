from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print "Hi"
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    print request.session['counter']
    return render(request, 'survey_app/index.html')

def process(request):
    print "Form"
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        print request.session['name']
        request.session['location'] = request.POST['dojo']
        request.session['language'] = request.POST['favlanguage']
        request.session['comments'] = request.POST['comment']
        return redirect('/formresults')
    else:
        return redirect('/')

def formresults(request):
    print "Form Submitted"
    return render(request, 'survey_app/survey.html')

def reset(request):
    print "Done!"
    return redirect('/')