from django.urls import include, path
from . import views

urlpatterns = [
    # One time url
    path('share/download', views.file_download_by_otu, name='Download-file-by-OTU'),

    # APIs for interacting with clients.
    path('crash/upload', views.crash_upload, name='crash-upload-crash'),
    path('fuzzer/update_info', views.fuzzer_update_info, name='fuzzer-update-client'),
    path('fuzzer/ping', views.fuzzer_ping, name='fuzzer-ping'),
    path('storage/list', views.storage_list, name='storage-list'),
    path('storage/download', views.storage_download, name='storage-download'),

    # APIs for getting account's information
    path('fuzzer/list', views.get_fuzzer_list, name='get-fuzzer-list'),
    path('statistics', views.get_status_all, name='get-status-all'),
    path('fuzzer/create', views.create_fuzzer, name='create-fuzzer'),

]
