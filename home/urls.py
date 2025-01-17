from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name='users-home'),
    path('testing', testing, name='users-home'),
    # path('scrape/', scrape_jumia, name='scrape_jumia'),
    # path('delete_all_products/', delete_all_products, name='delete_all_products'),
    path('api/bonds/', get_table_7_data, name='get_table_7_data'),
    path('api/bills/', get_table_8_data, name='get_table_8_data'),
    path('api/cps/', get_table_9_data, name='get_table_9_data'),
    path('api/fgn_bond_futures/', get_table_12_data, name='get_table_12_data'),
    path('api/scrapengx/', scrapengx, name='scrapengx'),
    path('get_table_9a_data', get_table_9a_data, name='get_table_9a_data'),
    path('get_table_9a_datagain', get_table_9a_datagain, name='get_table_9a_datagain'),
    path('scrape-nafem/', get_nafem_closing_rate, name='scrape-nafem'),
    path('api/form-submission/', FormSubmissionView.as_view(), name='form_submission'),
    path('account-opening-submissions/', fetch_all_account_opening_submissions, name='fetch_all_submissions'),
    path('submissions/<int:id>/', fetch_account_opening_submission_by_id, name='fetch_submission_by_id'),

    ]