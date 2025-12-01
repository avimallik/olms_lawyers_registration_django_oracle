from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json


@csrf_exempt
def insert_test_input(request):
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)
    
    print("CONTENT_TYPE =", request.content_type)
    print("RAW BODY    =", request.body)
    
    data = None

    if request.content_type == 'application/json':
        try:
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)
        except json.JSONDecodeError as e:
            return JsonResponse(
                {
                    'error': 'send right JSON',
                    'details': str(e)
                },
                status=400
            )
    else:
      
        data = request.POST

    # The objects after post execution
    name = data.get('name')
    phone = data.get('phone')

    if not name or not phone:
        return JsonResponse(
            {
                'error': 'Field is empty!',
            },
            status=400
        )

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO TBL_TEST (NAME, PHONE)
                VALUES (:name, :phone)
                """, {
                 'name': name, 
                 'phone': phone
                 }
            )

        return JsonResponse(
            {
                'message': 'Data posted successfully',
                'data': {
                    'name': name,
                    'phone': phone
                }
            },
            status=201
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
