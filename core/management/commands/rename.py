# import os
# from django.core.management.base import BaseCommand


# class Command(BaseCommand):
#     help = 'Renames a Django project'

#     def add_arguments(self, parser):
#         parser.add_argument('new-project-name', type=str, help='the new django project')

#     def handle(self, *args, **kwargs):
#         new_project_name = kwargs['new-project-name']

#         # logic for renaming the files

#         files_to_rename = ['demo/settings/base.py','demo/wsgi.py', 'manage.py']
#         folder_to_rename = 'demo'

#         for f in files_to_rename:
#             with open(f, 'r') as file:
#                 filedata = file.read()

#             filedata = filedata.replace('demo', new_project_name)

#             with open(f, 'w') as file:
#                 file.write(filedata)

#         os.rename(folder_to_rename, new_project_name)

#         self.stdout.write(self.style.SUCCESS(
#             'Project has been renamed to %s' % new_project_name))

import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('current', type=str, nargs='+',
                            help='The current Django project folder name')
        parser.add_argument('new', type=str, nargs='+',
                            help='The new Django project name')

    def handle(self, *args, **kwargs):
        current_project_name = kwargs['current'][0]
        new_project_name = kwargs['new'][0]

        # logic for renaming the files

        files_to_rename = [f'{current_project_name}/settings/base.py',
                           f'{current_project_name}/wsgi.py', 'manage.py']

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(current_project_name, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(current_project_name, new_project_name)

        self.stdout.write(self.style.SUCCESS(
            'Project has been renamed to %s' % new_project_name))
