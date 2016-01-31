import cmd, textwrap, sys, time

print "Your pudgy fingers sidle up to the keys on the keyboard."

def output_jargon(looping = True):
	while looping:
		time.sleep(.1)
		print '.',
		sys.stdout.flush()


output_jargon()
