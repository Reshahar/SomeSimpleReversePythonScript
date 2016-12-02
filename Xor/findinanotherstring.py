x='01040E0A0524172A0D131C0D1B2730292A'

a = x.decode('hex')
b = 'swfxc{gdv}fwfctslydRddoepsckaNDMSRITPNsmr1_=2cdsef66246087138'
c = ''

for j in range(17):
	i = ord(a[j])
	c += b[i]
print c
