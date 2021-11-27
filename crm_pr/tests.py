from decimal import Decimal 
from django.test import TestCase
from tasks.models import Tasks
from teachers.models import Teachers
from klients.models import Klients, StatusKlienta, Istochnik
from services.models import TypeService, ServiceModel
# Create your tests here.


class TaskTest(TestCase):

    def test_setUp(self):
        # print(TypeService.objects.get(pk=2))
        self.type_service = TypeService.objects.get(id=2).type
        self.status = StatusKlienta.objects.get(pk=1).status
        self.istochnik = Istochnik.objects.get(pk=1).istochnik
        self.teacher = Teachers.objects.create(f_name = 'Иван', s_name ='Колымагин', time = 18)
        self.service = ServiceModel.objects.create(name = 'Естествознание', type = self.type_service, teacher = self.teacher, count = 10, max_count = 18, price = Decimal('4.13'),sale_price = ('2.18'),)
        self.klient = Klients.objects.create(f_name = 'Саша', 
                              s_name = 'Остапчук',
                              servise  = self.service,
                              town = 'Moskow',
                              school = '22',
                              telephone =  37501987654321,
                              #call =  callf ,
                              another_inf = 'Умный мальчик' ,
                              status =  self.status ,
                              istochnik = self.istochnik ,)

    

        
        