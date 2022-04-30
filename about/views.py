from django.shortcuts import render
from django.views import View


class DescriptionView(View):
    template_name = 'about/description.html'
    context = {}

    def get(self, reqest):
        return render(reqest, self.template_name, self.context)
