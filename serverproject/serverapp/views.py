from django.shortcuts import render

# Create your views here.
def perimeter(request):
    context = {}
    context['length']="0"
    context['width']="0"
    context['perimeter']="0"

    if request.method == 'POST':
        print("POST METHOD IS USED")
        length=request.POST.get("length",0)
        width=request.POST.get("width",0)
        print('Length=',length)

        print('Width=',width)

        length_num = int(length)
        width_num = int(width)
        perimeter=2*(length_num+width_num)
        context['length']=length
        context['width']=width
        context['perimeter']=perimeter
        print('Perimeter=',perimeter)

    return render(request,"serverapp/perimeter.html",context)

def cssstyle(request):
    return render(request, "serverapp/cssstyle.html")