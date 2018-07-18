from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from industries.models import Category
from industries.serializers import CategorySerializer
from industries.models import Category
from rest_framework.decorators import authentication_classes, api_view, permission_classes
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from register.authentication import TokenAuthentication
from register.permissions import IsAuthenticated


@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def list_category(request):
    """
    List all categories, or create a new category.
    """
    
    if request.method == 'GET':
        filters = {'parent': None}
        q = request.GET.get('q', None)
        if q:
            filters['name__icontains'] = q
            # filters['name__unaccent__icontains'] = q //TODO: dont work :(

        categories = Category.objects.filter(**filters)
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            for category in data['industries']:
                create_category(category, None)

            return JsonResponse({"message": "ok"}, status=201)
        except:
            JsonResponse({"message": "Error"}, status=400)
    
def create_category(item, parent):
    category = Category.objects.create(name=item["name"], parent=parent)
    try:
        for item in item["children"]:
            create_category(item, category)
    except:
        # Not children found
        pass