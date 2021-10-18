# In this version we are simply solving the task.Without OOP.:)
n,m = input().split(' ')
try:
	n = int(n)
	m = int(m)
except:
	print('Борис,не нанимай на это дело идиотов!')
Dict = {}
for i in range(0,n):
	name = input()
	List = input().split(' ')
	for i in range(0,m):
		try:
			List[i] = float(List[i])
		except:
			print('Не шути со мной!!!')
	Dict[name] = sum(List)
min1 = min(Dict.values())
for key,v in Dict.items():
	if v == min1:
		print(key)