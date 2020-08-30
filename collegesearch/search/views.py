from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from .models import College


def index(request):
    if 'term' in request.GET:
        college_name = College.objects.filter(Actual_Course_Name__icontains=request.GET.get('term'))
        college_list = list()
        for search in college_name:
            college_list.append(search.Actual_Course_Name)
        return JsonResponse(college_list, safe=False)

    return render(request, 'search/index.html')


def course_search(request):
    searchWord = request.POST.get('college', '')
    courses = College.objects.filter(Actual_Course_Name__startswith=searchWord)
    context = {
        "Course_Name": searchWord,
        "courses": courses,
    }
    return render(request, 'search/course_search.html', context)


def course_detail(request, name):
    try:
        course = College.objects.filter(Actual_Course_Name=name)
    except College.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return render(request, 'search/course_detail.html', {'course': course})
