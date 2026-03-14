from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Cocktail
from .forms.CoctailAddForm import CoctailAddForm

# Create your views here.

def coctail_list(request):
    coctails_list = Cocktail.objects.all().order_by('name')
    return render(request, 'coctails_app/coctail_list.html', {'coctails_list': coctails_list})

def coctail_detail(request, coctail_id):
    coctail = get_object_or_404(Cocktail, id=coctail_id)
    ingredients = coctail.cocktailingredient_set.select_related('ingredient').all()
    return render(request, 'coctails_app/coctail_detail.html', {
        'coctail': coctail,
        'ingredients': ingredients,
    })
    
def coctail_create(request):
    return render(request, 'coctails_app/coctail_create.html', {'form': CoctailAddForm()})

def coctail_insert(request):
    if request.method == 'POST':
        form = CoctailAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].strip()
            category_name = form.cleaned_data['category'].strip()
            instructions = form.cleaned_data['instructions']
            is_alcoholic = form.cleaned_data['is_alcoholic']

            category_obj = None
            if category_name:
                category_obj, _ = Category.objects.get_or_create(name=category_name)

            Cocktail.objects.create(
                name=name,
                category=category_obj,
                instructions=instructions,
                is_alcoholic=is_alcoholic,
            )

            return render(request, 'coctails_app/coctail_add.html', {
                'form': CoctailAddForm(),
                'success': f"Koktajl '{name}' został dodany do bazy danych.",
            })
    else:
        form = CoctailAddForm()

    return render(request, 'coctails_app/coctail_add.html', {'form': form})

#def coctail_edit(request, coctail_id):