import random,math
import matplotlib.pyplot as plt
import numpy as np
def monte_carlo():
	try:
		n=int(input("Insert number of benchmarks (n): "))
		if n>0:
			k=0
			points_in=[]
			points_out=[]
			for i in range(n):
				x=random.uniform(-1,1)
				y=random.uniform(-1,1)
				if (x**2)+(y**2)<=1:
					k+=1
					points_in.append((x,y))
				else:
					points_out.append((x,y))
		else:
			print("Insert valid n-value (n>0)")
			return
	except ValueError:
		print("Error occured. Try again.")
	except RuntimeError:
		print("Runtime error occured. Try smaller number.")
	pi_est=(4*k)/n
	print(f"Score: {pi_est}")
	print(f"Relative error: {round(abs(math.pi-pi_est)*100/math.pi,2)} %.")

	x_in, y_in=zip(*points_in)
	x_out,y_out=zip(*points_out)

	plt.scatter(x_in,y_in,s=5,color='red')
	plt.scatter(x_out,y_out,s=5,color='blue')

	t=np.linspace(0,2*math.pi, 400)
	plt.plot(np.cos(t),np.sin(t),color='black')

	plt.gca().set_aspect('equal')
	plt.show()

monte_carlo()