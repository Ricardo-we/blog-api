from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Posts, PostComments
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from .serializers import PostsSerializer, UsersSerializer, PostCommentSerializer
from django.core.paginator import Paginator
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser])
def users(request, id=''):
    if(request.method == 'GET' and not id):
        user = Users.objects.all()
        serializer = UsersSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'GET' and id):
        user = Users.objects.filter(id=id).first()
        serializer = UsersSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'POST'):
        serializer = UsersSerializer(data=request.data)
        if(serializer.is_valid()):
            return JsonResponse(serializer.data, safe=False, status=204)
        else:
            return JsonResponse(serializer.errors, safe=False, status=400)

    elif(request.method == 'PUT'):
        user = Users.objects.get(id=id)
        serializer = UsersSerializer(user, data=request.data)
        if(serializer.is_valid()):
            return JsonResponse(serializer.data, safe=False, status=204)
        else:
            return JsonResponse(serializer.errors, safe=False, status=400)

    elif(request.method == 'DELETE'):
        user = Users.objects.get(id=id)
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['POST', 'GET'])
@parser_classes([MultiPartParser])
def check_user(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        gmail = request.POST.get('gmail')
        user = Users.objects.filter(username=username, password=password, gmail=gmail)

        if(user.exists()):
            return JsonResponse({'message': 'valid'}, safe=False, status=204)
        else:
            return JsonResponse({'message': 'invalid'}, safe=False, status=400)

    return HttpResponse('')

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser])
def posts(request, id='', username=''):
    if(request.method == 'GET' and not id):
        post = Posts.objects.all()
        if(request.GET.get('page')):
            page = request.GET.get('page')
            paginator = Paginator(post, 20)
            selected_page = paginator.get_page(page)
            serializer = PostsSerializer(selected_page, many=True)
            data = {
                'actual_page': page,
                'previous_page': selected_page.has_previous(),
                'next_page': selected_page.has_next(),
                'pages_amount': selected_page.paginator.num_pages,
                'data':serializer.data
            }
            return JsonResponse(data, safe=False)

        serializer = PostsSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'GET' and id):
        post = Posts.objects.filter(id=id).first();
        serializer = PostsSerializer(post);
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'GET' and username):
        username = Users.objects.get(username=username)
        post = Posts.objects.filter(author=username).all();
        serializer = PostsSerializer(post, many=True);
        return JsonResponse(serializer.data, safe=False)
    

    elif(request.method == 'POST'):
        author = Users.objects.get(username=request.POST.get('author'))
        image = request.FILES['image']
        heading = request.POST.get('heading')
        body = request.POST.get('body')
        post = Posts(author=author, image=image, heading=heading, body=body)
        post.save()
        return JsonResponse({'message': 'success'}, safe=False, status=204)
        
    elif(request.method == 'PUT'):
        post = Posts.objects.filter(id=id).first()

        if(request.GET.get('like')):
            like = request.GET.get('like')
            if(like == 'true'): 
                post.likes += 1
            elif(like == 'false' and post.likes > 0): 
                post.likes -= 1
            post.save()
            return JsonResponse({'likes': post.likes}, safe=False)
            
        if (request.FILES['image']): post.image = request.FILES['image']
        post.heading = request.data['heading']
        post.body = request.data['body']
        post.save()
        return JsonResponse({'message': 'success'})
        
    elif(request.method == 'DELETE'):
        post = Posts.objects.get(id=id)
        post.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser])
def post_comments(request, post_id=''):
    if(request.method == 'GET'):
        post = Posts.objects.get(id=post_id)
        comments = PostComments.objects.filter(post=post).all()
        serializer = PostCommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    elif(request.method == 'POST'):
        comment = request.POST.get('comment')
        post = Posts.objects.get(id=post_id)
        print(comment, post)
        try:
            new_comment = PostComments(post=post, comment=comment)
            new_comment.save()
        except: 
            print('err')
        return JsonResponse({'message': 'success'}, safe=False)

    elif(request.method == 'PUT'):
        comment_id = request.data['comment-id']
        comment = request.data['comment']
        old_comment = PostComments.objects.get(id=comment_id)
        old_comment.comment = comment
        old_comment.save()
        return JsonResponse({'message': 'success'}, safe=False)

    elif(request.method == 'DELETE'):
        comment_id = request.GET.get('comment-id')
        comment = PostComments.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({'message': 'success'}, safe=False)
