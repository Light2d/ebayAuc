# import os
# import sys
# import django

# # Добавляем путь к корневому каталогу проекта в sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # Загружаем настройки Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebay.settings')
# django.setup()

# # Теперь можно импортировать класс Command и другие модули Django
# from django.core.management.base import BaseCommand
# from allauth.socialaccount.models import SocialApp

# # Определяем класс Command
# class Command(BaseCommand):
#     help = 'Creates a SocialApp for Google provider'

#     # Определяем функцию handle, которая будет вызвана при выполнении команды
#     def handle(self, *args, **kwargs):
#         # Создаем объект SocialApp для Google
#         SocialApp.objects.create(
#             provider='google',
#             name='Google',
#             client_id='764768997499-qd34e6l4kr6856fovrbik9f3rbhma1gj.apps.googleusercontent.com',
#             secret='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'
#         )

#         # Выводим сообщение об успешном создании SocialApp
#         self.stdout.write(self.style.SUCCESS('SocialApp for Google created successfully'))
