import itertools

def main():

	numjobs = "1 4 16 64".split()
	filesize = "16m 64m 256m 1024m 4g 16g 64g 256g 1024g".split()
	rw = "randread randwrite".split()
	direct = "0 1".split()
	bs = "4 8 16 64 128 256 512 1024".split() 
	iodepth = "1 4 16 64 256".split()

	templ = "fio --name=%s --thread --group_report --numjobs=%s --filesize=%s --rw=%s --direct=%s --bs=%sk --iodepth=%s --runtime=3 --fsync_on_close=1 --filename=/tmp/a --minimal"

	for x in itertools.product(numjobs, filesize, rw, direct, bs, iodepth):
		print templ % tuple(['_'.join(x)] + list(x))

main()
	
	
	
