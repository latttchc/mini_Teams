from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Message
from .forms import MessageForm

@login_required
def index(request, account_id):
    # アカウントIDでユーザーを取得
    user = get_object_or_404(User, account_id=account_id)
    messages = Message.objects.filter(member=user)  # そのユーザーのメッセージを取得

    params = {
        'title': 'User Messages',
        'message': 'Here are your messages',
        'data': messages,
        'user': user,  
    }
    return render(request, 'work/index.html', params)

@login_required
def edit(request, account_id, message_id):
    # account_idを使ってUserを取得
    user = get_object_or_404(User, account_id=account_id)
    obj = get_object_or_404(Message, id=message_id, member=user)  # userに関連するMessageを取得
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            # 編集後はindexページへリダイレクト
            return redirect('work:index', account_id=account_id)  
    else:
        form = MessageForm(instance=obj)
    params = {
        'title': 'EDIT',
        'id': message_id,
        'form': form,
    }
    return render(request, 'work/edit.html', params)


@login_required
def create(request, account_id):
    user = get_object_or_404(User, account_id=account_id)
    if request.method == 'POST':
        obj = Message(member=user)
        form = MessageForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('work:index', account_id=account_id)
    params = {
        'title': 'Create',
        'form': MessageForm(),
    }
    return render(request, 'work/create.html', params)

@login_required
def delete(request, account_id, message_id):
    # 削除対象のメッセージを取得
    message = get_object_or_404(Message, id=message_id, member__account_id=account_id)

    if request.method == 'POST':
        # POSTリクエストで削除を実行
        message.delete()
        return redirect('work:index', account_id=account_id)  # indexページにリダイレクト

    # GETリクエストの場合は確認画面を表示
    return render(request, 'work/delete.html', {'message': message})


@login_required
def all_index(request):
    message = Message.objects.all()
    params = {
        'title':'All View',
        'message':'All members message',
        'data':message,
    }
    return render(request, 'work/all_index.html', params)