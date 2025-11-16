from django.core.management.base import BaseCommand
from base.models import BandMember

class Command(BaseCommand):
    help = 'Reorder band members: Katie, Austin, Elisha, Carter, Coleson, Micah'

    def handle(self, *args, **options):
        # Define the order: name -> order value
        order_map = {
            'Katie Berglin': 1,
            'Austin Martin': 2,
            'Elisha (Eli) McDuffie': 3,
            'Elisha McDuffie': 3,  # In case (Eli) was removed
            'Carter Randell': 4,
            'Coleson Franklin': 5,
            'Micah McDuffie': 6,
        }
        
        updated_count = 0
        for name, order in order_map.items():
            try:
                member = BandMember.objects.get(name__icontains=name.split()[0])
                member.order = order
                member.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f'Updated {member.name} to order {order}'))
            except BandMember.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Member with name containing "{name.split()[0]}" not found'))
            except BandMember.MultipleObjectsReturned:
                # Try exact match
                try:
                    member = BandMember.objects.get(name=name)
                    member.order = order
                    member.save()
                    updated_count += 1
                    self.stdout.write(self.style.SUCCESS(f'Updated {member.name} to order {order}'))
                except:
                    self.stdout.write(self.style.ERROR(f'Multiple members found for "{name}", please update manually'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} band members'))

