import datetime

class Patients:

    def __init__(self):
        self.dict = {}

    def string2Min(self, time):

        hours, minutes = time.split(':')
        return int(minutes) + (int(hours) * 60)

    def min2String(self, minutes):

        sec = minutes * 60
        time = str(datetime.timedelta(minutes=minutes))
        time = time[:5]
        return time

    def addPatient(self, name, time, room, obj):

        self.dict[name] = [time, room, obj]

    def addTime(self, name, addtime):

        timeInt = self.string2Min(self.dict[name][0])
        newTime = (timeInt + int(addtime))
        self.dict[name][0] = self.min2String(newTime)

    def subTime(self, name, negtime):

        timeInt = self.string2Min(self.dict[name][0])
        newTime = (timeInt - int(negtime))
        self.dict[name][0] = self.min2String(newTime)

    def deletePatient(self, name):

        del self.dict[name]

    def print_dict(self):

        for element in self.dict:
             print(f"{element}: ",end='')

             for i in self.dict[element]:

                # Hvis siste yrket i rekka:
                 if i == self.dict[element] [ len(self.dict[element]) -1 ] and (len(self.dict[element]))!=1:
                     print(f' og {i}')

                # Hvis første yrket i rekka og mer enn ett yrke:
                 elif i == self.dict[element][0] and len(self.dict[element])!=1:
                     print(f'{i}', end='')

                # Hvis bare et yrke i rekka:
                 elif (len(self.dict[element])) == 1:
                     print(f'{i}')

                # Hvis yrket er midt i rekka:
                 else:
                     print(f', {i}', end='')



