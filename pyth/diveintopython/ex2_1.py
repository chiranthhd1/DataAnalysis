def buildConnectString(paramas):
	"""Build a connection string from a dictionary of parameters.
	returns string"""
	return ";".join(["%s=%s" %(k,v) for k , v in paramas.items()])

if __name__ == "__main__":
	myParams = {"server":"Mpilgrim",
		    "database":"master",
		    "uid":"sa",
		    "pwd":"secret"	
			}
	print buildConnectString(myParams)

print buildConnectString.__doc__





