from django.urls import path
from .views import  ProductView,ReportView,SearchAPIView, ProductsDigitView,TransactSubcategoryView,WithDrawView, CategoryView,TransactsView,UserView, SolicCheckerView, AuthenticationView, GroupsView, LogoutView, InvitationCodeView, RoleRequestsView,Img_view

urlpatterns = [
    path('transactscategories',TransactSubcategoryView.as_view({'get':'get', 'post':'post'}),name="CheckerSOLIC"),
    path('seeker',SearchAPIView.as_view({'get':'get'}),name="busc"),
    path('inventory', ProductView.as_view({'get':'get_inventory'})),
    path('reports/<int:pkP>', ReportView.as_view({'post':'post_report'})),
    path('solicChecker',SolicCheckerView.as_view({'get':'get_solic_checker'},name="CheckerSOLIC")),
    path('solicChecker/<int:pk>',SolicCheckerView.as_view({'post':'post_solic_checker'},name="CheckerSOLIC")),
    path('images/<str:image_name>', Img_view.as_view({'get':'get_file_img'}), name="IMG_GET"),
    path('productos/digit', ProductsDigitView.as_view({'get':'get_digit_products','post':'post_product_digit'}, name="Digital_Products")),
    path('productos/digit/<int:pk>', ProductView.as_view({'get':'get_digit_product'}, name="Digistal_Products")),
    path('productos/digit/<int:pk>/<int:pkS>', ProductsDigitView.as_view({'put':'put_Product_state'}, name="Digistal_Products")),    
    path('productos/methods', ProductView.as_view({'get':'get_all_methods'}, name="MethodsRN")),
    path('productos/transacts/methods', TransactsView.as_view({ 'post':'post_new_transacts_method'}, name="MethodsRN")),
    path('productos/transacts/digits', TransactsView.as_view({ 'post':'post_transact_digits'}, name="CreateDigitTransact")),
    path('productos/methods/<int:pk>', ProductView.as_view({'get':'get_method'}, name="godHelpMe")),
    path('withdraws',WithDrawView.as_view({'get':'get_withdraws','post':'post_new_withdraw'}), name="Withdraws"),
    # path('productos/stores', StoresView.as_view({'get':'get_digit_products'}, name="Digital_Products")),
    path('productos',ProductView.as_view({'get':'nested_list_products','post':'post_product'}), name='listOfProducts' ),
    path('productos/<int:pk>',ProductView.as_view({'get':'get_product', 'delete':'delete_product','put':'update_product'}), name='listOfProducts' ),
    path('categorias', CategoryView.as_view({'get':'nested_list_categories', 'post':'post_category'}), name='list_of_categories'),
    path('categorias/<int:pk>', CategoryView.as_view({'put': 'update_category', 'post':'post_subCategorie','get':'get_category','delete':'destroy_category'}, name='Update_and_Get_Categorie')),
    path('categorias/<int:pk>/<int:subCat_id>', CategoryView.as_view({'put': 'update_subCategory', 'post':'post_subCategorie','delete':'delete_subCategory'}, name='Update_and_Get_Categorie')),
    path('groups', GroupsView.as_view({'get':'nested_list'}), name='Groups_list'),
    path('users',UserView.as_view({'get':'get_all_users','post':'post_user'}), name='List_Users'),
    path('rolechanges', RoleRequestsView.as_view({'get':'get_role_requests','post':'post_role_request',}), name='roleChanges'),
    path('users/authenticate',AuthenticationView.as_view(), name='Get_token'),
    path('users/logout',LogoutView.as_view(), name='logout'),
    path('users/<int:pk>', UserView.as_view({'get':'get_user','delete':'delete_user','put':'put_user_data'})),
    path('transacts',TransactsView.as_view({'get':'get_all_transacts','post':'post_transact_fisics'}), name='listOfTransacts'),
    path('transacts/<int:pk>',TransactsView.as_view({'delete':'delete_transact','put':'put_transact'}), name='individual_transact'),
    path('users/invitations', InvitationCodeView.as_view({'get':'get_invitation_codes','post':'post_invitation_code'}), name='invitation'),
    path('userbased/invitation/<int:pk>', InvitationCodeView.as_view({'get':'get_invitation_code_user_based'}, name="Ayuda")),
    path('users/invitations/<int:pk>', InvitationCodeView.as_view({'delete':'delete_invitation_code'}), name='invitationssss'),
]