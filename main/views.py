from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from .models import New
from .forms import PostForm
from django.conf import  settings
from django.utils.translation import gettext_lazy as _

def main_index(request):
    request.page_title = _('Bosh sahifa')

    request.breadcrumb = [
        request.page_title
    ]
    settings.LANGUAGE_CODE = request.COOKIES.get('lang')

    return render(request, "main/main.html", {
        "object_list": New.objects.all()
    }
    )


def main_add_post(request):
    request.page_title = _('Add')
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()


            messages.success(request, _("Maqola qo'shildi"))

            return redirect('main:main')
    
    return render(request, 'main/add-post.html',{
        'form': form
    })


def main_delete_post(request, id):

    New.objects.filter(id=id).delete()

    messages.success(request, _("Muvaffaqiyatli o'chirildi"))
    return redirect('main:main')


def main_view_post(request, id):
    request.page_title = _('Cars')
    post = New.objects.get(id=id)
    request.page_title = post.subject

    request.breadcrumb = [
        [post.subject]
    ]
    return render(request, 'main/view.html',{
        'post': post,
    })
