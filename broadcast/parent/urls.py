from django.urls import path, include
from parent.views import parent_dashboard, parentUseen, messageView, filedownload, pdfview, parentSeen, oldmessageView

urlpatterns = [
    path('dashboard/', parent_dashboard),
    path('unseen/', parentUseen),
    path('message/<int:id>', messageView),
    path('download/<int:id>', filedownload),
    path('view/<int:id>', pdfview),
    path('seen/', parentSeen),
    path('oldmessage/<int:id>', oldmessageView),
]