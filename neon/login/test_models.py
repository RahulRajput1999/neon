from django.test import TestCase
from .models import Program


class TestModels(TestCase):
    def setUp(self):
        self.program1 = Program.objects.create(
            program_code='PC01',
            institute_name='Inst1',
            name='Prog1',
            alias='Prog1',
            program_type='Type1',
            session_type='Semesters',
            no_of_sess=8,
            no_of_year=4,
            eligibility_criteria='Some criteria',
            result_type='Reg',
            total_sessional=4,
            compulsory_sessional=3
        )
    
    def test_project_model(self):
        self.assertAlmostEquals(self.program1.name,'Prog1')
