from safenigeria.baseform import SignUpForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login


class UserCreationView(FormView):
    template_name = 'registration/user_creation_form.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()

        # retrieve account creation credential and login user
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)