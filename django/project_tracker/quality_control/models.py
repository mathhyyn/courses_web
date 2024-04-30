from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )
    task =  models.ForeignKey(
        Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    
    PRIORITY_CHOICES = [
        (1, 'Высокий'),
        (2, 'Средний'),
        (3, 'Низкий'),
    ]
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3
    )

    def __str__(self):
        return self.title


class FeatureRequest(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task =  models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = [
        ('On_review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='On_review',
    )
    
    PRIORITY_CHOICES = [
        (1, 'Высокий'),
        (2, 'Средний'),
        (3, 'Низкий'),
    ]
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3
    )

    def __str__(self):
        return self.title