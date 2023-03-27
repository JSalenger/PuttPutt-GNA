import time
from WindowSingleton import WindowSingleton
from graphics import update
from constants import K

class PopulateSorter:
    def __init__(self, id, populate):
        self.id = id
        self.populate = populate
        self.distances = {}

    def getScore(self, k, sortablePopulates):
        cousins = []
        l = list(self.distances.keys())

        for i in range(k):
            try:
                id_of_closest_ball = int(l[i].replace(str(self.id), ""))
            except ValueError:
                cousins.append(self)
                continue
            for j in sortablePopulates:
                if j.id == id_of_closest_ball:
                    cousins.append(j)
        
        avgSore = (self.populate.getScore().m + sum([v.populate.getScore().m for v in cousins])) / (k + 1)

        return avgSore



class GNA:
    def __init__(self, dt, familySizes, PopulateCLS, stdDev, callbacks=[], reverseScoring=False):
        # TODO: make pop size variable
        self.dt = dt
        self.totalTime = 0

        self.familySizes = familySizes
        self.PopulateCLS = PopulateCLS
        self.stdDev = stdDev
        self.callbacks = callbacks


        self.populates = []
        self.populationSize = sum(familySizes)
        self.populatesDead = 0

        self.reverseScoring = reverseScoring
        self.epoch = 0

        for _ in range(self.populationSize):
            p = self.PopulateCLS.createNew(self.dt)
            self.populates.append(p)

    def createNextGeneration(self):
        sortablePopulates = [PopulateSorter(k, v) for k, v in enumerate(self.populates)]

        sTime = time.time()

        for k, v in enumerate(sortablePopulates):
            v.id = k

        for j, v in enumerate(sortablePopulates):
            for i in sortablePopulates[j+1:]:
                # compute distances in remaining members
                dist = v.populate.startingVelocity - i.populate.startingVelocity
                if v.id < i.id:
                    name = str(v.id) + str(i.id)
                    v.distances[name] = dist
                    i.distances[name] = dist
                else:
                    name = str(i.id) + str(v.id)
                    v.distances[name] = dist
                    i.distances[name] = dist
            
            v.distances = {k: v for k, v in sorted(v.distances.items(), key=lambda item: item[1].m)}

        print("running time: " + str(time.time() - sTime))

        sortablePopulates.sort(
            key=lambda x: x.getScore(K, sortablePopulates), reverse=self.reverseScoring)

        # for x in sortablePopulates[:2]:
        #     x.populate.sphere.undraw()
        #     x.populate.sphere.setFill("red")
        #     x.populate.sphere.draw(WindowSingleton()())
        #     l = list(x.distances.keys())

        #     f_member_score = 0
        #     f_member_v = None

        #     for i in range(3):
        #         id_of_closest_ball = int(l[i].replace(str(x.id), ""))
        #         for j in sortablePopulates:
        #             if j.id == id_of_closest_ball:
        #                 j.populate.sphere.undraw()
        #                 j.populate.sphere.setFill("blue")
        #                 j.populate.sphere.draw(WindowSingleton()())
        #                 f_member_score = j.populate.getScore().m
        #                 f_member_v = j.populate.startingVelocity

        #     update()
            
        #     print("Populate score: " + str(x.populate.getScore().m))
        #     print("Populate Vel: " + str(x.populate.startingVelocity))
        #     print("Sample family member velocity: " + str(f_member_v))
        #     print("Sample family member score: " + str(f_member_score))
        #     print("Family Score: " + str(x.getScore(3, sortablePopulates)))
            
        #     WindowSingleton()().getMouse()

        #     x.populate.sphere.undraw()
        #     x.populate.sphere.setFill("white")
        #     x.populate.sphere.draw(WindowSingleton()())
        #     l = list(x.distances.keys())
        #     for i in range(10):
        #         id_of_closest_ball = int(l[i].replace(str(x.id), ""))
        #         for j in sortablePopulates:
        #             if j.id == id_of_closest_ball:
        #                 j.populate.sphere.undraw()
        #                 j.populate.sphere.setFill("white")
        #                 j.populate.sphere.draw(WindowSingleton()())

        #     update()

                

        tempPopulates = []
        for k, familySize in enumerate(self.familySizes, start=0):
            for _ in range(familySize):
                if k == 0:
                    tempPopulates.append(self.PopulateCLS.createFrom(sortablePopulates[k].populate, self.stdDev, color="red"))
                else:
                    tempPopulates.append(self.PopulateCLS.createFrom(sortablePopulates[k].populate, self.stdDev))


        print("-----")
        print("Epoch " + str(self.epoch) + " finished.")
        print("Best Velocity: " + str(self.populates[0].startingVelocity))

        shotTimes = []
        for i in self.populates:
            shotTimes.append(i.tT)

        print("Avg. Shot Time: " + str(sum(shotTimes)/len(shotTimes)))
        print("Max Shot Time: " + str(max(shotTimes)))
        print("Loss: " + str(sortablePopulates[0].getScore(K, sortablePopulates)))
        print("Worst loss: " + str(sortablePopulates[-1].getScore(K, sortablePopulates)))
        print("-----")

        self.epoch += 1
        self.populatesDead = 0
        self.populates = tempPopulates
    
    def __call__(self):
        for i in self.populates:
            died = i()  # could replace with just "if i()"
            if died:
                self.populatesDead += 1

        if self.populatesDead == self.populationSize:
            self.createNextGeneration()
            for x in self.callbacks:
                x(self)

        self.totalTime += self.dt
