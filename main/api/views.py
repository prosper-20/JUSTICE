from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from main.models import Post
from .serializers import PostSerializer, UserRegistrationSerializer

@api_view(["GET", "POST"])
def api_home_view(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            new_post = serializer.save()
            data["Response"] = "Post has been created succesfully, Here's more info....."
            data["title"] = new_post.title
            data["content"] = new_post.content
            data["author"] = new_post.author.username
            data["date_posted"] = new_post.date_posted
            data["slug"] = new_post.slug
            return Response(data=data)



@api_view(["GET", "PUT", "DELETE"])
def api_detail_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        data = {}
        operation = post.delete()
        if operation:
            data["Response"] = "Post delete successful!"
        else:
            data["Response"] = "Post delete failed"
        return Response(data=data)


@api_view(["PUT"])
def api_update_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    

@api_view(["DELETE"])
def api_delete_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        data = {}
        operation = post.delete()
        if operation:
            data["Response"] = "Post delete successful!"
        else:
            data["Response"] = "Post delete failed"
        return Response(data=data)


@api_view(["POST"])
def api_create_view(request):
    user = User.objects.get(pk=1)
    post = Post(author=user)
    if request.method == "POST":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            data = {}
            new_post = serializer.save()
            data["Response"] = "Post has been created succesfully, Here's more info....."
            data["title"] = new_post.title
            data["content"] = new_post.content
            data["author"] = new_post.author.username
            data["date_posted"] = new_post.date_posted
            data["slug"] = new_post.slug
            return Response(data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def api_registration_view(request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["Response"] = "Successfully registered a new  user"
            data["email"] = user.email
            data["username"] = user.username
        else:
            data = serializer.errors
        return Response(data)

            


