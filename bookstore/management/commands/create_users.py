# bookstore/management/commands/create_users.py
from django.core.management.base import BaseCommand
from bookstore.models import User

class Command(BaseCommand):
    help = "Crée des utilisateurs avec différents rôles"

    def handle(self, *args, **kwargs):
        # Vérifiez si l'utilisateur existe déjà avant de le créer
        User.objects.get_or_create(username="admin_user", defaults={'is_admin': True, 'is_publisher': False, 'is_librarian': False})
        User.objects.get_or_create(username="publisher_user", defaults={'is_admin': False, 'is_publisher': True, 'is_librarian': False})
        User.objects.get_or_create(username="librarian_user", defaults={'is_admin': False, 'is_publisher': False, 'is_librarian': True})

        self.stdout.write(self.style.SUCCESS("Utilisateurs créés avec succès !"))
