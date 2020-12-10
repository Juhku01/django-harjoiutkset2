from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':"HELLO IM FROM FIRSTAPP!"}
    return render(request, 'first_app/index.html',context=my_dict)

def users(request):


    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'appTwo/users.html',context=user_dict)
    