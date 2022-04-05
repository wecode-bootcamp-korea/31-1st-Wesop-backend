import django
import csv, os,sys, json

os.chdir('.')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'wesop.settings')
django.setup()

from products.models import *

# with open('cores/csv/1_categories.csv') as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
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

# PATH = 'cores/csv/2_products.csv'
# with open(PATH) as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)
#     for row in data_reader:
#         if row[0]:
#             created_at  = row[1]
#             updated_at  = row[2]
#             name        = row[3]
#             price       = row[4]
#             size        = row[5]
#             description = row[6]
#             category_id = row[7]
#             howtouse    = json.loads(row[8].replace("'", "\""))
#             badge       = row[9]
            
#             Product.objects.create(
#                 created_at  = created_at,
#                 updated_at  = updated_at,
#                 name        = name,
#                 price       = price,
#                 size        = size,
#                 description = description,
#                 howtouse    = howtouse,
#                 category_id = category_id,
#                 badge       = badge
#             )

# PATH = 'cores/csv/3_skintypes.csv'
# with open(PATH) as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)
#     for row in data_reader:
#         if row[0]:
#             name = row[1]

#             SkinType.objects.create(
#                 name = name
#             )

# PATH = 'cores/csv/4_product_skintypes.csv'

# with open(PATH) as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)
#     for row in data_reader:
#         if row[0]:
#             product_id = row[1]
#             skint_type_id = row[2]

#             ProductSkintype.objects.create(
#                 product_id=product_id,
#                 skin_type_id=skint_type_id
#             )

# PATH = 'cores/csv/5_ingredients.csv'
# with open(PATH) as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)
#     for row in data_reader:
#         if row[0]:
#             name = row[1]
#             Ingredient.objects.create(
#                 name = name
#             )

# PATH = 'cores/csv/6_product_ingredients.csv'
# with open(PATH) as in_file:
#     data_reader = csv.reader(in_file, delimiter = ',')
#     next(data_reader, None)
#     for row in data_reader:
#         if row[0]:
#             ingredient_id = row[1]
#             product_id    = row[2]
#             major         = row[3]
#             ProductIngredient.objects.create(
#                 major         = major,
#                 ingredient_id = ingredient_id,
#                 product_id    = product_id
#             )