from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    # path('bugs/add_bug/', views.create_bug, name='create_bug'),
    # path('features/add_feature/', views.create_feature, name='create_feature'),
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('feature/<int:feature_id>/update/', views.update_feature, name='update_feature'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugReportsListView.as_view(), name='bug_list'),
    path('features/', views.FeatureRequestsListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
    
    path('bugs/add_bug/', views.BugReportCreateView.as_view(), name='create_bug'),
    path('features/add_feature/', views.FeatureRequestCreateView.as_view(), name='create_feature'),

    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    path('feature/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    path('feature/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),
]