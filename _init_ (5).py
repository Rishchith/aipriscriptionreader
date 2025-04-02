from unittest import TestLoader, TestSuite

def load_tests():
    loader = TestLoader()
    suite = TestSuite()
    
    # Add test suites for each feature
    test_modules = [
        'test_features.test_prescription',
        'test_features.test_treatment',
        'test_features.test_virtual_assistant',
        'test_features.test_epidemic',
        'test_features.test_insurance',
        'test_features.test_disease_detector',
        'test_features.test_medication_cost',
        'test_features.test_mental_health',
        'test_features.test_womens_health',
        'test_features.test_environmental'
    ]
    
    for module in test_modules:
        suite.addTests(loader.loadTestsFromName(module))
    
    return suite