import os
import re

class data_preprocess():
    def __init__(self, directory):
        self.files, self.data = [], []
        self.target_dir = os.getcwd()+directory

        
    def __sort_file_path(self): # get sorted file
        for filename in os.listdir(self.target_dir):
            self.files.append(filename)

        # file sorted by its name
        self.files.sort(key=lambda f: int(re.sub('\D', '', f)))
        
    def __read_file(self):
        self.__sort_file_path()
        
        for filename in self.files:
            temp = []
            with open(os.path.join(self.target_dir, filename), 'r') as f:
                    temp += f.readlines()
            self.data.append(temp)
    
    def train_data(self): # for training data
        self.__read_file()
        train = []
        for i in range(len(self.data)):
            temp = []
            for item in self.data[i]:
                temp.append(item.split()[1:])
            train.append(temp)
            
        final = []   
        for j in range(len(train)):
            a = ''
            for i in range(len(train[j])):
                a += ' '.join(train[j][i]) +';'
            a = a[:-1]
            index = re.sub('\D', '', self.files[j])

            dic = {'UserId':index, 'Predicted': a}

            final.append(dic)
            
        return train, final
    
    def ego_data(self): # for ego data
        self.__read_file()
        
        fin, user = [], []

        for j in range(len(self.data)):
            temp, temp2 = [], []

            for i in range(len(self.data[j])):
                u, a = self.data[j][i].split(":")
                a = self.data[j][i].replace(":", '').split()
                temp.append([int(a[i]) for i in range(len(a))])
                temp2.append(int(u))
            fin.append(temp)
            user.append(temp2)
        return fin, user
    
    def edge_data(self, index):
        node, head = [], []
        for line in open(self.target_dir + "\\" + self.files[index]):
            e1, es = line.split(':')
            es = es.split()
            for e in es:
                if e == e1: continue
                node.append((int(e1),int(e)))
            head.append(e1)
                         
        e1 = re.sub('\D', '', self.files[index])
        for e in head:
            node.append((int(e1),int(e)))
        return node