from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275512',
        'name': 'Yovan Raju',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
