from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "Ledger Admin"
admin.site.site_title="Welcome to Dashboard"
admin.site.index_title="Welcome to the Portal"
urlpatterns = [
    path("",views.home,name='/'),
    path("home",views.home,name='home'),
    path("history",views.history, name="history"),
    path("transaction",views.add_transaction,name="transaction"),
    path("group",views.show_groups,name='show_group'),
    path("create_group",views.group,name='create_group'),
    path("signup",views.handle_signup,name='signup'),
    path("login",views.handle_login,name='login'),
    path("logout",views.handle_logout,name='logout'),
    path("group_history/<str:slug>",views.group_history,name='group history'),
    path("calculate",views.calculate,name="calculate")
]
