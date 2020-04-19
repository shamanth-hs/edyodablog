from django.shortcuts import render
from accounts.forms import SignUpForm,BioClass
from django.views.generic import CreateView,UpdateView
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

class UserCreateView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpForm
    success_url ="/accounts/login"

class AuthorCreateView(LoginRequiredMixin,UpdateView):
    template_name = "account/bio.html"
    model = Profile
    # user = User.objects.get(id = )
    # queryset = Profile.user.get()
    success_url = "/blogs"
    # form_class = BioClass
    fields = ["bio","image"]


    def get_queryset(self):
        print(self.__dict__)
        # self.category = get(Category, name=self.kwargs['category'])
        self.user = User.objects.get(id =self.kwargs['pk'])
        print(self.user)
        self.profile = Profile.objects.filter(user = self.user )
        for profile in self.profile:
            print(profile.id)
        return self.profile
