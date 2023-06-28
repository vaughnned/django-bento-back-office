from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Appetizer, MainCourse, Dessert
from menu.form import AppForm, MainForm, DessertForm

# Create your views here.
menu = [
    {
        "type": "appetizer",
        "price": 6.99,
        "name": "Gyoza",
        "japanese_name": "餃子",
        "description": "Delicious pan-fried dumplings filled with seasoned ground pork and vegetables. Served with a tangy soy dipping sauce."
    },
    {
        "type": "appetizer",
        "price": 5.99,
        "name": "Edamame",
        "japanese_name": "枝豆",
        "description": "Steamed young soybeans lightly seasoned with sea salt. A classic and healthy Japanese appetizer."
    },
    {
        "type": "appetizer",
        "price": 7.99,
        "name": "Agedashi Tofu",
        "japanese_name": "揚げ出し豆腐",
        "description": "Deep-fried tofu served in a flavorful dashi broth with grated daikon, green onions, and bonito flakes."
    },
    {
        "type": "appetizer",
        "price": 8.99,
        "name": "Takoyaki",
        "japanese_name": "たこ焼き",
        "description": "Savory octopus-filled batter balls cooked to perfection and topped with takoyaki sauce, mayonnaise, and bonito flakes."
    },
    {
        "type": "main course",
        "price": 12.99,
        "name": "Teriyaki Chicken",
        "japanese_name": "照り焼きチキン",
        "description": "Grilled chicken marinated in a sweet and savory teriyaki sauce. Served with steamed rice and a side of mixed vegetables."
    },
    {
        "type": "main course",
        "price": 14.99,
        "name": "Sushi Platter",
        "japanese_name": "寿司盛り合わせ",
        "description": "A delightful assortment of fresh nigiri and maki sushi. Chef's selection may include tuna, salmon, shrimp, and vegetable rolls."
    },
    {
        "type": "main course",
        "price": 15.99,
        "name": "Beef Yakiniku",
        "japanese_name": "焼肉",
        "description": "Thinly sliced beef marinated in a flavorful soy-based sauce and grilled to perfection. Served with a side of rice and kimchi."
    },
    {
        "type": "main course",
        "price": 13.99,
        "name": "Vegetable Tempura",
        "japanese_name": "野菜天ぷら",
        "description": "Assorted lightly battered and deep-fried seasonal vegetables. Served with a dipping sauce and steamed rice."
    },
    {
        "type": "main course",
        "price": 11.99,
        "name": "Tonkatsu",
        "japanese_name": "とんかつ",
        "description": "Crispy breaded and deep-fried pork cutlet served with shredded cabbage, tonkatsu sauce, and steamed rice."
    },
    {
        "type": "main course",
        "price": 16.99,
        "name": "Unagi Don",
        "japanese_name": "鰻丼",
        "description": "Grilled freshwater eel glazed with a sweet soy-based sauce. Served over a bed of steamed rice and garnished with pickles."
    },
    {
        "type": "main course",
        "price": 18.99,
        "name": "Ramen",
        "japanese_name": "ラーメン",
        "description": "A comforting bowl of flavorful broth, ramen noodles, and various toppings such as chashu pork, bamboo shoots, and a soft-boiled egg."
    },
    {
        "type": "main course",
        "price": 12.99,
        "name": "Chicken Katsu Curry",
        "japanese_name": "チキンカツカレー",
        "description": "Deep-fried breaded chicken cutlet served with Japanese curry sauce and steamed rice. A perfect combination of crispy and savory flavors."
    },
    {
        "type": "main course",
        "price": 17.99,
        "name": "Sashimi Deluxe",
        "japanese_name": "刺身デラックス",
        "description": "A premium selection of fresh sashimi, including tuna, salmon, yellowtail, and octopus. Served with wasabi, soy sauce, and pickled ginger."
    },
    {
        "type": "dessert",
        "price": 6.99,
        "name": "Matcha Green Tea Ice Cream",
        "japanese_name": "抹茶アイスクリーム",
        "description": "Creamy and refreshing matcha green tea-flavored ice cream. A perfect ending to your Japanese meal."
    },
    {
        "type": "dessert",
        "price": 7.99,
        "name": "Mochi Ice Cream",
        "japanese_name": "もちアイスクリーム",
        "description": "Chewy mochi rice cake filled with various flavors of ice cream, such as strawberry, mango, and green tea."
    },
    {
        "type": "dessert",
        "price": 5.99,
        "name": "Dorayaki",
        "japanese_name": "どら焼き",
        "description": "Sweet red bean paste sandwiched between two fluffy pancakes. A popular traditional Japanese dessert."
    }
]


