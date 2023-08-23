from MDSplus import Device,Data,Action,Dispatch,Method

class WHAM_ACQ196(Device):

	parts=[
	{'path':':NAME','type':'text'}, 
	{'path':':COMMENT','type':'text'},
	]

	# Add 96 channels
	for i in range(96):
		ch_num = f'{i+1:02d}'
		parts.append({'path':':CH_'+ch_num, 'type':'signal'})

	del i

	def init(self,arg):
		return 1

	def store(self,arg):
		return 1


