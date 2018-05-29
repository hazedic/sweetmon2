from django.urls import include, path
from . import views

urlpatterns = [
    # One time url
    path('share/download', views.crash_download_by_otu, name='Download-file-by-OTU'),

    # Internal API
    path('crash/<int:idx>/download', views.crash_download, name='crash-download-directly'),
    path('crash/<int:idx>/generate_url', views.crash_generate_url, name='crash-generate-OTU'),
    path('crash/<int:idx>/duplicated_list', views.crash_dup_crash_list, name='crash-duplicated-crash'),

    # API for interacting with clients.
    path('crash/upload', views.crash_upload, name='crash-upload-crash'),

    path('fuzzer/update_info', views.fuzzer_update_info, name='fuzzer-update-client'),
    path('fuzzer/ping', views.fuzzer_ping, name='fuzzer-ping'),

    path('storage/list', views.storage_list, name='storage-list'),
    path('storage/download', views.storage_download, name='storage-download'),
]