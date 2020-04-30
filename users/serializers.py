'''
Serializers allow complex data such as querysets and model instances to be converted to native Python 
datatypes that can then be easily rendered into JSON, XML or other content types. 
Serializers also provide deserialization, allowing parsed data to be converted back into complex types, 
after first validating the incoming data.

Serializing is changing the data from complex querysets from the DB to a form of data we can understand, 
like JSON or XML. Deserializing is reverting this process after validating the data we want to save to the DB.

We provide a Serializer class which gives you a powerful, generic way to control the output 
of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating 
serializers that deal with model instances and querysets.

Serialization in REST framework is a two-phase process:
1. Serializers marshal between complex types like model instances, and
python primitives.
2. The process of marshalling between python primitives and request and
response content is handled by parsers and renderers.

https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py
https://www.django-rest-framework.org/api-guide/serializers/
https://www.django-rest-framework.org/api-guide/fields/
https://www.django-rest-framework.org/api-guide/relations/
'''

# from django.contrib.auth.models import Group
# from django.contrib.auth.models import User
# from django.core.serializers import serialize
## from .models import CustomUser, UserInformation, Allergies_List, AllergyMapping, RecommendedFood
# from rest_framework import serializers
# class UserSerializer(serializers.ModelSerializer):
#     allergic_food = serializers.ListField(allow_empty=True, min_length=None, max_length=None)
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'username', 'first_name', 'last_name',
#                     'age', 'gender', 'height', 'weight', 'activity',
#                     'allergic_food']
#
# class RecommendedFoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecommendedFood
#         read_only_fields = ['recipe_id', 'recipe_name', 'marketing_description', 'allergen_attributes', 'dietary_attributes']
#         fields = ['recipe_id', 'recipe_name', 'marketing_description', 'allergen_attributes', 'dietary_attributes']
#
# class AllergyMappingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AllergyMapping
#         fields = ['milk','egg','peanut','tree_nut','soy','wheat',
#         'fish','shellfish','msg_monosodium_glutamate','high_fructose_corn_syrup_hfcs'
#         ,'mustard','celery','sesame','gluten','red_yellow_blue_dye','gluten_free_per_fda','non_gmo_claim']
#         read_only_fields = ['milk','egg','peanut','tree_nut','soy','wheat',
#         'fish','shellfish','msg_monosodium_glutamate','high_fructose_corn_syrup_hfcs'
#         ,'mustard','celery','sesame','gluten','red_yellow_blue_dye','gluten_free_per_fda','non_gmo_claim']
#
#
# class Allergies_ListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     allergy_id = serializers.CharField(max_length=256)
#     # class Meta:
#     #     model = Allergies_List
#     #     fields = ['id', 'allergy_id']
# class UserInformationSerializer(serializers.ModelSerializer):
#     target_calorie_intake = serializers.CharField()
#     height = serializers.CharField()
#     weight = serializers.CharField()
#     # zip_code = serializers.CharField()
#     # allergic_food = serializers.IntegerField()
#     # allergic_food = serializers.ReadOnlyField()
#     # track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')
#     class Meta:
#         model = UserInformation
#         fields = ['url','date_of_birth', 'height',
#                     'weight', 'gender', 'target_calorie_intake',
#                      'preferred_meal', 'allergic_food',
#                      'work_out_level', 'dietary_preferences',
#                       'health_history', 'preferred_breakfast_time',
##                       'preferred_lunch_time', 'preferred_dinner_time']
        # read_only_fields = ('date_created', 'date_modified')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
