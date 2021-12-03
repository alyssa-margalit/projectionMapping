# me - this DAT
# 

# Called when connection established
# dat - the OP which is cooking
def onConnect(dat):
	print('connect')
	
	return

# Called when connection failed
# dat - the OP which is cooking
# msg - reason for failure
def onConnectFailure(dat, msg):
	return

# Called when current connection lost
# dat - the OP which is cooking
# msg - reason for failure
def onConnectionLost(dat, msg):
	print('connection lost')
	return

# Called when server receives subscription request
# dat - the OP which is cooking
def onSubscribe(dat):
	return

# Called when subscription request fails.
# dat - the OP which is cooking
# msg - reason for failure
def onSubscribeFailure(dat, msg):
	return

# Called when server receives unsubscription request
# dat - the OP which is cooking
def onUnsubscribe(dat):
	return

# Called when unsubscription request fails.
# dat - the OP which is cooking
# msg - reason for failure
def onUnsubscribeFailure(dat, msg):
	return

# Called when server receives publish request
# dat - the OP which is cooking
def onPublish(dat):
	return

# Called when new content received from server
# dat - the OP which is cooking
# topic - topic name of the incoming message
# payload - payload of the incoming message
# qos - qos flag for of the incoming message
# retained - retained flag of the incoming message
# dup - dup flag of the incoming message
def onMessage(dat, topic, payload, qos, retained, dup):
	if topic == 'TopLx':
		print('TLx:',payload)
		x = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		x.par.value0 = payload
	elif topic == 'TopLy':
		print('TLy:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value1 = payload
	elif topic == 'TopRx':
		print('TRx:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value2 = payload
	elif topic == 'TopRy':
		print('TRy:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value3 = payload
	elif topic == 'TopLx':
		print('TLx:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value4 = payload
	elif topic == 'TopLy':
		print('TLy:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value5 = payload
	elif topic == 'TopRx':
		print('TRx:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value6 = payload
	elif topic == 'TopRy':
		print('TRy:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value7 = payload
	elif topic == 'fireworkx':
		print('fx:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value8 = payload
	elif topic == 'fireworky':
		print('fy:',payload)
		y = op('constant1')
		payload = str(payload)
		payload = float(payload[2:(len(payload)-1)])
		print(payload)
		y.par.value9 = payload
	return



	
