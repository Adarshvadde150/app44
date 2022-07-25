import pymongo as pm
client=pm.MongoClient()
mdb=client['account']
class Db(dict):
    def __init__(self):
          self.d=dict()
    def insert_one(self,keyvalues):
            mdb.adarsh.insert_one(keyvalues)
    def find(self,key,password):
        data=mdb.adarsh.find()
        dict1=[]
        dict2=[]
        for data1 in data:
            dict1.append(data1)
        for i in dict1:
            i=i
            for all in i:
                if all==key:
                   dict2.append(i[key])
        for j in dict2:
            j=j
            for al in j:
                if al==password:
                    details1=j[al]
        id=mdb.adarsh.find({key:{password:details1}})
        for i in id:
            id=i['_id']
        return details1,id
    def update(self,id,key,value):
        self.id=id
        self.key=key
        self.value=value
        mdb.adarsh.update_one({'_id':self.id},{'$set':{self.key:self.value}})
    def name(self):
        name=mdb.adarsh.find()
        namelist=[]
        for i in name:
            for name1 in i:
                if name1=='_id':
                    None
                else:
                   namelist.append(name1)
        return namelist
    def password(self,):
        data = mdb.adarsh.find()
        dict1 = []
        dict2 = []
        passwordlist=[]
        for data1 in data:
            dict1.append(data1)
        for i in dict1:
            i = i
            for all in i:
                if all == '_id':
                    None
                else:
                    dict2.append(i[all])
        for j in dict2:
            j = j
            for al in j:
                 passwordlist.append(al)
        return passwordlist
    def idid(self):
        self.data1=mdb.adarsh.find()
        id=[]
        for i in self.data1:
            id.append(i['_id'])
        return id
class verify(dict):
    def __init__(self):
          self.d=dict()
    def verify1(self,name,email,password,otp):
        self.d['name']=name
        self.d['email']=email
        self.d['password']=password
        self.d['otp']=otp
    def verify2(self,key):
        if key in self.d:
            for keys in self.d:
                if key==keys:
                    value=self.d[key]
        return value
class Account(dict):
    def __init__(self):
          self.da=dict()
    def account1(self,name,password):
        self.da['name']=name
        self.da['password']=password
        self.da['_id']=name+password
    def account2(self,key):
        if key in self.da:
            for keys in self.da:
                if key==keys:
                    value=self.da[key]
        return value

class friendaccounts(dict):
    def __init__(self):
          self.d=dict()
    def insert_one(self,keyvalues):
        for key in keyvalues:
            self.d[key]=keyvalues[key]
        return self.d
    def find(self,key):
        self.data=self.d
        if key in self.data:
            for keys in self.data:
                if key==keys:
                    value=self.data[key]
        return value
class find(dict):
    def __init__(self):
          self.data=[]
    def find(self,key):
        self.data1=mdb.adarsh.find({'_id':key})
        for i in self.data1:
            return i
