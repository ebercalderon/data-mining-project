# Features
features = ['age', 'job', 'education', 'default', 'day_of_week', 'duration', 'campaign', 'previous', 'cons.conf.idx', 'euribor3m', 'nr.employed']

# Questions
questions = {
  'age': 'age?',
  'job': 'job?',
  'education': 'education?',
  'nr.employed': 'nr.employed?',

  'default': 'default?',
  'day_of_week': 'day_of_week?',
  'duration': 'duration?',
  'campaign': 'campaign?',
  'previous': 'previous?',

  'cons.conf.idx': 'cons.conf.idx?',
  'euribor3m': 'euribor3m?'
}

# Answers Buttons
answers = {
  'age': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'job': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'education': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'nr.employed': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],

  'default': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'day_of_week': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'duration': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'campaign': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'previous': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],

  'cons.conf.idx': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'euribor3m': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }]
}

# Answers that is String
questionWithComplete = ['age', 'job', 'education', 'nr.employed']

# Absolute (Remove train_x item if is not equal)
absoluteFeatures = ['duration', 'euribor3m', 'age', 'job']
