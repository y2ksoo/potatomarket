from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin

class LogOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "접근할 수 없습니다.")
        return redirect("home")

# class LogInOnlyView(UserPassesTestMixin):

    
