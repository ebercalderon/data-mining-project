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

  'default': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }, { 'title': 'Unknown', 'value': 2 }],
  'day_of_week': [{ 'title': 'Mon', 'value': 0 }, { 'title': 'Tue', 'value': 1 }, { 'title': 'Wed', 'value': 2 }, { 'title': 'Thu', 'value': 3 }, { 'title': 'Fri', 'value': 4 }],
  'duration': [{ 'title': 'between 0-1', 'value': 1 }, { 'title': 'between 2 - 5', 'value': 2 }, { 'title': 'between 6-10', 'value': 3 }, { 'title': 'between 11-20', 'value': 4 }, { 'title': 'between 21-40', 'value': 5 }, { 'title': 'between 41-60', 'value': 6 }, { 'title': 'Above 60', 'value': 0 }],
  'campaign': [{ 'title': '1', 'value': 1 }, { 'title': '2', 'value': 2 }, { 'title': '3', 'value': 3 }, { 'title': '4', 'value': 4 }, { 'title': '5', 'value': 5 }, { 'title': '6', 'value': 6 }, { 'title': 'Above 7', 'value': 0 }],
  'previous': [{ 'title': '0', 'value': 0 }, { 'title': '1', 'value': 1 }, { 'title': '2', 'value': 2 }, { 'title': 'Above 3', 'value': 3 }],

  'cons.conf.idx': [{ 'title': '1', 'value': 1 }, { 'title': '2', 'value': 2 }, { 'title': '3', 'value': 3 }, { 'title': '4', 'value': 4 }, { 'title': '5', 'value': 5 }, { 'title': 'Above 7', 'value': 0 }],
  'euribor3m': [{ 'title': '1', 'value': 1 }, { 'title': '2', 'value': 2 }, { 'title': '3', 'value': 3 }, { 'title': '4', 'value': 4 }, { 'title': '5', 'value': 5 }, { 'title': 'Above 7', 'value': 0 }]
}

# Answers that is String
questionWithComplete = ['age', 'job', 'education', 'nr.employed']

# Absolute (Remove train_x item if is not equal)
absoluteFeatures = ['age', 'job']
