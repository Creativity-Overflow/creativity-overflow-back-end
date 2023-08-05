# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Art


# class ArtListView(LoginRequiredMixin, ListView):
#     template_name = "Arts/art_list.html"
#     model = Art
#     context_object_name = "Arts"


# class ArtDetailView(LoginRequiredMixin, DetailView):
#     template_name = "Arts/art_detail.html"
#     model = Art


# class ArtUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = "Arts/art_update.html"
#     model = Art
#     fields = "__all__"


# class ArtCreateView(LoginRequiredMixin, CreateView):
#     template_name = "Arts/art_create.html"
#     model = Art
#     fields = "__all__" # "__all__" for all of them


# class ArtDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = "Arts/art_delete.html"
#     model = Art
#     success_url = reverse_lazy("art_list")
