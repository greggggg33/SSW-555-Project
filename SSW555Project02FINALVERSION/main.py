import python-gedcom
key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']

levels = ['1','2','3']



text_file = open('export-BloodTree.ged', 'r')


y = '000'
numberPriority = '000'
tag = '000'
for line in text_file:
  level_number = line[:1]

  line = line.split()

  for word in key_words:
      if word in line:

       tag = word
       y = 'Y'

  for level in levels:
      if level in line:
        numberPriority = level

  print('<-- |' + tag + '|' + numberPriority + '|' + y)
  print("-->", line)
