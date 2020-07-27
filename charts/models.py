from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=150)
    HR = models.CharField(max_length=150)
    O2Sat = models.CharField(max_length=150)
    Temp = models.CharField(max_length=150)
    SBP = models.CharField(max_length=150)
    MAP = models.CharField(max_length=150)
    DBP = models.CharField(max_length=150)
    Resp = models.CharField(max_length=150)
    EtCO2 = models.CharField(max_length=150)
    BaseExcess = models.CharField(max_length=150)
    HCO3 = models.CharField(max_length=150)
    FiO2 = models.CharField(max_length=150)
    pH = models.CharField(max_length=150)
    PaCO2 = models.CharField(max_length=150)
    SaO2 = models.CharField(max_length=150)
    AST = models.CharField(max_length=150)
    BUN = models.CharField(max_length=150)
    Alkalinephos = models.CharField(max_length=150)
    Calcium = models.CharField(max_length=150)
    Chloride = models.CharField(max_length=150)
    Creatinine = models.CharField(max_length=150)
    Bilirubin_direct = models.CharField(max_length=150)
    Glucose = models.CharField(max_length=150)
    Lactate = models.CharField(max_length=150)
    Magnesium = models.CharField(max_length=150)
    Phosphate = models.CharField(max_length=150)
    Potassium = models.CharField(max_length=150)
    Bilirubin_total = models.CharField(max_length=150)
    TroponinI = models.CharField(max_length=150)
    Hct = models.CharField(max_length=150)
    Hgb = models.CharField(max_length=150)
    PTT = models.CharField(max_length=150)
    WBC = models.CharField(max_length=150)
    Fibrinogen = models.CharField(max_length=150)
    Platelets = models.CharField(max_length=150)
    Age = models.CharField(max_length=150)
    Gender = models.CharField(max_length=10)
    Unit1 = models.CharField(max_length=150)
    Unit2 = models.CharField(max_length=150)
    HospAdmTime = models.CharField(max_length=150)
    ICULOS = models.CharField(max_length=150)
    # SepsisLabel = models.CharField(max_length=150)

    def __str__(self):
        return self.name
