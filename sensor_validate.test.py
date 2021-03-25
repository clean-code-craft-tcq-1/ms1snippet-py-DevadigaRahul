import unittest
import sensor_validate

maxDelta ={
  'soc':0.05,
  'current':0.1,
  'temperature':0.5,
  'charge_rate':1
  }

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soc_jumps(self):
    self.assertFalse(
      sensor_validate.reports_sudden_jump_in_reading([0.0, 0.01, 0.5, 0.51],maxDelta['soc'])#Test pass->Expecting [False] for No sudden jump in reading
    )
  
  def test_reports_error_when_current_jumps(self):
    self.assertTrue(
      sensor_validate.reports_sudden_jump_in_reading([0.03, 0.06, 0.09, 0.12],maxDelta['current'])#Test Fail->Expecting [True] for sudden jump in reading
    )

 
  '''def test_reports_error_when_temperature_jumps(self):#Test Empty list/Reading
    self.assertEqual(
       sensor_validate.reports_sudden_jump_in_reading([],maxDelta['temperature']),None
    )'''
    
  def test_reports_error_when_charge_rate_jumps(self):#Test None reading
    self.assertEqual(
       sensor_validate.reports_sudden_jump_in_reading(None,maxDelta['charge_rate']),None
    )
    
if __name__ == "__main__":
  unittest.main()