def home_page(request):
    return render(request, "home_page.html", {'menu': menu})


def item(request, index):
    item = menu[index]
    return render(request, 'item_description.html', {'item': item})


def appetizer_item(request, appetizer_item_id):
    appetizer_item = get_object_or_404(Appetizer, id=appetizer_item_id)
    return render(request, "seed_item.html", {"item": appetizer_item})


def main_item(request, main_item_id):
    main_item = get_object_or_404(MainCourse, id=main_item_id)
    return render(request, "seed_item.html", {"item": main_item})


def dessert_item(request, dessert_item_id):
    dessert_item = get_object_or_404(Dessert, id=dessert_item_id)
    return render(request, "seed_item.html", {"item": dessert_item})


def appetizer_records(request):
    app_record = Appetizer.objects.all()
    return render(request, 'back_office.html', {"app_records": app_record})


def delete_app(request, appetizer_record_id):
    appetizer_record = get_object_or_404(Appetizer, id=appetizer_record_id)

    if request.method == 'POST':
        appetizer_record.delete()
        return render(request, 'back_office.html', {"deleted_item": appetizer_record})
    else:
        return HttpResponseNotAllowed(['POST'])


def update_app(request, appetizer_record_id):
    appetizer_record = get_object_or_404(Appetizer, id=appetizer_record_id)

    if request.method == 'POST':
        form = AppForm(request.POST, instance=appetizer_record)
        if form.is_valid():
            form.save()
    else:
        form = AppForm(instance=appetizer_record)
    context = {
        'form': form,
        'app_list': Appetizer.objects.all()
    }
    return render(request, 'edit.html', context)


def create_app(request):

    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AppForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def main_records(request):
    main_record = MainCourse.objects.all()
    return render(request, 'back_office.html', {"main_records": main_record})


def delete_main(request, main_record_id):
    main_record = get_object_or_404(MainCourse, id=main_record_id)

    if request.method == 'POST':
        main_record.delete()
        return render(request, 'back_office.html', {"deleted_item": main_record})
    else:
        return HttpResponseNotAllowed(['POST'])


def update_main(request, main_record_id):
    main_record = get_object_or_404(MainCourse, id=main_record_id)

    if request.method == 'POST':
        form = MainForm(request.POST, instance=main_record)
        if form.is_valid():
            form.save()
    else:
        form = MainForm(instance=main_record)
    context = {
        'form': form,
        'main_list': MainCourse.objects.all()
    }
    return render(request, 'edit.html', context)


def create_main(request):

    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MainForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def dessert_records(request):
    dessert_record = Dessert.objects.all()
    return render(request, 'back_office.html', {"dessert_records": dessert_record})


def delete_dessert(request, dessert_record_id):
    dessert_record = get_object_or_404(Dessert, id=dessert_record_id)

    if request.method == 'POST':
        dessert_record.delete()
        # return redirect('')
        return render(request, 'back_office.html', {"deleted_item": dessert_record})
    else:
        return HttpResponseNotAllowed(['POST'])


def update_dessert(request, dessert_record_id):
    dessert_record = get_object_or_404(Dessert, id=dessert_record_id)

    if request.method == 'POST':
        form = DessertForm(request.POST, instance=dessert_record)
        if form.is_valid():
            form.save()
    else:
        form = DessertForm(instance=dessert_record)
    context = {
        'form': form,
        'dessert_list': Dessert.objects.all()
    }
    return render(request, 'edit.html', context)


