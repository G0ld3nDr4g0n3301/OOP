n,m = input().split(' ')
try:
	n = int(n)
	m = int(m)
except:
	print('Ой-вэй,Рабинович,вы же неправильно ввели числа!Таки страшно представить,сколько шекелей я с этого потеряю!') #Я бы кодил на Иврите,но такого ЯПа нету((.
class Driver():
	def __init__(self,name,List):
		self.name = name
		self.sumtime = sum(List)
		for i in range(0,m):
			exec('self.CircleNumber{} = List[i]'.format(i+1))
	def __lt__(self,other):
		return self.sumtime < other.sumtime
	def __le__(self,other):
		return self.sumtime <= other.sumtime
	def __gt__(self,other):
		return self.sumtime > other.sumtime
	def __ge__(self,other):
		return self.sumtime >= other.sumtime
	def __eq__(self,other):
		return self.sumtime == other.sumtime
	def __ne__(self,other):
		return self.sumtime != other.sumtime
for i in range(0,n):
	try:
		exec('Racer{} = Driver(input(),[float(k) for k in input().split(\' \')])'.format(i+1))
	except:
		print('Неправильный ввод.')
#print(sorted([Obj1,Obj2,Obj3 и т.д.]))