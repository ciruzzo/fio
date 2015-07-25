#kldload aio

for t in read write 
do
echo $t
fio --append-terse --output=result-freebsd-$t.txt --filename=fio-data/test --name=fio-freebsd-$t --readwrite=$t  --bs=1m freebsd.fio
done

for t in randread randwrite 
do
echo $t
	for b in 4k 16k 64k
	do
	fio --append-terse --output=result-freebsd-$t-$b.txt --filename=fio-data/test --name=fio-freebsd-$t-$b --readwrite=$t --bs=$b freebsd.fio
	done

done

