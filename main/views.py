from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165710',
        'name': 'Leonita Cecilia',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
