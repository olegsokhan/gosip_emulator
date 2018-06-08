import random
import sys

nParameter = 0
iParamter = 0
runMyAlgorithm = 0

for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-n":
        nParameter = int(sys.argv[i + 1])
    elif sys.argv[i] == "-i":
        iParamter = int(sys.argv[i + 1])
    elif sys.argv[i] == "--your-algorithm":
        runMyAlgorithm = 1

servers = []
sendFromToList = []

class Node:

    def __init__(self, index, ports):
        self.index = index
        self.msgsCache= []
        self.otherServerPorts = list(ports)
        del self.otherServerPorts[index]

    def setMsg(self, msg, fromNode):
        for i in range(0, len(self.msgsCache)):
            if self.msgsCache[i] == str(msg):
                return
        self.msgsCache.append(msg)

        serverIndexesToSendMesg = []
        while len(serverIndexesToSendMesg) < 4:
            randNum = random.choice(self.otherServerPorts)
            exists = 0
            for i in range(0, len(serverIndexesToSendMesg)):
                if serverIndexesToSendMesg[i] == randNum:
                    exists = 1
                    break
            if exists == 0:
                serverIndexesToSendMesg.append(randNum)
                sendFromToList.append(str(self.index) + "," + str(randNum)+","+str(msg))

class ImprovedNode:

    def __init__(self, index, ports):
        self.index = index
        self.msgsCache= []
        self.otherServerPorts = list(ports)
        del self.otherServerPorts[index]

    def setMsg(self, msg, fromNode):
        for i in range(0, len(self.msgsCache)):
            if self.msgsCache[i] == str(msg):
                return
        self.msgsCache.append(msg)

        serverIndexesToSendMesg = []
        while len(serverIndexesToSendMesg) < 4:
            randNum = random.choice(self.otherServerPorts)
            exists = 0
            for i in range(0, len(serverIndexesToSendMesg)):
                if serverIndexesToSendMesg[i] == randNum:
                    exists = 1
                    break
            if exists == 0 and randNum != int(fromNode):
                serverIndexesToSendMesg.append(randNum)
                sendFromToList.append(str(self.index) + "," + str(randNum)+","+str(msg))

notReceivedTimes = 0
iterations = 0
totalIterations = 0
for z in range(0, iParamter):
    servers = []
    sendFromToList = []

    if runMyAlgorithm == 1:
        for i in range(0, nParameter):
            servers.append(ImprovedNode(i, list(range(0, nParameter))))
        random.choice(servers).setMsg("msg", "-1")
    else:
        for i in range(0, nParameter):
            servers.append(Node(i, list(range(0, nParameter))))
        random.choice(servers).setMsg("msg", "-1")

    while len(sendFromToList) > 0:
        iterations += 1
        tmpList = list(sendFromToList)
        sendFromToList = []
        for i in range(0, len(tmpList)):
            data = str(tmpList[i]).split(",")
            servers[int(data[1])].setMsg(data[2], data[0])
    for p in range(0, len(servers)):
        if(len(servers[p].msgsCache) == 0):
            notReceivedTimes+=1
    totalIterations += iterations
    iterations = 0

print("Total qty of iterations: " + str(totalIterations)+", average qty of iterations: " + str(totalIterations / iParamter))
print("In " + str(100 - (notReceivedTimes / iParamter * 100)) + "% cases all nodes received the packet")