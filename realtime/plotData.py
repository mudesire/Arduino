

import pandas as pd
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


#
def animate(i):
	data = pd.read_csv('temp.csv', header=0, sep=',',parse_dates=[0], index_col=0, squeeze=True)
	ax.clear()
	ax.plot(data)
	plt.xlabel('Time')
	plt.ylabel('distance[m]')
	plt.title('Ultrasound ranging')
	plt.tight_layout()
	plt.xticks(rotation=45, ha='right')
	plt.subplots_adjust(bottom=0.30)
#
while True:
	try:
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		ani = FuncAnimation(fig, animate, interval=100)
		plt.show()
	except KeyboardInterrupt:
		print('Keyboard Interrupt')
		plt.close()
		break

