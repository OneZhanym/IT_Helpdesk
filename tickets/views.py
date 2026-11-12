from django.shortcuts import render

def home(request):
    context = {
        'title': 'IT Helpdesk',
        'description': 'System for managing IT support tickets',
        'tickets_count' : 0,
    }

    return render(request, 'tickets/home.html', context)
