from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
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
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            user = form.user
            update_session_auth_hash(request, user)

            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials, enter correct details')
    return request.user.get_absolute_url()




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
class UserProfileView(UpdateView):
    """
    displays a user profile page
    """
    model = get_user_model()
    context_object_name = 'form'
    template_name = 'profile.html'
    fields = ('email', 'first_name', 'last_name')


    def get_success_url(self):
        return self.request.user.get_absolute_url()

    def get_context_data(self, **kwargs):
        """
        including important features to response object
        rendering profile page
        """
        context = super().get_context_data(**kwargs)
        context['password_form'] = PasswordChangeForm(user=self.request.user)
        return context