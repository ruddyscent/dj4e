from cats.forms import BreedForm
from cats.models import Breed, Cat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cl = Cat.objects.all()
        bc = Breed.objects.all().count()

        ctx = {"breed_count": bc, "cat_list": cl}
        return render(request, "cats/cat_list.html", ctx)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        cc = Cat.objects.all().count()

        ctx = {"cat_count": cc, "breed_list": bl}
        return render(request, "cats/breed_list.html", ctx)


class BreedCreate(LoginRequiredMixin, View):
    template = "cats/breed_form.html"
    success_url = reverse_lazy("cats:all")

    def get(self, request):
        form = BreedForm()
        ctx = {"form": form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy("cats:all")
    template = "cats/breed_form.html"

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {"form": form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy("cats:all")
    template = "cats/breed_confirm_delete.html"

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {"breed": breed}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")
