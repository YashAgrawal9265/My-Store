from django.shortcuts import render,HttpResponse
from shop.models import Product,Order,OrderUpdate
from math import ceil
import json
# Create your views here.

def index(request):
    # product = Product.objects.all()
    # product_length = len(product)
    # nslides = ceil(product_length/4)
    # # params = {'product':product,'range':range(1,nslides)}
    # allprod = [[product,range(1,nslides)],[product,range(1,nslides)]]
    allprod = []
    category = Product.objects.values('category')
    
    #list = [item['category'] for item in category]  # we cannot use list compherension because we want unique categoryies in list categories are repeating
    set = {item['category'] for item in category} 
    
    for cat in set:
        product = Product.objects.filter(category=cat)
        # print(product)
        prod_length = len(product)
        nslides = ceil(prod_length/4)
        allprod.append([product,range(1,nslides)])
    # for item in category:
    #     list.append(items['category'])
    params = {'allprod':allprod}
    return render(request,'shop/index.html',params)

# fucntion for checking search queries
def searchquery(query,item):
    if query in item. product_name.lower() or query in item.category.lower() or query in item.subcategory.lower() or query in item.desc.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprod = []
    category = Product.objects.values('category')
    set = {item['category'] for item in category} 
    
    for cat in set:
        product = Product.objects.filter(category=cat)
        prod = [item for item in product if searchquery(query,item)]
        prod_length = len(prod)
        nslides = ceil(prod_length/4) 
        if prod_length > 0:
            allprod.append([prod,range(1,nslides)])
        params = {'allprod':allprod,'message':""}
        if len(allprod) == 0 or len(query) < 3:
            params = {'message':'Please make sure to enter relevant search query'}
    return render(request,'shop/search.html',params)
        
    
    


def products(request,myid):
    product=Product.objects.filter(id=myid)
    param = {'product':product[0]}
    return render(request,'shop/products.html',param)
    
    
    # print(Product.objects.filter(id=myid))


def checkout(request):
    if request.method == "POST":
        itemJson = request.POST.get('itemJson')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address1')+" "+request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zipcode','')

        order = Order(itemJson=itemJson,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        orderupdate = OrderUpdate(order_id=order.order_id,order_desc="Your order has been received")
        orderupdate.save()
        thank = True
        
        return render(request,'shop/checkout.html',{'thank':thank,'id':order.order_id})
        

    return render(request,'shop/checkout.html')

def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('orderId')
        email = request.POST.get('email')
        try:
            order = Order.objects.filter(order_id=order_id,email=email)
            
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.order_desc,'timestamp':item.timestamp})
                response =  json.dumps([updates,order[0].itemJson],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
            
    return render(request,'shop/tracker.html')
    


