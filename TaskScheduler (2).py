# This program is built based on Python3.6
# Problems would arise if you use Python2
# So please run this file on Python3, THANKS!

# I think this is a typical Hungarian Algorithm problem
# requiring me find the best matches for two groups.

# Build a analyst class to import the analysts' information
class Analyst(object):
    def __init__(self, analystName, taskTypeList):
        self.analystName = analystName
        self.analystPreference = taskTypeList

# Build a task class to import the tasks' information
class Task(object):
    def __init__(self, taskType=None, taskId=None, taskPriority=None):
        self.taskType = taskType
        self.taskId = taskId
        self.taskPrioroty = str(taskPriority).upper()
        self.priorityList = ['URGENT', 'HIGH', 'MEDIUM', 'LOW']
        # make sure assign the tasks according to priority
    def compare(self):
        return self.priorityList.index(self.taskPrioroty)# - self.priorityList.index(mTask.taskPrioroty)

# Build taskscheduler class
class TaskScheduler(object):
    def __init__(self, taskList:Task=None, analystList:Analyst=None):
        self.M = []
        self.visit = {}
        if taskList is not None:
            self.taskList = taskList
            self.analystList = analystList

            for analyst in analystList:
                self.visit[analyst.analystName] = len(analyst.analystPreference)
        else:
            self.taskList = []
            self.analystList = []

    def insertTask(self, type, id, priority):
        self.taskList.append(Task(type, id, priority))

    def insertAnalyst(self, analystName, taskTypeList):
        self.analystList.append(Analyst(analystName, taskTypeList))
        self.visit[analystName] = len(taskTypeList)
        
    def assign(self):
        mtaskList = sorted(self.taskList, key=Task.compare)
        manalystList = self.analystList[:]
        ttaskList = []
        matchMap = {}
        for eachAnalyst in manalystList:
            for eachTask in eachAnalyst.analystPreference:
                try:
                    matchMap[eachTask].append(eachAnalyst)
                except:
                    matchMap[eachTask] = [eachAnalyst]


        while 1:
            if not mtaskList:
                #
                break
            try:
                self.M.append((mtaskList[0].taskId, matchMap[mtaskList[0].taskType][0].analystName))
                self.visit[matchMap[mtaskList[0].taskType][0].analystName] -= 1
                matchMap[mtaskList[0].taskType].pop(0)
                mtaskList.pop(0)
            except:
                ttaskList.append(mtaskList[0])
                mtaskList.pop(0)
        if ttaskList:
            keylist = list(self.visit.keys())
            ind = 0
            while ind < len(keylist):
                if self.visit[keylist[ind]]:
                    self.M.append((ttaskList[0].taskId, keylist[ind]))
                    ttaskList.pop(0)
                    if ttaskList:
                        break
                else:
                    ind += 1
        while ttaskList:
            self.M.append((ttaskList[0].taskId, None))
            ttaskList.pop(0)
    def print(self):
        for each in self.M:
            print(each[0], '->', each[1])

# Import all the data and make sure the outcomes are what I want
if __name__ == '__main__':
    scheduler = TaskScheduler()
    scheduler.insertTask("TaskType1", "TaskID1","MEDIUM")
    scheduler.insertTask("TaskType1", "TaskID2", "URGENT")
    scheduler.insertTask("TaskType1", "TaskID3", "MEDIUM")
    scheduler.insertTask("TaskType2", "TaskID4", "HIGH")
    scheduler.insertTask("TaskType3", "TaskID5", "HIGH")

    scheduler.insertAnalyst("Analyst1", ["TaskType1", "TaskType2"])
    scheduler.insertAnalyst("Analyst2", ["TaskType1", ])
    scheduler.insertAnalyst("Analyst3", ["TaskType2"])

    scheduler.assign()
    scheduler.print()

# Although the outcomes are in different order with the example in
# the Python test file, but they are actually the same.
# Thank you!
