from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404

from.forms import CommentForm,ReplyForm,Reply,Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from rest_framework.response import Response
from serialisers import CommentSerializer, ReplySerializer
from .models import  Comment, Reply
from rest_framework import viewsets
from  rest_framework.decorators import detail_route, list_route






def post_comment(request):

    comments = Comment.objects.order_by("-id")
    form1 = CommentForm()
    form2 = ReplyForm()
    com_id=None
    if request.method == "POST":
        print request.POST['type']
        if request.POST['type'] =="comment":
            form1 = CommentForm(request.POST)
            if form1.is_valid():
                comment = form1.save(commit=False)
                comment.save()
                redirect('/comments/')
        else:
             form2 = ReplyForm(request.POST)
             if form2.is_valid():

                  reply = form2.save(commit=False)
                  reply.save()
                  redirect('/comments/')




    else:
        form1 = CommentForm()
        form2 = ReplyForm()
    return render(request, 'index.html', {'form1':form1,'form2':form2, "comments":comments})



def add_like(request):

    com_id=None

    if request.method == 'GET':

        com_id = request.GET['comment_id']



    like = 0

    if com_id:
        comments = Comment.objects.get(id=(int(com_id)))

        if comments:

            like = comments.like + 1
            comments.like = like
            comments.save()

    return HttpResponse(like)




class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @list_route(methods=['GET'])
    def comment_with_resp_reply(self, request):
        comment = Comment.objects.all()
        data = []
        for i in comment:
            d = {}
            d["id"] = i.id
            d["comment"] = i.comment
            reply=i.reply_set.all()
            rep = ReplySerializer(reply, many=True)
            d["reply"] = rep.data
            data.append(d)
        return Response(data)



class ReplyViewSet(viewsets.ModelViewSet):

    serializer_class = ReplySerializer
    queryset = Reply.objects.all()








