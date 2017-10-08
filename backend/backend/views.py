# -*- coding: utf-8 -*-
import copy

from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView


class HealthCheckView(TemplateView):
    @never_cache
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'success'})
