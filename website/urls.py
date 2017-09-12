from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Section Page
    url(r'^page/(?P<position_id>.*?)/$', views.page,
        name='section_page'),

    # People page
    url(r'^people/$', views.people, name='people'),
    url(r'^people/(?P<username>.*?)/$', views.people_profile,
        name='people_profile'),

    # Research Page
    url(r'^research/$', views.research, name='research'),

    # Teaching Page
    url(r'^teaching/$', views.teaching, name='teaching'),

    # Publications Page
    url(r'^publications/$', views.publications, name='publications'),

    # News Page
    url(r'^news/$', views.news_page, name='news_page'),

    # Blog specific page
    url(r'^blog/(?P<slug>[^\.]+)/$', views.blog_post, name='blog_post'),

    # Events Page
    url(r'^events/$', views.events_page, name='events_page'),
    url(r'^events/(?P<slug>[^\.]+)/$', views.event_post, name='event_post'),

    # Honeycomb gallery
    url(r'^gallery/$', views.honeycomb, name='gallery'),

    # Admin Panel Dash Board
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # Admin Panel Login Page
    url(r'^dashboard/login/?$', views.dashboard_login, name='dashboard_login'),

    # Generic Add / Edit page
    url(r'^dashboard/(?P<model_name>.*?)/edit/(?P<model_id>.*?)/$',
        views.edit_page, name='edit_page'),
    url(r'^dashboard/(?P<model_name>.*?)/delete/(?P<model_id>.*?)/$',
        views.delete_page, name='delete_page'),

    # Section and Page Management
    url(r'^dashboard/sections/edit/(?P<section_type_requested>.*?)/(?P<position_id>.*?)/$',
        views.edit_website_section, name='edit_website_section'),
    url(r'^dashboard/sections/add/$',
        views.add_website_page, name='add_website_page'),
    url(r'^dashboard/sections/delete/(?P<position_id>.*?)/$',
        views.delete_website_page, name='delete_website_page'),
    url(r'^dashboard/sections/(?P<section_type_requested>.*?)/$',
        views.dashboard_sections, name='dashboard_sections'),

    # Blog Management
    url(r'^dashboard/blog/$', views.dashboard_blog, name='dashboard_blog'),

    # Publication Management
    url(r'^dashboard/publications/$', views.dashboard_publications, name='dashboard_publications'),
    url(r'^dashboard/publications/highlight/$', views.highlight_publications, name='highlight_publications'),

    # Teaching Management
    url(r'^dashboard/courses/$', views.dashboard_courses, name='dashboard_courses'),

    # Events Management
    url(r'^dashboard/events/$', views.dashboard_events, name='dashboard_events'),

    # Carousel Management
    url(r'^dashboard/carousel/$', views.dashboard_carousel,
        name='dashboard_carousel'),
    url(r'^dashboard/carousel/edit/(?P<carousel_image_id>.*?)/$',
        views.edit_carousel_image, name='edit_carousel_image'),
    url(r'^dashboard/carousel/add/$', views.add_carousel_image,
        name='add_carousel_image'),
    url(r'^dashboard/carousel/delete/(?P<carousel_image_id>.*?)/$',
        views.delete_carousel_image, name='delete_carousel_image'),

    # Profile Management
    url(r'^dashboard/profile/$', views.edit_profile, name='edit_profile'),

    # Team Management
    url(r'^dashboard/team/$', views.dashboard_team, name='dashboard_team'),

    # logout url
    url(r'^dashboard/logout/$', logout,
        {'next_page': reverse_lazy('index')}, name='dashboard_logout')

]
