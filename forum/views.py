from django.shortcuts import render
from .models import Topic, Message
from .forms import CommentForm

def index(request):
    TOPIC_LIST = Topic.objects.all()
    context = {
        "topics": TOPIC_LIST
    }
    return render(request, "forum/index.html", context)


def forum(request, topic):
    topic = Topic.objects.get(name=topic)
    messages = Message.objects.filter(topic=topic).order_by("created_at")
       
    if request.method == "POST":

        if "comment" in request.POST:

            # データの作成１
            # forms.pyを導入した場合のデータを作成するやり方
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():

                message_id = request.POST["comment"]
                message = Message.objects.get(id=message_id)

                comment_form.instance.message = message
                comment_form.save()

        elif "message" in request.POST:
            
            # データの作成２
            # これまで扱っていた
            # モデルに対してcreateメソッドを使用してデータを作成するやり方
            message = request.POST["message"]
            Message.objects.create(
                topic=topic,
                content=message,
            )

    comment_form = CommentForm()

    context = {
        "messages": messages,
        "topic": topic,
        "comment_form": comment_form,
    }
    return render(request, "forum/forum.html", context)