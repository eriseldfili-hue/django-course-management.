from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from .serializers import StudentSerializer, StudentCreateSerializer, StudentUpdateSerializer
from tct.pagination import TCTPagination
from .models import Student


class StudentListView(APIView):
   def get(self, request, pk):
       student = get_object_or_404(Student, pk=pk)
       serializer = StudentSerializer(student)
       return Response(serializer.data, status=status.HTTP_200_OK)


class StudentListFilteredView(APIView):
   def get(self, request):
       student = Student.objects.all()


       name = request.query_params.get("name")
       if name:
           student = student.filter(name__icontains=name)
           # same as below
           # student = Student.objects.filter(name=name)
       email = request.query_params.get("email")
       if email:
           student = student.filter(email=email)
           # same as below
           # student = Student.objects.filter(
           # email=email
           # )


       paginator = TCTPagination()
       paginated_students = paginator.paginate_queryset(student, request)
       serializer = StudentSerializer(paginated_students, many=True)
       return paginator.get_paginated_response(serializer.data)


class StudentCreateView(APIView):


   def post(self, request):
       serializer = StudentCreateSerializer(data=request.data)


       if serializer.is_valid():
           serializer.save()
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED
           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )


class StudentUpdateDeleteView(APIView):


   def put(self, request, pk):
       student = get_object_or_404(Student, pk=pk)
       serializer = StudentUpdateSerializer(student, data=request.data)


       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)


       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )


   def patch(self, request, pk):
       student = get_object_or_404(Student, pk=pk)
       serializer = StudentUpdateSerializer(
           student,
           data=request.data,
       )


       if serializer.is_valid():
           serializer.save()
           return Response(
               serializer.data,
               status=status.HTTP_200_OK
           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )


   def delete(self, request, pk):
       student = get_object_or_404(Student, pk=pk)
       if student.courses.exists():
           return Response(
               {
                   "error": "Cannot delete a student with an active course."
               },
               status=status.HTTP_400_BAD_REQUEST
           )


       student.delete()
       return Response(
           {"message": "Student deleted successfully"},
           status=status.HTTP_204_NO_CONTENT
       )
