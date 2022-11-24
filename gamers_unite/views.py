from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post, Profile
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        profile = get_object_or_404(Profile, id=post.author_id)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        followed = False
        if profile.following.filter(id=self.request.user.id).exists():
            followed = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
                "following": followed
            },
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=id)
        profile = get_object_or_404(Profile, id=post.author_id)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        followed = False
        if profile.following.filter(id=self.request.user.id).exists():
            followed = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.creator_id = request.user.id
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
                "comment_form": CommentForm(),
                "following": followed
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
        new_post = PostForm(request.POST, request.FILES)

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
        return redirect('post_detail', id)


class EditComment(View):

    def get(self, request, id, comment_id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        query = Comment.objects.filter(approved=True)
        post = get_object_or_404(queryset, id=id)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment = get_object_or_404(query, id=comment_id)
        if comment.creator_id == self.request.user.id:
            edit_comment = CommentForm(instance=comment)
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True

            return render(
                request,
                "edit_comment.html",
                {
                    "post": post,
                    "comments": comments,
                    "liked": liked,
                    "comment_form": edit_comment
                },
            )
        else:
            return redirect('post_detail', id)

    def post(self, request, id, comment_id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        query = Comment.objects.filter(approved=True)
        post = get_object_or_404(queryset, id=id)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment = get_object_or_404(query, id=comment_id)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
        else:
            comment_form = CommentForm()

        return redirect('post_detail', id)


class Delete(View):
    def get(self, request, id, comment_id, model):
        if model == 'Post':
            post = get_object_or_404(Post, id=id)
            if post.author_id == self.request.user.id:
                post.delete()
            return redirect('home')
        elif model == 'Comment':
            comment = get_object_or_404(Comment, id=comment_id)
            if comment.creator_id == self.request.user.id:
                comment.delete()
            return redirect('post_detail', id)


class FollowUser(View):

    def post(self, request, id, post_id):
        user = get_object_or_404(Profile, user=id)

        if user.following.filter(id=request.user.id).exists():
            user.following.remove(request.user)
            is_following = False
        else:
            user.following.add(request.user)
            is_following = True
        return HttpResponseRedirect(reverse('post_detail', args=[post_id]))
