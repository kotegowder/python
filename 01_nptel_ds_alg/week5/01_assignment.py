# update Books, Borrowers and Checkouts dictionaries
Books     = {}
Borrowers = {}
Checkouts = []

line = input()
while True:
  line = input()
  if line == "Borrowers":
    break
  tilde_pos = line.find('~')
  Books[line[:tilde_pos]] = line[tilde_pos+1:]
while True:
  line = input()
  if line == "Checkouts":
    break
  tilde_pos = line.find('~')
  Borrowers[line[:tilde_pos]] = line[tilde_pos+1:]
while True:
  line = input()
  if line == "EndOfInput":
    break
  Checkouts.append(line.split('~'))

for idx in range(len(Checkouts)):
  Checkouts[idx][0] = Borrowers[Checkouts[idx][0]]
  Checkouts[idx][1] = [Checkouts[idx][1], Books[Checkouts[idx][1]]]
  Checkouts[idx][2] = (Checkouts[idx][2]).split('-')
for idx in range(len(Checkouts)):
  Checkouts[idx][0],Checkouts[idx][2] = Checkouts[idx][2],Checkouts[idx][0]


for idx in range(len(Checkouts)):
  minIdx = idx
  for i in range(idx, len(Checkouts)):
    if int(Checkouts[i][0][0]) < int(Checkouts[minIdx][0][0]):
      minIdx = i
    if ((int(Checkouts[i][0][0]) == int(Checkouts[minIdx][0][0])) and
        (int(Checkouts[i][0][1]) < int(Checkouts[minIdx][0][1]))):
      minIdx = i
    if ((int(Checkouts[i][0][0]) == int(Checkouts[minIdx][0][0])) and
        (int(Checkouts[i][0][1]) == int(Checkouts[minIdx][0][1])) and
        (int(Checkouts[i][0][2]) < int(Checkouts[minIdx][0][2]))):
      minIdx = i
    if ((int(Checkouts[i][0][0]) == int(Checkouts[minIdx][0][0])) and
        (int(Checkouts[i][0][1]) == int(Checkouts[minIdx][0][1])) and
        (int(Checkouts[i][0][2]) == int(Checkouts[minIdx][0][2])) and
        (Checkouts[i][2] < Checkouts[minIdx][2])):
      minIdx = i
    if ((int(Checkouts[i][0][0]) == int(Checkouts[minIdx][0][0])) and
        (int(Checkouts[i][0][1]) == int(Checkouts[minIdx][0][1])) and
        (int(Checkouts[i][0][2]) == int(Checkouts[minIdx][0][2])) and
        (Checkouts[i][2] == Checkouts[minIdx][2]) and 
        (Checkouts[i][1][0] < Checkouts[minIdx][1][0])):
      minIdx = i
    if ((int(Checkouts[i][0][0]) == int(Checkouts[minIdx][0][0])) and
        (int(Checkouts[i][0][1]) == int(Checkouts[minIdx][0][1])) and
        (int(Checkouts[i][0][2]) == int(Checkouts[minIdx][0][2])) and
        (Checkouts[i][2] == Checkouts[minIdx][2]) and 
        (Checkouts[i][1][0] == Checkouts[minIdx][1][0]) and
        (Checkouts[i][1][1] < Checkouts[minIdx][1][1])):
      minIdx = i
  (Checkouts[idx], Checkouts[minIdx]) = (Checkouts[minIdx], Checkouts[idx])

for i in range(len(Checkouts)):
  print(Checkouts[i][0][0]+"-"+Checkouts[i][0][1]+"-"+
              Checkouts[i][0][2]+"~"+Checkouts[i][2]+"~"+
              Checkouts[i][1][0]+"~"+
              Checkouts[i][1][1])
