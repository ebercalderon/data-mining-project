# Features
features = ['age', 'job', 'education', 'default', 'day_of_week', 'duration', 'campaign', 'previous', 'cons.conf.idx', 'euribor3m', 'nr.employed']

# Questions
questions = {
  'age': 'Is your age ',
  'job': 'Is your job ',
  'education': 'Is your education ',
  'nr.employed': 'Is your nr.employed ',

  'default': 'Does the lead has any default?',
  'day_of_week': 'Last contact day of the week?',
  'duration': 'Last contact duration, in minutes?',
  'campaign': 'Number of contacts performed during this campaign and for this client?',
  'previous': 'Number of contacts performed before this campaign and for this client?',

  'cons.conf.idx': 'Consumer confidence index - Monthly indicator?',
  'euribor3m': 'Euribor 3 month rate - daily indicator?'
}

# Answers Buttons
answers = {
  'age': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'job': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'education': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],
  'nr.employed': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }],

  'default': [{ 'title': 'Yes', 'value': 1 }, { 'title': 'No', 'value': 0 }, { 'title': 'Unknown', 'value': 2 }],
  'day_of_week': [{ 'title': 'Mon', 'value': 0 }, { 'title': 'Tue', 'value': 1 }, { 'title': 'Wed', 'value': 2 }, { 'title': 'Thu', 'value': 3 }, { 'title': 'Fri', 'value': 4 }],
  'duration': [{ 'title': '0-1', 'value': 1 }, { 'title': '2 - 5', 'value': 2 }, { 'title': '6-10', 'value': 3 }, { 'title': '11-20', 'value': 4 }, { 'title': '21-40', 'value': 5 }, { 'title': '41-60', 'value': 6 }, { 'title': 'Above 60', 'value': 0 }],
  'campaign': [{ 'title': '1', 'value': 1 }, { 'title': '2', 'value': 2 }, { 'title': '3', 'value': 3 }, { 'title': '4', 'value': 4 }, { 'title': '5', 'value': 5 }, { 'title': '6', 'value': 6 }, { 'title': 'Above 7', 'value': 0 }],
  'previous': [{ 'title': '0', 'value': 0 }, { 'title': '1', 'value': 1 }, { 'title': '2', 'value': 2 }, { 'title': 'Above 3', 'value': 3 }],

  'cons.conf.idx': [{ 'title': '> -35', 'value': 1 }, { 'title': '> -40', 'value': 2 }, { 'title': '> -45', 'value': 3 }, { 'title': '> -50', 'value': 4 }, { 'title': '> -60', 'value': 5 }, { 'title': '> -30', 'value': 0 }],
  'euribor3m': [{ 'title': '0.7-0.9', 'value': 1 }, { 'title': '1-1.9', 'value': 2 }, { 'title': '3-3.9', 'value': 3 }, { 'title': '4.6-5.1', 'value': 4 }, { 'title': '4-4.5', 'value': 5 }, { 'title': '0.6-0.69', 'value': 0 }]
}

# Answers that is String
questionWithComplete = ['age', 'job', 'education', 'nr.employed']

# Absolute (Remove train_x item if is not equal)
absoluteFeatures = ['age', 'job']
