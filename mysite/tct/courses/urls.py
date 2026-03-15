from django.urls import path
from tct.courses.views import (
  CourseListView, CourseCreateView,
  CourseListFilteredView, CourseUpdateDeleteView, CourseEnrollView, CourseUnrollView, CourseBulkImportView, CourseCreateBulkView,
)

urlpatterns = [
  # course views
  path("course/<int:pk>", CourseListView.as_view(), name='course-list'),
  path("filter-course/", CourseListFilteredView.as_view(), name='course-list-filtered'),
  path("course-create", CourseCreateView.as_view(), name='course-create'),
  path("course-detail/<int:pk>", CourseUpdateDeleteView.as_view(), name='course-detail'),
  path("course/<int:pk>/enroll", CourseEnrollView.as_view(), name='enroll-student'),
  path("course/<int:pk>/unroll", CourseUnrollView.as_view(), name='unroll-student'),
  path("course-create-bulk", CourseBulkImportView.as_view(), name='course-create-bulk'),
  path("course-enroll-bulk", CourseCreateBulkView.as_view(), name='course-enroll-bulk'),
]