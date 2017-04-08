import sys

INPUT_VIDEO = "input.ext"
OUTPUT_VIDEO = "output.ext"

def getSec(s): # http://stackoverflow.com/a/17248389
    l = map(int, s.split(':')) # l = list(map(int, s.split(':'))) in Python 3.x
    return sum(n * sec for n, sec in zip(l[::-1], (1, 60, 3600)))

try:
	inputfile = sys.argv[1]
except:
	print "usage: mute.py list_with_durations.txt"
	sys.exit(1)

audiofilter = ""

for line in open(inputfile,'r'):
	i = 0
	for time in line.split():
		if not time is "-":
			if i == 0:
				time1 = time
				i += 1
			elif i == 1:
				time2 = time
	#print str(getSec(time1)) + "-" + str(getSec(time2))
	audiofilter = audiofilter + 'volume=enable=\'between(t,' + str(getSec(time1)) + ',' + str(getSec(time2)) + ')\':volume=0, '

audiofilter = audiofilter[:-2] # remove last , and space

print "ffmpeg -i " + INPUT_VIDEO + " -af \"" + audiofilter + "\" -c:a aac -c:v copy " + OUTPUT_VIDEO