from email.policy import default
from django.shortcuts import render 
from testing.models import Testing as t1
from django.shortcuts import HttpResponse as hr
import pymongo 
from django.conf import settings
connect_string="mongodb://localhost:27017";
my_client = pymongo.MongoClient(connect_string)
dbname = my_client["demodatabase"]
collection=dbname["testing_testing"]
def index(request):
    # collection.update({"name":"gopal"},{"age":21})
    a=collection.find({"name":"yesh aggarwal"})
    for i in a:
        print(i)
    collection.update({"name": "yesh aggarwal"},{"id":520,"name":"yesh aggarwal","age":29,"email":"gopaljha11321@gmail.com","number":"9871436400"})
    # a=collection.find({"name":"gopal"});
   
    return render(request,"index.html");
def thanks(request):
    id_number=request.POST.get('id','default');
    name=request.POST.get('name','default');
    age=request.POST.get('age','default');
    email=request.POST.get('email','default');
    number=request.POST.get('number','default');
    print(id_number,name,age,email,number);
    count_ele=collection.find({"id":id_number}).count();

    if count_ele==0:
        dis={
            "id":id_number,
            "name":name,
            "age":age,
            "email":email,
            "number":number
        }
        collection.insert(dis)
    else:
        collection.update({"name":name},{"id":id_number,"name":name,"age":age,"email":email,"number":number})

    return hr("<h1>Thanks for contecting!!</h1>");
def delete(request):
    id_number=request.POST.get('id','default');
    if (collection.find({"id":id_number}).count()) >0:
        collection.remove({"id":id_number});
    else:
        return hr("<h1> Data not founded</h1>")
    return hr("<h1> Data deleted</h1>");