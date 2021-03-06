from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_status = [
        (1, 'Admitted'),
        (2, 'Discharged'),
        (3, 'Recovered'),
        (4, 'Deceased'),
    ]

    severities = [
        (0, 'Mild'),
        (1, 'Potenitally worsening'),
        (2, 'Moderate severity'),
        (3, 'High severity'),
        (4, 'Requires urgent care'),
    ]

    name = models.CharField(max_length=32)
    dob = models.DateField()
    address = models.CharField(max_length=128)
    phone_no = models.IntegerField()
    next_of_kin = models.ForeignKey('Kin', on_delete=models.CASCADE, blank=True, null=True)
    insurance = models.CharField(max_length=16)
    aadhar = models.IntegerField()
    status = models.IntegerField(choices=patient_status, default=1)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, blank=True, null=True)
    admit_date = models.DateTimeField()
    recovery_date = models.DateField(blank=True, null=True)
    discharge_date = models.DateTimeField(blank=True, null=True)
    bed = models.OneToOneField('Bed', on_delete=models.SET_NULL, blank=True, null=True)
    medicines = models.ManyToManyField('Medicine', blank=True)
    health_details = models.OneToOneField('HealthDetails', on_delete=models.CASCADE, blank=True, null=True)
    severity_score = models.IntegerField(default=0)
    severity = models.IntegerField(choices=severities, default=1)

    def __str__(self):
        return self.name

    def age(self):
        years = date.today() - self.dob
        return int(years.days / 365)


class Kin(models.Model):
    name = models.CharField(max_length=32)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.name

class HealthDetails(models.Model):
    def calculate_severity(self):
        score = 0
        med_list = [self.aches, self.sore_throat, self.diarrhoea, self.conjunctivitis, self.headache,
            self.loss_of_taste_or_smell, self.rash,
        ]
        high_list = [self.shortness_of_breath, self.chest_pain, self.loss_of_speech]

        print(med_list)
        for isShowing in med_list:
            count = 0
            if isShowing:
                score += 2
                count += 1
            if count > 3:
                score += 5
        
        print(high_list)
        for isShowing in high_list:
            if isShowing:
                score += 10

        score = 23 if score > 23 else score

        self.patient.severity_score = score
        self.patient.save()
        
        return int((score / 23) * 4)

    diseases = [
        ('DB', 'Diabeties'),
        ('CD', 'Cardiovascular Disease'),
    ]

    #symptoms
    fever = models.BooleanField(default=False)
    dry_cough = models.BooleanField(default=False)
    tiredness = models.BooleanField(default=False)

    # less common symptoms
    aches = models.BooleanField(default=False)
    sore_throat = models.BooleanField(default=False)
    diarrhoea = models.BooleanField(default=False)
    conjunctivitis = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    loss_of_taste_or_smell = models.BooleanField(default=False)
    rash = models.BooleanField(default=False)

    #serious symptoms
    shortness_of_breath = models.BooleanField(default=False)
    chest_pain = models.BooleanField(default=False)
    loss_of_speech = models.BooleanField(default=False)


    comorbid = models.CharField(
        max_length=12,
        choices=diseases,
        blank=True,
        null=True,
    )
    blood_group = models.CharField(max_length=3, default='UNK')
    is_smoker = models.BooleanField(default=False)
    is_drinker = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.patient.name + "'s Health Record"
        except:
            return "Health Record " + str(self.id)

    


class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='doctor',
    )
    name = models.CharField(default='dr', max_length=32)
    phone_no = models.IntegerField(blank=True, null=True)
    patients = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    category_types = [
        ('PK', 'Painkiller'),
        ('BT', 'Blood thinner'),
        ('LX', 'Laxative'),
        ('AI', 'Anti inflammatory')
    ]
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=2, choices=category_types)
    expiry = models.DateField()
    qty = models.IntegerField()
    threshold_value = models.IntegerField()

    def __str__(self):
        return self.name


class Ward(models.Model):
    type_list = [
        ('ICU', 'ICU'),
        ('GEN', 'General'),
    ]

    type = models.CharField(max_length=3, choices=type_list)

    def __str__(self):
        return self.type + ' ' + str(self.id)

class Bed(models.Model):
    available = models.BooleanField(default=True)
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE)
    ventilator = models.OneToOneField('Ventilator', blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        status = '(Available)' if self.available else '(Unavailable)'
        return 'Bed ' + str(self.id) + status

class Ventilator(models.Model):
    available = models.BooleanField(default=True)

    def __str__(self):
        return 'Ventilator ' + str(self.id)

class LabTest(models.Model):
    type_choices = [
        ('AG', 'Antigen'),
        ('RT', 'RT-PCR'),
    ]

    result_choices = [
        ('P', 'Positive'),
        ('N', 'Negative'),
    ]

    type = models.CharField(max_length=2, choices=type_choices)
    result = models.CharField(max_length=1, choices=result_choices, blank=True)
    testing_date = models.DateTimeField()
    test_duration = models.IntegerField('Hours until test results')
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Lab test ' + str(self.id)
