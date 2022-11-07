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


        if len(time) > 8:
            time = time[8:]
        elif len(time) == 7:
            time = f"0{time}"

        time = time[:5]
        return time

    def addPatient(self, name, time, room, obj):

        self.dict[name] = [time, room, obj]
        # False if treatment hasn't started - True if it has
        self.dict[name].append(False)
        print(self.dict[name][3])

    # Function for setting new time in the dictionary when time is added:
    def addTime(self, name, addtime, timercounternum):

        # Make sure you can't add time so the timer goes past 24 hours
        if timercounternum + (int(addtime)*60) >= 86400:
            pass

        # Combine the added time with the current time, make it into a string and replace the dict value
        else:
            timeInt = self.string2Min(self.dict[name][0])
            newTime = (timeInt + int(addtime))
            self.dict[name][0] = self.min2String(newTime)

    # Function for setting new time in the dictionary when time is subtracted:
    def subTime(self, name, negtime, timercounternum):

        # If user tries to subtract more time than the counter has left, just remove the time that's left
        if timercounternum - (int(negtime) * 60) <= 0:

            min = timercounternum//60
            timeInt = self.string2Min(self.dict[name][0])
            newTime = (timeInt - min)
            self.dict[name][0] = self.min2String(newTime)

         # If not, remove the time specified
        else:
            timeInt = self.string2Min(self.dict[name][0])
            newTime = (timeInt - int(negtime))
            self.dict[name][0] = self.min2String(newTime)

        #print(self.dict[name][0])

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



