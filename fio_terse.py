field1="""terse version,fio version,jobname,groupid,error""".split(',')
field2="""Total I/O (KB),bandwidth (KB/s),IOPS,runtime (msec),\
Submission lat(usec) min,max,mean,stdv,\
Completion lat(usec) min,max,mean,stdv,\
Completion lat percentiles(usec) 1.00%,5.00%,10.00%,20.00%,30.00%,40.00%,50.00%,60.00%,70.00%,80.00%,90.00%,95.00%,99.00%,99.50%,99.90%,99.95%,99.99%,0%,0%,0%,\
Total lat(usec)  min,max,mean,stdv,\
Bandwidth min,max,aggregate percentage of total,mean,stdv""".split(',')
field3="""CPU usage user,system,context switches,major page faults,minor page faults,\
IO depth distribution <=1,2,4,8,16,32,>=64,\
IO latency distribution us <=2,4,10,20,50,100,250,500,750,1000,\
msec<=2,4,10,20,50,100,250,500,750,1000,2000,>=2000""".split(',')
dsk="""Disk utilization (each disk) name,read ios,write ios,read merges,write merges,read ticks,write ticks,read in-queue time,write in-queue time,disk utilization percentage""".split(',')
Err="""Error Info (dependent on continue_on_error,default off) total # errors,first error code,text description""".split(',')

import csv
import sys

def int_float(s):
	try:
		f = float(s)
		if int(f) == f:
			f = int(f)
		s = str(f)
	except:
		pass
	return s

def clean():
	numdisk=0
	field=field1+field2*2+field3+dsk*numdisk

	buf = []
	for row in csv.reader(iter(sys.stdin.readline, ''), delimiter=';'):
		for i,(f,c) in enumerate(zip(field, row)):
			# remove % and something before '='
			v = int_float(c[c.find('=')+1:].rstrip('%'))
			buf.append(v)
#			print "%d %s:\t%s" % (i, f, v)
	return buf

def main():
	buf = clean()
	print ','.join(buf)

main()
