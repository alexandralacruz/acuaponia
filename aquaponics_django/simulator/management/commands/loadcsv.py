import csv
import re

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from simulator.models import Cultivo, Municipio, MunicipiosCultivo


class Command(BaseCommand):
    help = 'Load the reviews data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('--csv', type=str)

    @staticmethod
    def row_to_dict(row, header):
        if len(row) < len(header):
            row += [''] * (len(header) - len(row))
        return dict([(header[i], row[i]) for i, head in enumerate(header) if head])

    def handle(self, *args, **options):
        m = re.compile(r'content:(\w+)')
        header = None
        models = dict()
        try:
            with open(options['csv'],newline='',encoding='utf-8') as csvfile:
                model_data = csv.reader(csvfile)
                for i, row in enumerate(model_data):
                    if len(row) == 0: continue
                    if max([len(cell.strip()) for cell in row[1:] + ['']]) == 0 and m.match(row[0]):
                        model_name = m.match(row[0]).groups()[0]
                        models[model_name] = []
                        header = None
                        continue

                    if header is None:
                        header = row
                        continue

                    row_dict = self.row_to_dict(row, header)
                    if set(row_dict.values()) == {''}:
                        continue
                    models[model_name].append(row_dict)

        except FileNotFoundError:
            raise CommandError('File "{}" does not exist'.format(options['csv']))

        for data_dict in models.get('Cultivos', []):
            c, created = Cultivo.objects.get_or_create(cultivo=data_dict['cultivo'],
            tipo=data_dict['tipo'],
            t_min = data_dict['t_min'],
            t_max = data_dict['t_max'],
            t_opt = data_dict['t_opt'],
            germinacion_1 = float(data_dict['germinacion_1']),
            germinacion_n = float(data_dict['germinacion_n']),
            distancia = data_dict['distancia'],
            primera_cosecha = data_dict['primera_cosecha'],
            n_cosechas = data_dict['n_cosechas'],
            distanciaXcosechaAnual = data_dict['distanciaXcosechaAnual'],
            )

            if created:
                print('Created Cultivo "{}"'.format(c.cultivo))

        for data_dict in models.get('Municipios', []):
            m, created = Municipio.objects.get_or_create(municipio=data_dict['municipio'],
            t_min = data_dict['t_min'],
            t_avg = data_dict['t_avg'],
            t_max = data_dict['t_max'], defaults={'departamento':data_dict['departamento']}
            )
            if created:
                print('Created Cultivo "{}"'.format(m.municipio))

       
        print("Import complete")
