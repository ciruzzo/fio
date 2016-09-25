import sys, os
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

commaform = mpl.ticker.FuncFormatter(lambda x,p: format(int(x), ','))

def get_info(text):
	numjobs, filesize, rw, direct, bs, iodepth = text.split('_')

def read_terse(infile):
	df = pd.read_csv(infile,sep=';',header=0)
	df.columns = range(1,len(df.columns)+1)

	tm = df[9]+df[50]
	iops = df[8]+df[49]

	#cleaning for ('99.0000%=123'), 95th and 99th percentile
	for X in [29,30,70,71]:
		df[X] = df[X].str.split('=').str.get(1).astype('float64')

	lat = [df[r]+df[w] for r,w in zip(range(38,42)+range(29,31), range(79,83)+range(70,72))]

	kb = df[6]+df[47]
	usr = df[88].str.rstrip('%').astype('float64')
	sys = df[89].str.rstrip('%').astype('float64')

	return pd.concat([tm, iops, kb, usr, sys] + lat, axis=1, keys=["tm","iops","kb","usr","sys","latmin","latmax","latmean","latstdv","p95th","p99th"])
