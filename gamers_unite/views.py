from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class NewPost(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request,
            'new_post.html',
            {
                'new_post': PostForm(),
            },
        )

    def post(self, request):
        new_post = PostForm(request.POST)

        if new_post.is_valid():
            new_post.instance.email = request.user.email
            new_post.instance.name = request.user.username
            new_post.instance.author_id = request.user.id
            new_post.save()
        else:
            new_post = PostForm()

        return redirect('home')


class PostLike(View):

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[id]))


class EditPost(View, LoginRequiredMixin):

    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        if post.author_id == self.request.user.id:
            orginal_post = PostForm(instance=post)
            return render(
                request,
                'edit_post.html',
                {
                    'post': orginal_post,
                },
            )
        else:
            return redirect('home')

    def post(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        if post.author_id == self.request.user.id:
            edited_post = PostForm(request.POST, request.FILES, instance=post)

            if edited_post.is_valid():
                edited_post.save()
            else:
                edited_post = PostForm(instance=post)
        return redirect('home')
