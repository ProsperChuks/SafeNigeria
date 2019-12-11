from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView


from safenigeria.baseform import SignUpForm


def change_password(request):
    """
    handles password changing functionality.
    """
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)  # Important!
        messages.success(request, 'Your password was successfully updated!')
        return redirect('change_password')
    else:
        messages.error(request, 'Please correct the error below.')
    return redirect('profile')




class UserCreationView(FormView):
    """
    handles user creation
    """
    template_name = 'registration/user_creation_form.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        """
        integrating additional processing to a valid form
        """
        form.save()

        # retrieve account creation credential and login user
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    """
    displays a user profile page
    """
    model = get_user_model()
    context_object_name = 'form'
    template_name = 'profile.html'
    fields = ('email', 'first_name', 'last_name')


    def get_context_data(self, **kwargs):
        """
        including important features to response object
        rendering profile page
        """
        context = super().get_context_data(**kwargs)
        context['password_form'] = PasswordChangeForm()
        return context