from django.shortcuts import render, redirect


def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
        print('key exists!')
    else:
        request.session['counter'] = 1
        print("key 'key_name' does NOT exist")

    return render(request, 'index.html')


def destroy(request):
    request.session['counter'] = 0

    return redirect('/')


def addTwo(request):
    if 'counter' in request.session:
        request.session['counter'] += 2

    return render(request, 'index.html')


def anyNumber(request):
    if 'counter' in request.session:
        int_from_form = request.POST['anyInt']
        request.session['counter'] += int(int_from_form) 
        # Line 31 is casting - 'int(int_from_form)' is how you cast
        print(int_from_form)

    return render(request, 'index.html')