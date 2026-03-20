from django.urls import path, include
from tct.teacher.views import (
TeacherListView, TeacherListFilteredView, TeacherCreateView, TeacherUpdateDeleteView, TeacherBulkCreateView
)

from tct.student.views import (
StudentListView, StudentListFilteredView, StudentCreateView, StudentUpdateDeleteView
)

urlpatterns = [
  # course views
  path("courses/", include("tct.courses.urls")),

  # teacher views
  path("teacher/<int:pk>", TeacherListView.as_view(), name='teacher-list'),
  path("filter-teacher/", TeacherListFilteredView.as_view(), name='teacher-list-filtered'),
  path("teacher-create", TeacherCreateView.as_view(), name='teacher-create'),
  path("teacher-detail/<int:pk>", TeacherUpdateDeleteView.as_view(), name='teacher-detail'),
  path("teacher-create-bulk", TeacherBulkCreateView.as_view(), name='teacher-create-bulk'),


  # student views
  path("student/<int:pk>", StudentListView.as_view(), name='student-list'),
  path("filter-student/", StudentListFilteredView.as_view(), name='student-list-filtered'),
  path("student-create", StudentCreateView.as_view(), name='student-create'),
  path("student-detail/<int:pk>", StudentUpdateDeleteView.as_view(), name='student-detail'),
]