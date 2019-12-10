from safenigeria.baseform import SignUpForm
from django.views.generic.edit import FormView


class UserCreationView(FormView):
    template_name = 'registration/user_creation_form.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)