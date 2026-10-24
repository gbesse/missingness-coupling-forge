import random,math,copy
from .common import number,integer,unique_ids

def run(data):
 rows=data['rows'];unique_ids(rows);rules=data['rules'];seed=integer(data.get('seed',0),0,2**53-1);rng=random.Random(seed)
 if not isinstance(rules,dict)or len(rules)>30 or len(rows)>5000:raise ValueError('bounds')
 specs=[]
 for field,r in sorted(rules.items()):
  if field=='id':raise ValueError('identity')
  if r['mechanism']=='mcar':number(r['probability'],0,1)
  elif r['mechanism']=='mar':
   number(r.get('intercept',0),-1000,1000)
   if field in r['coefficients']or len(r['coefficients'])>30:raise ValueError('observed_predictors')
   for k,v in r['coefficients'].items():number(v,-1000,1000)
   for row in rows:
    for k in r['coefficients']:
     if k in rules or row.get(k)is None:raise ValueError('predictor_must_stay_observed')
     number(row[k],-1e9,1e9)
  else:raise ValueError('mechanism')
  specs.append((field,r))
 masked=copy.deepcopy(rows);masks=[]
 for original,result in zip(rows,masked):
  record={'id':original['id'],'fields':{}}
  for field,r in specs:
   if field not in original:raise ValueError('target_missing')
   if r['mechanism']=='mcar':p=r['probability']
   else:
    z=r.get('intercept',0)+math.fsum(v*original[k]for k,v in r['coefficients'].items());p=1/(1+math.exp(-z))if z>=0 else math.exp(z)/(1+math.exp(z))
   hide=rng.random()<p
   if hide:result[field]=None
   record['fields'][field]={'probability':p,'newly_hidden':hide and original[field]is not None,'originally_missing':original[field]is None}
  masks.append(record)
 return {'masked_rows':masked,'masks':masks,'seed':seed,'model':'caller_declared_mcar_or_observed_covariate_logistic_mar_simulation'}
