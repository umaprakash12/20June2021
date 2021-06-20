import pytest
from _pytest.monkeypatch import monkeypatch
from bmi_calculator_manager import BMI_Manager 

class Test_Bmi_Manager():
    
    @pytest.mark.bmi_calculation
    def test_bmi_calculation(self, monkeypatch):
        def mock_calculate_bmi(application_id):
            return ""
    
        def mock_catagarize_over_weight(application_id):
            return ""
        
        def mock_count_no_of_over_weight(application_id):
            return ""
        monkeypatch.setattr(BMI_Manager, 'calculate_bmi', mock_calculate_bmi)
        monkeypatch.setattr(BMI_Manager, 'catagarize_over_weight', mock_catagarize_over_weight)
        monkeypatch.setattr(BMI_Manager, 'count_no_of_over_weight', mock_count_no_of_over_weight)
        
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Manager(data)
        obj.bmi_calculation()
    
    @pytest.mark.calculate_bmi
    def test_calculate_bmi(self, monkeypatch):
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Manager(data)
        obj.calculate_bmi()
        assert isinstance(obj, BMI_Manager) 
            
    @pytest.mark.get_bmi
    def test_get_bmi(self, monkeypatch):
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Manager(data)
        obj.get_bmi()
        assert isinstance(obj, BMI_Manager) 
        
    @pytest.mark.catagarize_over_weight
    def test_catagarize_over_weight(self, monkeypatch):
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Manager(data)
        obj.catagarize_over_weight()
        
    @pytest.mark.is_over_weight
    def test_is_over_weight(self, monkeypatch):
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Manager(data)
        obj.is_over_weight()
        
        
    @pytest.mark.count_no_of_over_weight
    def test_count_no_of_over_weight(self, monkeypatch):
        data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        obj = BMI_Manager(data)
        obj.count_no_of_over_weight()
        
        
        
    