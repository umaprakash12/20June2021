
import pytest
from bmi_calculator_controller import BMI_Calculator_Api
from _pytest.monkeypatch import monkeypatch

class Test_Bmi_controller():
    
    @pytest.mark.test_bmi_calculate
    def test_bmi_calculate(self, monkeypatch):
        data =[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Calculator_Api(data)
        obj.bmi_calculate()
        assert isinstance(obj, BMI_Calculator_Api) 
        
        
    @pytest.mark.test_validate
    def test_validate(self, monkeypatch):
        data =[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Calculator_Api(data)
        obj.validate()
        assert isinstance(obj, BMI_Calculator_Api) 
        