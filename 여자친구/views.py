from django.shortcuts import render

group = "여자친구"

# Create your views here.
def show_유주(request):
    return render(request, '유주.html', {'group': group, 'member': '유주'})

def show_소원(request):
    return render(request, '소원.html', {'group': group, 'member': '소원'})

def show_예린(request):
    return render(request, '예린.html', {'group': group, 'member': '예린'})

def show_신비(request):
    return render(request, '신비.html', {'group': group, 'member': '신비'})

def show_엄지(request):
    return render(request, '엄지.html', {'group': group, 'member': '엄지'})

def show_은하(request):
    return render(request, '은하.html', {'group': group, 'member': '은하'})
