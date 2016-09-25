import sys
from fio_browser import read_summary
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

commaform = mpl.ticker.FuncFormatter(lambda x,p: format(int(x), ','))

def read_summary(filename):
	pass



if __name__ == '__main__':
	usage = "%s #job dirs"
	if len(sys.argv) < 3:
		print usage
		exit()

	sns.set_style("whitegrid")

	f,ax = plt.subplots(1,1)
	j = int(sys.argv[1])
	filename = sys.argv[2]
	df = read_summary(filename)
	df.bandwidth = df.bandwidth
	# depth: [16, 64, 256, 1024, 4096]
	[ax.plot(df[df.depth==dp]['iosize'], df[df.depth==dp]['iops'], marker='o', 
			linewidth=3, label=dp) for dp in [4**i for i in range(2, 7)]]

	ax.get_yaxis().set_major_formatter(commaform)
	ax.set_yscale('log')
	ax.set_xlabel('iosize')
	ax.set_ylabel('iops')
	ax.legend(loc='best')
	sns.plt.show()

