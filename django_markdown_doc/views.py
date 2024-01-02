from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
from .forms import DocumentForm
from markdownx.utils import markdownify  # 导入markdownify函数
import yaml

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def document_detail(request, document_id):
    # document = get_object_or_404(Document, pk=document_id)
    # # return render(request, 'document_detail.html', {'document': document})
    # content_markdown = markdownify(document.content)  # 使用markdownify函数将Markdown文本转换为HTML
    # return render(request, 'document_detail.html',
    #               {'document': document, 'content_markdown': content_markdown})  # 将转换后的HTML内容传递给模板
    document = get_object_or_404(Document, pk=document_id)
    content_markdown = markdownify(document.content)  # 将Markdown格式内容转换为HTML
    yaml_data = yaml.safe_load(document.yaml_content)  # 使用PyYAML库解析YAML格式内容
    return render(request, 'document_detail.html',
                  {'document': document, 'content_markdown': content_markdown, 'yaml_data': yaml_data})

def document_new(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect('document_detail', document_id=document.pk)
    else:
        form = DocumentForm()
    return render(request, 'document_edit.html', {'form': form})

def document_edit(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            document = form.save()
            return redirect('document_detail', document_id=document.pk)
    else:
        form = DocumentForm(instance=document)
    return render(request, 'document_edit.html', {'form': form})

def document_delete(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.delete()
    return redirect('document_list')  # Assuming 'home' is the name of your homepage URL