def create_dessert(request):

    if request.method == 'POST':
        form = DessertForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DessertForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def seed(request):
    if not Appetizer.objects.exists():
        appetizers = [
            Appetizer(name="Gyoza", price=6.99,
                      description="Delicious pan-fried dumplings filled with seasoned ground pork and vegetables. Served with a tangy soy dipping sauce."),
            Appetizer(name="Edamame", price=5.99,
                      description="Steamed young soybeans lightly seasoned with sea salt. A classic and healthy Japanese appetizer."),
            Appetizer(name="Agedashi Tofu", price=7.99,
                      description="Deep-fried tofu served in a flavorful dashi broth with grated daikon, green onions, and bonito flakes."),
            Appetizer(name="Takoyaki", price=8.99,
                      description="Savory octopus-filled batter balls cooked to perfection and topped with takoyaki sauce, mayonnaise, and bonito flakes.")
        ]
        Appetizer.objects.bulk_create(appetizers)
    appetizer_list = Appetizer.objects.all()

    if not MainCourse.objects.exists():
        main_course = [
            MainCourse(name="Teriyaki Chicken", price=12.99,
                       description="Grilled chicken marinated in a sweet and savory teriyaki sauce. Served with steamed rice and a side of mixed vegetables."),
            MainCourse(name="Sushi Platter", price=14.99,
                       description="A delightful assortment of fresh nigiri and maki sushi. Chef's selection may include tuna, salmon, shrimp, and vegetable rolls."),
            MainCourse(name="Beef Yankiniku", price=15.99,
                       description="Thinly sliced beef marinated in a flavorful soy-based sauce and grilled to perfection. Served with a side of rice and kimchi."),
            MainCourse(name="Vegetable Tempura", price=13.99,
                       description="Assorted lightly battered and deep-fried seasonal vegetables. Served with a dipping sauce and steamed rice."),
            MainCourse(name="Tonkatsu", price=11.99,
                       description="Crispy breaded and deep-fried pork cutlet served with shredded cabbage, tonkatsu sauce, and steamed rice."),
            MainCourse(name="Unagi Don", price=16.99,
                       description="Grilled freshwater eel glazed with a sweet soy-based sauce. Served over a bed of steamed rice and garnished with pickles."),
            MainCourse(name="Ramen", price=18.99,
                       description="A comforting bowl of flavorful broth, ramen noodles, and various toppings such as chashu pork, bamboo shoots, and a soft-boiled egg."),
            MainCourse(name="Chicken Katsu Curry",
                       price=12.99, description="Deep-fried breaded chicken cutlet served with Japanese curry sauce and steamed rice. A perfect combination of crispy and savory flavors."),
            MainCourse(name="Sashimi Deluxe", price=17.99,
                       description="A premium selection of fresh sashimi, including tuna, salmon, yellowtail, and octopus. Served with wasabi, soy sauce, and pickled ginger."),
        ]
        MainCourse.objects.bulk_create(main_course)
    maincourseList = MainCourse.objects.all()

    if not Dessert.objects.exists():
        desserts = [
            Dessert(name="Matcha Green Tea Ice Cream",
                    price=6.99, description="Creamy and refreshing matcha green tea-flavored ice cream. A perfect ending to your Japanese meal."),
            Dessert(name="Mochi Ice Cream", price=7.99,
                    description="Chewy mochi rice cake filled with various flavors of ice cream, such as strawberry, mango, and green tea."),
            Dessert(name="Dorayaki", price=5.99,
                    description="Sweet red bean paste sandwiched between two fluffy pancakes. A popular traditional Japanese dessert."),
        ]
        Dessert.objects.bulk_create(desserts)
    dessertList = Dessert.objects.all()

    return render(request, 'seed.html', {'appetizers': appetizer_list, 'main_course': maincourseList, 'desserts': dessertList})
