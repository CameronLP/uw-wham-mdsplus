from MDSplus import Device,Data,Action,Dispatch,Method

class WHAM_RED_PITAYA(Device):

	parts=[{'path':':NAME', 'type':'text'}, 
	{'path':':COMMENT', 'type':'text'},
	{'path':':FREQ', 'type':'numeric'},
	{'path':':CH_01', 'type':'signal'},
	{'path':':CH_02', 'type':'signal'}
	]

	def init(self,arg):
		return 1

	def store(self,arg):
		return 1
