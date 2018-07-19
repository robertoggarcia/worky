from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CategorySerializer
from .models import Category
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from register.authentication import TokenAuthentication
from register.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def list_category(request):
    """
    Handle POST and GET request to create or list categories.
    :param request:
    :return: HTTP Response
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
        except KeyError:
            JsonResponse({"message": "Error"}, status=400)


def create_category(item, parent):
    """
    Create new category with parent
    :param item:
    :param parent:
    :return:
    """
    try:
        category = Category.objects.create(name=item["name"], parent=parent)
        try:
            for item in item["children"]:
                create_category(item, category)
        except KeyError:
            pass
    except category.IntegrityError:
        pass