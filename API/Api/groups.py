from django.contrib.auth.models import Group
def create_groups():
    # Crea el grupo de administradores
    admin_group, created = Group.objects.get_or_create(name='administrator')
    if created:
        print('Grupo de administradores creado exitosamente')

    # Crea el grupo de checkers
    checkers_group, created = Group.objects.get_or_create(name='checkers')
    if created:
        print('Grupo de checkers creado exitosamente')

    # Crea el grupo de sellers
    sellers_group, created = Group.objects.get_or_create(name='sellers')
    if created:
        print('Grupo de sellers creado exitosamente')

    # Crea el grupo buyers
    buyers_group, created = Group.objects.get_or_create(name="buyers")
    if created:
        print('Grupo buyers creado sin problemas')