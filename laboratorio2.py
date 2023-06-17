m1 = [[1, "v", False, "a"],
      ["perro", "s", True, " "],
      ["mexico", "b", 12, "i"],
      [3, "e", [123], "n"]
      ]

def charFindAndJoint(mInput):
	SecretWord = ""
	for i in mInput:
		for j in i:
			if type(j) == str:
				if len(j) == 1:
					SecretWord = SecretWord + j
			else:
				continue
	return SecretWord

print(charFindAndJoint(m1))