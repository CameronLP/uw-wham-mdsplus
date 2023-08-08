from MDSplus import Device,Data,Action,Dispatch,Method

class RP(Device):
	"""A Demo 4 Channel, 16 but digitizer"""

	parts=[{'path':':NAME','type':'text'}, {'path':':COMMENT','type':'text'},
	{'path':':CLOCK_FREQ','type':'numeric', 'value':10000},
	{'path':':TRIG_SOURCE','type':'numeric', 'value':0},
	{'path':':PTS','type':'numeric', 'value':1000}]
	for i in range(4):
		parts.append({'path':'.CHANNEL_%d'%(i),'type':'structure'})
		parts.append({'path':'.CHANNEL_%d:START_IDX'%(i),'type':'numeric', 'value':0})
		parts.append({'path':'.CHANNEL_%d:END_IDX'%(i),'type':'numeric', 'value':1000})
		parts.append({'path':'.CHANNEL_%d:DATA'%(i),'type':'signal', 'options':('no_write_model','compress_on_put')})

	del i


	def init(self,arg):


		try:
			name = self.name.data()
		except:
			print("Missing name")
			return 0


		return 1

	def store(self,arg):
		return 1

