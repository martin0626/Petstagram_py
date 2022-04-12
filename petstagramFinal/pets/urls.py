from django.urls import path
from petstagramFinal.pets.views import like_pet, edit_pet, del_photo, make_comment, \
    AllPetsView, PetDetails, CreatePetView

urlpatterns = [
    path('pets/', AllPetsView.as_view(), name='pets list'),
    path('details/<int:pk>', PetDetails.as_view(), name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('pets/create/', CreatePetView.as_view(), name='create'),
    path('pets/edit/<int:pk>', edit_pet, name='edit'),
    path('pets/delete/<int:pk>', del_photo, name='delete'),
    path('pets/comment/<int:pk>', make_comment, name='comment'),

]

