from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
        'масло сливочное, г': 20,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe(request, dish):
    servings = request.GET.get('servings')
    try:
        recipe_data = DATA[dish]
    except KeyError:
        return HttpResponseNotFound(f"Рецепт для '{dish}' не найден.")

    if servings:
        try:
            servings = int(servings)
            if servings <= 0:
                context = {'error_message': "Количество порций должно быть положительным числом."}
                return render(request, 'calculator/index.html', context) # Use template for error
            recipe = {ingredient: float(amount) * servings for ingredient, amount in recipe_data.items()} # Convert to float
        except ValueError:
            context = {'error_message': "Количество порций должно быть целым числом."}
            return render(request, 'calculator/index.html', context) # Use template for error
    else:
        recipe = recipe_data

    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)
