from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')

# def show_details(request,my_id):
#     print(my_id)
#     st={'id':my_id}
#     return render(request,'enroll/show.html',st)


def show_details(request,my_id):
    if my_id==1:
        st={'id':my_id,'name':'Rohan'}
    if my_id==2:
        st={'id':my_id,'name':'Sohan'}
    if my_id==3:
        st={'id':my_id,'name':'Sonam'}
    
    return render(request,'enroll/show.html',st)



def show_subdetails(request,my_id,my_subid):
    if my_id==1 and my_subid==5:
        st={'id':my_id,'name':'Rohan','info':'sub Details','ids':my_subid}
    if my_id==2 and my_subid==6:
        st={'id':my_id,'name':'Sohan','info':'sub Details','ids':my_subid}
    if my_id==3 and my_subid==7 :
        st={'id':my_id,'name':'Sonam','info':'sub Details','ids':my_subid}
    
    return render(request,'enroll/show.html',st)
