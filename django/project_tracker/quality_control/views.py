from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'quality_control/index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

def bug_list(request):
    bugreports = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugreports})

class BugReportsListView(ListView):
    model = BugReport
    context_object_name = 'bug_list'
    template_name = 'quality_control/bug_list.html'

def feature_list(request):
    featurerequests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': featurerequests})

class FeatureRequestsListView(ListView):
    model = FeatureRequest
    context_object_name = 'feature_list'
    template_name = 'quality_control/feature_list.html'

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'

def feature_detail(request, feature_id):
    featurerequest = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': featurerequest})

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'

from .forms import BugReportForm, FeatureRequestForm

def create_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def create_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})
