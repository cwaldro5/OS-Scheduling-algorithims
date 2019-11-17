class process:
    def __init__(self, id, arrivalTime, priority, burstTime):
        self.id = id
        self.arrivalTime = arrivalTime
        self.priority = priority
        self.burstTime = burstTime
    
def nonPSJF(processList):
    readyQueue = []
    time = 0
    count = 0
    shortestIndex = 0
     
    lenReady = len(readyQueue)
    lenProcess = len(processList)
    while lenReady > 0 or lenProcess > 0:
        for i in range(len(processList)):
            if int(processList[i].arrivalTime) <= time:
                readyQueue.append(processList[i])
                count = count + 1   
            
        processList = processList[count:]
        count = 0
        shortestProcess = readyQueue[0]
        for i in range(len(readyQueue)):
            if int(readyQueue[i].burstTime) < int(shortestProcess.burstTime):
                shortestProcess = readyQueue[i]
                shortestIndex = i
        
        print("At time " + str(time) + " ms, CPU starts running process " + shortestProcess.id)
        time = time + int(shortestProcess.burstTime)
        if lenReady == 1 and lenProcess == 0:
            readyQueue.pop(0)
        else:
            readyQueue.pop(shortestIndex)
        lenReady = len(readyQueue)
        lenProcess = len(processList)

    print("End of the results of nonpreemptive SJF")
    print("\n")
            
def nonPPriority(processList):
    readyQueue = []
    time = 0
    count = 0
    highestIndex = 0
     
    lenReady = len(readyQueue)
    lenProcess = len(processList)
    while lenReady > 0 or lenProcess > 0:
        for i in range(len(processList)):
            if int(processList[i].arrivalTime) <= time:
                readyQueue.append(processList[i])
                count = count + 1   
            
        processList = processList[count:]
        count = 0
        highestPriority = readyQueue[0]
        for i in range(len(readyQueue)):
            if int(readyQueue[i].priority) > int(highestPriority.priority):
                highestPriority = readyQueue[i]
                highestIndex = i
        
        print("At time " + str(time) + " ms, CPU starts running process " + highestPriority.id + " with priority " + str(highestPriority.priority))
        time = time + int(highestPriority.burstTime)
        if lenReady == 1 and lenProcess == 0:
            readyQueue.pop(0)
        else:
            readyQueue.pop(highestIndex)
        lenReady = len(readyQueue)
        lenProcess = len(processList)

    print("End of the results of nonpreemptive SJF")
    print("\n")


def roundRobin(processList):
    readyQueue = []
    time = 0
    count = 0
     
    lenReady = len(readyQueue)
    lenProcess = len(processList)
    while lenReady > 0 or lenProcess > 0:
        for i in range(len(processList)):
            if int(processList[i].arrivalTime) <= time:
                readyQueue.append(processList[i])
                count = count + 1   
            
        processList = processList[count:]
        count = 0
        currentProcess = readyQueue.pop(0)

        if int(currentProcess.burstTime) > 10:
            print("At time " + str(time) + " ms, CPU starts running process " + currentProcess.id)
            time = time + 10
            currentProcess.burstTime = int(currentProcess.burstTime) - 10
            readyQueue.append(currentProcess)
        else:
            print("At time " + str(time) + " ms, CPU starts running process " + currentProcess.id)
            time = time + int(currentProcess.burstTime)
        #if lenReady == 1 and lenProcess == 0:
         #   readyQueue.pop(0)
        #else:
          #  readyQueue.pop(shortestIndex)
        lenReady = len(readyQueue)
        lenProcess = len(processList)

    print("End of the results of nonpreemptive SJF")
    print("\n")

if __name__ == "__main__":
    source = open("processes.txt", "rt")
    input = source.read()
    source.close()
    variablesList = []

    variablesList = input.split(", ")

    p1 = process(variablesList[0], variablesList[1], variablesList[2], variablesList[3])
    p2 = process(variablesList[4], variablesList[5], variablesList[6], variablesList[7])
    p3 = process(variablesList[8], variablesList[9], variablesList[10], variablesList[11])
    p4 = process(variablesList[12], variablesList[13], variablesList[14], variablesList[15])
    p5 = process(variablesList[16], variablesList[17], variablesList[18], variablesList[19])
    p6 = process(variablesList[20], variablesList[21], variablesList[22], variablesList[23])
    
    processList = [p1, p2, p3, p4, p5, p6]
    nonPSJF(processList)
    nonPPriority(processList)
    roundRobin(processList)