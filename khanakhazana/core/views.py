from django.shortcuts import render

# Create your views here.

def home(request):
    context = [
        {'name': 'Chicken_Biryani', 'description': 'Traditional Pakistani spicy rice dish cooked with tender chicken and aromatic spices', 'price': '$12', 'image': 'https://images.unsplash.com/photo-1604908176997-4313d7accb43'},
        {'name': 'Beef Karahi', 'description': 'Rich and flavorful beef cooked with tomatoes, garlic and traditional spices.', 'price': '$15', 'image': 'https://images.unsplash.com/photo-1604908176997-4313d7accb43'},
        {'name': 'Chicken Tikka', 'description': 'Juicy grilled chicken marinated with yogurt and traditional BBQ spices.', 'price': '$10', 'image': 'https://images.unsplash.com/photo-1604908176997-4313d7accb43'},
        {'name': 'Seekh Kebab', 'description': 'Minced meat kebabs grilled on charcoal with authentic desi flavor.', 'price': '$9', 'image': 'https://images.unsplash.com/photo-1604908176997-4313d7accb43'},
        {'name': 'Butter Chicken', 'description': 'Creamy tomato curry cooked with soft chicken and rich butter flavor.', 'price': '$13', 'image': 'https://images.unsplash.com/photo-1604908176997-4313d7accb43'},
        {'name': 'Chapli Kebab', 'description': 'Famous Peshawari style kebab made with minced beef and special spices.', 'price': '$11', 'image': 'https://images.unsplash.com/photo-1604908176997-4313d7accb43'}
    ]
    return render(request, 'core/home.html', {"context": context})

def about(request):
    return render(request, 'core/about.html')

def footer(request):
    return render(request, 'core/footer.html')