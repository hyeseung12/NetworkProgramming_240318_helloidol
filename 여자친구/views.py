from django.shortcuts import render

group = {
    'members': [
        {
            'group': '여자친구',
            'name': '유주'
        },
        {
            'group': '여자친구',
            'name': '소원'
        },
        {
            'group': '여자친구',
            'name': '예린'
        },
        {
            'group': '여자친구',
            'name': '신비'
        },
        {
            'group': '여자친구',
            'name': '엄지'
        },
        {
            'group': '여자친구',
            'name': '은하'
        }
    ]
}

# Create your views here.
def show_유주(request):
    context = list(filter(lambda member: '유주' in member['name'], group['members']))[0]
    return render(request, '멤버.html', context)

def show_소원(request):
    context = list(filter(lambda member: '소원' in member['name'], group['members']))[0]
    return render(request, '멤버.html', context)

def show_예린(request):
    context = list(filter(lambda member: '예린' in member['name'], group['members']))[0]
    return render(request, '멤버.html', context)

def show_신비(request):
    context = list(filter(lambda member: '신비' in member['name'], group['members']))[0]
    return render(request, '멤버.html', context)

def show_엄지(request):
    context = list(filter(lambda member: '엄지' in member['name'], group['members']))[0]
    return render(request, '멤버.html', context)

def show_은하(request):
    context = list(filter(lambda member: '은하' in member['name'], group['members']))[0]
    return render(request, '멤버.html', context)

def show_멤버(request, 멤버):
    context = list(filter(lambda member: 멤버 in member['name'], group['members']))[0]
    return render(request, '멤버.html', context=context)