import unittest,copy
from missingness_coupling_forge import run
class Tests(unittest.TestCase):
 def test_zero_and_one_probability_and_no_input_mutation(self):
  d={'rows':[{'id':'a','x':1,'y':2}],'rules':{'x':{'mechanism':'mcar','probability':0},'y':{'mechanism':'mcar','probability':1}}};before=copy.deepcopy(d);r=run(d);self.assertEqual(r['masked_rows'],[{'id':'a','x':1,'y':None}]);self.assertEqual(d,before)
 def test_declared_mar_depends_on_observed_covariate(self):
  d={'rows':[{'id':'a','x':1,'z':-100},{'id':'b','x':1,'z':100}],'rules':{'x':{'mechanism':'mar','coefficients':{'z':1}}}};r=run(d);self.assertEqual(r['masked_rows'][0]['x'],1);self.assertIsNone(r['masked_rows'][1]['x']);self.assertEqual(r,run(d))
 def test_target_and_masked_predictor_are_not_mar_inputs(self):
  for coefficients in ({'x':1},{'y':1}):
   with self.assertRaises(ValueError):run({'rows':[{'id':'a','x':1,'y':2}],'rules':{'x':{'mechanism':'mar','coefficients':coefficients},'y':{'mechanism':'mcar','probability':0}}})
 def test_preexisting_missing_separate_from_new_mask(self):
  r=run({'rows':[{'id':'a','x':None}],'rules':{'x':{'mechanism':'mcar','probability':1}}});self.assertTrue(r['masks'][0]['fields']['x']['originally_missing']);self.assertFalse(r['masks'][0]['fields']['x']['newly_hidden'])
