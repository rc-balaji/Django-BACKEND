from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),  # Endpoint for user registration
    # Add more endpoints as needed,
    path("login", views.login, name="login"),
    path("admin-register", views.admin_register, name="admin-register"),
    #    TP-1
    path("api/users/<str:user_id>", views.get_user, name="get_user"),
    path("api/users/<str:user_id>/update", views.update_user, name="update_user"),
    path("dashboard-stats", views.dashboard_stats, name="dashboard-stats"),
    # TP-1
    path("get-subadmins", views.get_subadmins, name="get_subadmins"),
    path("edit-subadmin/<str:id>", views.edit_subadmin, name="edit_subadmin"),
    path("delete-subadmin/<str:id>", views.delete_subadmin, name="delete_subadmin"),
    path("topic", views.get_topics, name="get_topics"),
    path("topic/<str:id>", views.organize_topic, name="organize_topic"),
    path("add/topic", views.add_topic, name="add_topic"),
    path("add/topic/<str:topic_id>/subtopics", views.add_subtopic, name="add_subtopic"),
    path(
        "add/topic/<str:topic_id>/subtopics/<str:subtopic_id>",
        views.add_title,
        name="add_title",
    ),
    path("subtopics", views.get_subtopics, name="get_subtopics"),
    path(
        "topics/<str:topic_id>/subtopics/<str:subtopic_id>",
        views.organize_subtopic,
        name="organize_subtopic",
    ),
    path("title", views.get_titles, name="get_titles"),
    path("get-title", views.get_title, name="get_title"),
    path("add/questions", views.add_question, name="add_question"),
    path("questions/<str:title_id>", views.get_question, name="get_question"),
    path("download-sample", views.download_sample, name="download_sample"),
    path(
        "add/questions/import", views.add_questions_import, name="add_questions_import"
    ),
    path("contents", views.manage_content, name="manage_content"),
    path("users", views.get_users_by_role, name="get_users_by_role"),
    path("user-topics", views.get_user_topics, name="get_user_topics"),
    path("allocate", views.allocate_topics, name="allocate_topics"),
    path(
        "attempts/<str:user_id>/<str:title_id>",
        views.get_attempts,
        name="get_attempts",
    ),
    path(
        "test-history/<str:user_id>",
        views.get_test_history_by_user,
        name="get_test_history_by_user",
    ),
    path(
        "test-history/<str:user_id>/<str:test_id>",
        views.get_test_history_by_user_and_test,
        name="get_test_history_by_user_and_test",
    ),
    path("api/questions/count", views.get_question_count, name="get_question_count"),
    path("save-result", views.finish_test, name="finish-test"),
    path("title/<str:id>", views.organize_title, name="organize-title"),
    path("update/questions", views.update_question, name="update_question"),
    path("delete/questions", views.delete_question, name="delete_question"),
]
