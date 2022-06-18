from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.indexbef,name='indexbef'),
	#path("indexaflogin/<str:i>/",views.indexaflogin,name='indexaflogin'),
    path("indexaflogin",views.indexaflogin,name='indexaflogin'),
	path("disease",views.disease,name='disease'),

	path("dashboard",views.dashboard,name='dashboard'),

	path("feedbacklog",views.feedbacklog,name='feedbacklog'),
	path("contactlog",views.contactlog,name='contactlog'),	

	path("feedbacklogout",views.feedbacklogout,name='feedbacklogout'),
	path("contactlogout",views.contactlogout,name='contactlogout'),	




	path("logout",views.logout,name='logout'),  
	path("about",views.about,name='about'),

	path("userform",views.userform,name='userform'),
    path("userformdies/<str:i>/",views.userformdies,name='userformdies'),
    path("dashdata/<str:i>/<str:j>/",views.dashdata,name='dashdata'),
	path("login_register",views.login_register,name='login_register'),
	path("handellogin",views.handellogin,name='handellogin'),
	path("handellogout",views.handellogout,name='handellogout'),
	

    path("Newdiet",views.userform,name='Newdiet'),
	path("Help",views.feedbacklog,name='Help'),
	path("data",views.data,name='data'),
	path("testfilter",views.testfilter,name='testfilter'),



]
