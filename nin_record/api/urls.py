from django.urls import path

from nin_record.api.views import GuardianDetail, GuardianList, NINReportList, NINReportDetail, NextOfKinDetail, NextOfKinList, ParentDetail, ParentList, SupportingDocumentDetail, SupportingDocumentList

urlpatterns = [
    path('nin/record/', NINReportList.as_view()),
    path('nin/record/<str:pk>/', NINReportDetail.as_view()),

    path('document/', SupportingDocumentList.as_view()),
    path('document/<str:pk>/', SupportingDocumentDetail.as_view()),

    path('parent/', ParentList.as_view()),
    path('parent/<str:pk>/', ParentDetail.as_view()),

    path('guardian/', GuardianList.as_view()),
    path('guardian/<str:pk>/', GuardianDetail.as_view()),

    path('nok/', NextOfKinList.as_view()),
    path('nok/<str:pk>/', NextOfKinDetail.as_view()),
]