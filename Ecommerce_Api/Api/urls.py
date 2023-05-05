from django.urls import path
from .views import ProductView, CategoryView,TransactsView,UserView, AuthenticationView, GroupsView, LogoutView, InvitationCodeView, RoleRequestsView

urlpatterns = [
    path('productos',ProductView.as_view({'get':'nested_list_products','post':'post_product'}), name='listOfProducts' ),
    path('productos/<int:pk>',ProductView.as_view({'get':'get_product', 'delete':'delete_product','put':'update_product'}), name='listOfProducts' ),
    path('categorias', CategoryView.as_view({'get':'nested_list_categories', 'post':'post_category'}), name='list_of_categories'),
    path('categorias/<int:pk>', CategoryView.as_view({'put': 'update_category', 'get':'get_category','delete':'destroy_category'}, name='Update_and_Get_Categorie')),
    path('groups', GroupsView.as_view({'get':'nested_list'}), name='Groups_list'),
    path('users',UserView.as_view({'get':'get_all_users','post':'post_user'}), name='List_Users'),
    path('rolechanges', RoleRequestsView.as_view({'get':'get_role_requests','post':'post_role_request',}), name='roleChanges'),
    path('users/authenticate',AuthenticationView.as_view(), name='Get_token'),
    path('users/logout',LogoutView.as_view(), name='logout'),
    path('users/<int:pk>', UserView.as_view({'get':'get_user','delete':'delete_user','put':'put_user_data'})),
    path('transacts',TransactsView.as_view({'get':'get_all_transacts','post':'post_transact'}), name='listOfTransacts'),
    path('transacts/<int:pk>',TransactsView.as_view({'delete':'delete_transact'}), name='individual_transact'),
    path('users/invitations', InvitationCodeView.as_view({'get':'get_invitation_codes','post':'post_invitation_code'}), name='invitation')
]