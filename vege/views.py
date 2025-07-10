from django.shortcuts import render, redirect, get_object_or_404
from .models import recepi

def vege(request):
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        recepi.objects.create(
            recepi_name=recipe_name,
            recepi_description=recipe_description,
            recepi_image=recipe_image,
        )
        return redirect('vege')

    queryset = recepi.objects.all()
    return render(request, "recepi.html", {"recipes": queryset})


def update_recepi(request, id):
    recipe = get_object_or_404(recepi, id=id)

    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe.recepi_name = recipe_name
        recipe.recepi_description = recipe_description

        if recipe_image:
            recipe.recepi_image = recipe_image

        recipe.save()
        return redirect('vege')

    return render(request, "update_recepi.html", {"recepi": recipe})


def dltrec(request, id):
    recipe = get_object_or_404(recepi, id=id)
    recipe.delete()
    return redirect('vege')
