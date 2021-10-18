# In this version we are simply solving the task.Without OOP.:)
n,m = input().split(' ')

n = int(n)
m = int(m)
Dict = {}
i = 0
while i != n:
	name = input()
	List = input().split(' ')
	i2 = 0
	while i2 != m:
		try:
			List[i2] = float(List[i2])
		except:
			print('Не шути со мной,придурок!!!')
		i2 += 1
	Dict[name] = sum(List)
	i += 1
min1 = min(Dict.values())
for key,v in Dict.items():
	if v == min1:
		print(key)