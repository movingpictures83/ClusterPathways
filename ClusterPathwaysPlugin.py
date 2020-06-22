import sys
import random
random.seed(1234)

class ClusterPathwaysPlugin:
   def input(self, inputfile):
      params = open(inputfile, 'r')
      self.parameters = dict()
      for line in params:
         contents = line.strip().split('\t')
         self.parameters[contents[0]] = contents[1]
      self.noafile = open(self.parameters['noafile'], 'r')
      self.pathwayfile = open(self.parameters['pathways'], 'r')

   def run(self):
      pass

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      junk = self.noafile.readline()  # first line
      bacteria = []
      clustermap = dict()
      for line in self.noafile:
         info = line.split('\t')
         bac = info[0]
         cluster = int(info[1].strip())
         bacteria.append(bac)
         clustermap[bac] = cluster

      sameclusters = dict()

      for line in self.pathwayfile:
         pathwayname = line[line.find(':')+1:line.find('INVOLVES')]
         #print "PATHWAY: ", pathwayname
         myline = line.strip()
         myline = myline[myline.find('INVOLVES:')+9:]
         elements = myline.split('\t')
         while (elements.count('') != 0):
            elements.remove('')
         bioelements = []
         for item in elements:
            for entry in bacteria:
              try:
               if (item[0] == 'X' and item[1].isdigit()):
                if (entry == item):
                  bioelements.append(entry)
               elif (entry.find(item) != -1):
                  bioelements.append(entry)
              except:
                 print(item)
                 raw_input()
            for i in range(len(bioelements)):
               for j in range(i+1, len(bioelements)):
                  elementi = bioelements[i]
                  elementj = bioelements[j]
                  if (elementi != elementj and clustermap[elementi] == clustermap[elementj]):
                        if (elementi > elementj):
                           temp = elementi
                           elementi = elementj
                           elementj = temp
                        if ((elementi, elementj) not in sameclusters):
                           sameclusters[(elementi, elementj)] = set()
                        sameclusters[(elementi, elementj)].add(pathwayname)
      
      for key in sameclusters:
         sameclusters[key] = list(sameclusters[key])
         sameclusters[key].sort()

      #print sameclusters
      outfile.write("IN SAME CLUSTER:"+"\n")
      for elementpair in sameclusters.keys():
         outfile.write(str(elementpair)+" CLUSTER: "+str(clustermap[elementpair[0]])+" \nPATHWAYS: ")
         for pathway in sameclusters[elementpair]:
            outfile.write(pathway+" "+'\n')
         outfile.write('\n')
