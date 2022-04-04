import csv, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wesop.settings")
django.setup()

from products.models import *

# with open('categories.csv') as in_file:
#     data_reader = csv.reader(in_file, delimiter = ':')
#     next(data_reader, None)

#     for row in data_reader:
#         if row[0]:
#             category_name    = row[1]
#             main_description = row[2]
#             sub_description  = row[3]

#             Category.objects.create(
#                 category_name    = category_name,
#                 main_description = main_description,
#                 sub_description  = sub_description
#             )


# with open('products.csv') as in_file:

#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)

#     for row in data_reader:
#         if row[0]:
#             name        = row[3]
#             price       = row[4]
#             size        = row[5]
#             description = row[6]
#             feeling     = row[7]
#             howtouse    = row[8]
#             badge       = row[9]
#             category_id = row[10]
            
#             Product.objects.create(
#                 name        = name,
#                 price       = price,
#                 size        = size,
#                 description = description,
#                 feeling     = feeling,
#                 howtouse    = howtouse,
#                 category_id = category_id,
#                 badge       = badge
#             )



# with open('skintypes.csv') as in_file:
#     data_reader = csv.reader(in_file, delimiter = ':')
#     next(data_reader, None)

#     for row in data_reader:
#         if row[0]:
#             skin_type = row[1]

#             SkinType.objects.create(
#                 skin_type = skin_type
#             )




# with open('product_skintypes.csv') as in_file:

#     data_reader = csv.reader(in_file, delimiter = ':')
#     next(data_reader, None)

#     for row in data_reader:
#         if row[0]:
#             product_id = row[1]
#             skint_type_id = row[2]

#             ProductSkintype.objects.create(
#                 product_id=product_id,
#                 skin_type_id=skint_type_id
#             )


# with open('ingredients.csv') as in_file:
#     data_reader = csv.reader(in_file, delimiter = ':')
#     next(data_reader, None)

#     for row in data_reader:
#         if row[0]:
#             ingredients = row[1]

#             Ingredient.objects.create(
#                 ingredients=ingredients
#             )



# with open('product_ingredients.csv') as in_file:
#     data_reader = csv.reader(in_file, delimiter = ':')
#     next(data_reader, None)

#     for row in data_reader:
#         squence = row[0]
#         ingredient_id = row[1]
#         product_id = row[2]

#         ProductIngredient.objects.create(
#             squence=squence,
#             ingredient_id=ingredient_id,
#             product_id=product_id
#         )


# with open('product_images.csv') as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)

#     for row in data_reader:
#         product_id = row[1]
#         image_url = row[2]

#         ProductImage.objects.create(
#             product_id=product_id,
#             image_url=image_url
#         )