import xmlrpclib, json, subprocess, os 

server = xmlrpclib.Server('http://localhost:20738/RPC2')
G = server.ubigraph
os.system("executeServer.py")
json_data = open("history.json")
data = json.load(json_data)
numberOfObjects = len(data)
counter = 0
prevNode = None
G.clear()
a = int(raw_input("Look at how many links in the past? --> "))


def cleanUrl(u):
	start = u.find("//")
	start+=2
	end = u.find("/",start)
	url = u[start:end]
	print url
	return url

while(counter<min(numberOfObjects,a)):
	if(counter == (numberOfObjects - 1)):
		x = G.new_vertex()
		node = data[counter]
		G.set_vertex_attribute(x,'label',cleanUrl(node['url']))
		G.set_vertex_attribute(x, 'color', '#0000ff')
		G.set_vertex_attribute(x, 'shape', 'sphere')
		G.new_edge(x,prevNode)
		prevNode = x
		# print node['id']
	elif(prevNode != None):										    	
		node = data[counter] 						    
		x = G.new_vertex()
		G.set_vertex_attribute(x,'label',cleanUrl(node['url']))
		G.set_vertex_attribute(x, 'color', '#ff0000')
		G.set_vertex_attribute(x, 'shape', 'sphere')
		G.new_edge(x,prevNode)
		prevNode = x
	elif(data[counter]!= None):
		node = data[counter]			
		x = G.new_vertex()
		G.set_vertex_attribute(x,'label',cleanUrl(node['url']))
		G.set_vertex_attribute(x, 'color', '#00ff00')
		G.set_vertex_attribute(x, 'shape', 'torus')
		prevNode = x
	counter+=1

