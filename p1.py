import sys
def cal():
	arr = [-11,'abcd','dfgh',-6,-7,-3,'a','b',-21]
	min = sys.maxint
	for a in arr:
		if(isinstance(a,(int,float,long))):
			if(a<min and a>-1):
				min = a
	if(min!=sys.maxint):
		print(min)
	else:
		print(-1)
	
cal()
