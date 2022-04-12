from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from petstagramFinal.accounts.models import UserProfile
from petstagramFinal.pets.forms import PetForm, CommentsForm, EditForm
from petstagramFinal.pets.models import Pet, Like, Comment


class AllPetsView(ListView):
    template_name = 'pets/pet_list.html'
    model = Pet
    context_object_name = 'Pets'


class PetDetails(DetailView):
    template_name = 'pets/pet_detail.html'
    model = Pet
    context_object_name = 'Pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentsForm()
        comments = Comment.objects.filter(pet_id=self.object.pk)
        owner = User.objects.get(pk=self.object.user_id)
        is_liked = Like.objects.filter(
            user_id=self.request.user.id,
            pet_id=self.object.id,
        )
        likes_count = len(list(Like.objects.filter(pet_id=self.object.id)))
        context.update(
            {
                'form': form,
                "comments": comments,
                "owner": owner,
                'is_liked': is_liked,
                'likes_count':likes_count
            }
        )
        return context


class CreatePetView(CreateView):
    template_name = 'pets/pet_create.html'
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('pets list')

    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(user_id=self.request.user.id)
        return super().form_valid(form)


def make_comment(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentsForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
            user_id=request.user.id
        )
        comment.save()

    return redirect('pet details', pk)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    is_liked = Like.objects.filter(
        user_id=request.user.id,
        pet_id=pet.id,
    )

    if is_liked:
        list(is_liked)[0].delete()
    else:
        like = Like(pet_id=pet.id, user_id=request.user.id)
        like.save()

    return redirect('pet details', pet.id)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets list')
    context = {
        'form': EditForm(
            initial=pet.__dict__
        ),
    }

    return render(request, 'pets/pet_edit.html', context)


def del_photo(request, pk):

    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        pet.delete()
        return redirect('pets list')

    return render(request, 'pets/pet_delete.html')
