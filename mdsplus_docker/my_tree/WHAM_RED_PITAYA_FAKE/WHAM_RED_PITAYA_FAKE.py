from MDSplus import Device,Data,Action,Dispatch,Method

class WHAM_RED_PITAYA_FAKE(Device):

	parts=[{'path':':NAME', 'type':'text'},
	{'path':':COMMENT', 'type':'text'},
	{'path':':FREQ', 'type':'numeric'},
	{'path':':CH_01', 'type':'signal'},
	{'path':':CH_02', 'type':'signal'}
	]


	parts.append(
	{'path':':INIT_ACTION','type':'task',
	#'valueExpr':"Action(Dispatch(None,'INIT',50,None),Method(None,'init',head))",
	#'valueExpr':"Action(None,Method(None,'init',head))"
	'valueExpr':"Method(2,'init',head)",
	'options':('no_write_shot',)
	}
	)

	parts.append(
	{'path':':STORE_ACTION','type':'task',
	#'valueExpr':"Action(None,Method(None,'store',head))"
	'valueExpr':"Method(2,'store',head)",
	'options':('no_write_shot',)
	}
	)

	
	def init(self):
		from MDSplus import TreeNode
		from ctypes import CDLL, c_int, c_char_p
		try:
			deviceLib = CDLL("libWhamRedPitayaFakeShr.so")
		except:
			print("Cannot link to device library")	
			return 0
		

		self.__getattr__("COMMENT").putData("Initialized")



		name = self.name
		print(name)

		print(type(name))

		try:
			name = self.name
		except:
			print("Missing name")
			return 0
		
		deviceLib.initialize(c_char_p(name.encode('utf-8')))
		#deviceLib.initialize(c_char_p(name))
		#deviceLib.initialize(c_char_p(name), c_int(clockMode), c_int(pts))




		return 1

	def store(self):
	    

		from MDSplus import Tree, TreeNode, Int16Array, Float64Array, Int32, Int64, Float32, Float64, Signal, Data, Dimension, Window, Range
		from ctypes import CDLL, c_char_p, c_short, byref


		try:
			deviceLib = CDLL("libWhamRedPitayaFakeShr.so")
		except:
			print("Cannot link to device library")
			return 0
		

		try:
			name = self.name
		except:
			print("Missing name")
			return 0


		DataArray = c_short * 65536
		rawChan = []
		rawChan.append(DataArray())
		rawChan.append(DataArray())


		status = deviceLib.acquire(c_char_p(name.encode('utf-8')), byref(rawChan[0]), byref(rawChan[1]))
		if status == -1:
			print("Acquisition Failed")
			return 0

		totSamples = 65536
		pts = 0
		trigTime = 0

		clockDict = {1000:1, 5000:2, 10000:3, 50000:4, 100000:5}
		clockFreq = 10000
		clockPeriod = 1./clockFreq
		

		startIdx = []
		endIdx = []
		try :
			for chan in range(0,2):
				#currStartIdx = self.__getattr__('channel_%d_start_idx'%(chan)).data()
				#currEndIdx = self.__getattr__('channel_%d_end_idx'%(chan)).data()
				currStartIdx = 0
				currEndIdx = totSamples - 1
				startIdx.append(currStartIdx)
				endIdx.append(currEndIdx)
		except:
			print("Cannot read start idx or end idx")
			return 0


		#the following steps are performed for each acquired channel 
		educedRawChans = []
		for chan in range(0,2):
			actStartIdx = totSamples - pts + startIdx[chan]  #first index of the part of interest of the sample array
			actEndIdx = totSamples - pts  + endIdx[chan]   #last index of the part of interest of the sample array
		
			#make sure we do not exceed original array limits
			if actStartIdx < 0:
				actStartIdx = 0
			if actEndIdx > totSamples:
				actEndIdx = totSamples - 1

			#build reshaped array
			reducedRawChan = rawChan[chan][actStartIdx:actEndIdx]


			dim = Dimension(Window(startIdx[chan], endIdx[chan], trigTime), Range(None, None, clockPeriod))

			convExpr = Data.compile("10.* $VALUE/32768.")

			rawMdsData = Int16Array(reducedRawChan)

			rawMdsData.setUnits("Count")
			convExpr.setUnits("Volt")

			signal = Signal(convExpr, rawMdsData, dim)


			try:
				self.__getattr__('CH_0%d'%(chan+1)).putData(signal)
			except:
				print("Cannot write Signal in the tree")
				return 0




		
		return 1