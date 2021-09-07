from .models import *


# this menthod is used to update details of a cat
def update_cat_details(data, cat_id):
    # we get all the necessary data from request like this
    name = data.get('name', '')
    breed = data.get('breed', '')
    description = data.get('description', '')
    age = data.get('age', '')
    colour = data.get('colour', '')
    picture = data.get('picture', '')

    # we get the cat object model where updating is required
    cat_info = CatDetailModel.objects.get(id=cat_id)

    # if a certain field is provided we update it otherwise it just stays the same
    if len(name) != 0:
        cat_info.name = name
        cat_info.save(update_fields=['name'])
    if len(breed) != 0:
        cat_info.breed = breed
        cat_info.save(update_fields=['breed'])
    if len(description) != 0:
        cat_info.description = description
        cat_info.save(update_fields=['description'])
    if len(age) != 0:
        cat_info.age = age
        cat_info.save(update_fields=['age'])
    if len(colour) != 0:
        cat_info.colour = colour
        cat_info.save(update_fields=['colour'])
    if len(picture) != 0:
        cat_info.picture = picture
        cat_info.save(update_fields=['picture'])

    cat_info.save()