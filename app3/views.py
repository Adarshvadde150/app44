from .objects import image_object,image_object1,alldata
from django.shortcuts import render
import sendgrid
from .db import Db,Account,verify,friendaccounts,find
database=Db()
verifys=verify()
accounts=Account()
friendsaccount=friendaccounts()
find=find()
def mainpage(request):
    if request.method == 'POST':
        all=request.POST
        keys=['csrfmiddlewaretoke','loginname','password']
        key=len(keys)
        keyvalue=[]
        for samekeys1 in all:
            keyvalues=keyvalue.append(samekeys1)
        if len(keyvalue)==key:
            for i in range(key) :
                if keyvalue[i]==keys[i]:
                    name=all['loginname']
                    password=all['password']
                    accounts.account1(name,password)
                    name=accounts.account2('name')
                    password=accounts.account2('password')
                    names=database.name()
                    passwords=database.password()
                    length=len(names)
                    for i in range(length):
                        if name == names[i]:
                            if password == passwords[i]:
                                details,mainid=database.find(name,password)
                                profileimage=details[0]
                                profileimage=profileimage['profileimage']
                                profiledetails = details[1]
                                profiledetails = profiledetails['profiledetails']
                                uploads=details[2]
                                uploads=uploads['uploads']
                                friends=details[3]
                                friends=friends['friends']
                                alldetails=profiledetails
                                alldetails['profile']=profileimage
                                alldetails['image']=uploads
                                alldetails['friends']=friends
                                friendsaccount.insert_one(friends)
                                for i in friends:
                                    data=friendsaccount.find(i)
                                    data=find.find(i+data)
                                    for data6 in data:
                                        name2=data6
                                    name=data[name2]
                                    for password in name:
                                        password1=password
                                    details =database.find(name2,password1)
                                    profiledetails = details[1]
                                    profiledetails = profiledetails['profiledetails']
                                    profileimage = details[0]
                                    profileimage = profileimage['profileimage']
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    friends = details[3]
                                    friends = friends['friends']
                                    all1= profiledetails
                                    all1['profile'] = profileimage
                                    all1['image'] = uploads
                                    all1['friends'] = friends
                                allids=database.idid()
                                length=len(allids)
                                data1=[]
                                for i in range(length):
                                    recamand=allids[i]
                                    data = find.find(recamand)
                                    for data6 in data:
                                        name2 = data6
                                    name = data[name2]
                                    for password in name:
                                        password1 = password
                                    details,id = database.find(name2, password1)
                                    if mainid==id:
                                        None
                                    else:
                                        profileimage = details[0]
                                        profileimage = profileimage['profileimage']
                                        profiledetails = details[1]
                                        profiledetails = profiledetails['profiledetails']
                                        emailid=profiledetails['email']
                                        uploads = details[2]
                                        uploads = uploads['uploads']
                                        friends = details[3]
                                        friends = friends['friends']
                                        all1 = profiledetails
                                        all1['profile'] = profileimage
                                        all1['image'] = uploads
                                        all1['friends'] = friends
                                        data1.append({i+1:[all1,{name2:emailid}]})
                                alldetails['sergesions']=data1
                                return render(request, 'homepage.html',alldetails)
                            else:
                                return render(request,'login.html')

        keys=['csrfmiddlewaretoke','name','email','password']
        key=len(keys)
        keyvalue=[]
        for samekeys1 in all:
            keyvalues=keyvalue.append(samekeys1)
        if len(keyvalue)==key:
            for i in range(key) :
                name=all['name']
                email=all['email']
                password=all['password']
                length=str(email)
                lengthemail=len(length)
                for otpno in range(lengthemail*245):
                    otp=str(otpno)
                verifys.verify1(name,email,password,otp)
                sg = sendgrid.SendGridAPIClient("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")
                data = {
                   "personalizations": [
                  {
                    "to": [
                        {
                            "email": email
                        }
                    ],
                    "subject": "login verification"
                  }
                  ],
                   "from": {
                  "email": "vaddeadarsh150@gmail.com"
                  },
                  "content": [
                  {
                    "type": "text/plain",
                    "value": "your login verification code is -->   " + otp
                  }
                  ]
                  }
                sg.client.mail.send.post(request_body=data)
                if keyvalue[i]==keys[i]:
                    return render(request,'verify.html')
        keys=['csrfmiddlewaretoke','username','conemail','conpassword','otp']
        key=len(keys)
        keyvalue=[]
        for samekeys1 in all:
            keyvalue.append(samekeys1)
        if len(keyvalue)==key:
            for i in range(key) :
                if keyvalue[i]==keys[i]:
                    username=all['username']
                    conemail=all['conemail']
                    conpassword=all['conpassword']
                    conotp=all['otp']
                    name=verifys.verify2('name')
                    email=verifys.verify2('email')
                    password=verifys.verify2('password')
                    otp=verifys.verify2('otp')
                    names=database.name()
                    password1=database.password()
                    ids=database.idid()
                    length=len(names)
                    for i in range(length):
                        if name!=names[i]:
                            #if password!=password[i]:
                                if name==username and conemail==email and  conpassword==password and conotp==otp:
                                    accounts.account1(username,conpassword)
                                    if username+conemail in ids:
                                        return render(request,'verify.html',{'content':'Name and Email already existed '})
                                    else:
                                        database.insert_one({username:{password:[{'profileimage':"""iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAADAFBMVEWcnJzJyckAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBT53eAAACg0lEQVR4nO3bQW7DMAxEUev+ly4QdBGkdiSSQ3FKzd/GpvQWBYxavkaTruoNoBKELUHYEoQtQdgShC1B2BKELUHYEoQtQdgShC1B2BKELUHYEoQtQdgShK1UyPVe5kIjD3Ldl7TayIE8IHIx+LETRhYFPHRBkWSBTlxmJFCQ80wOtAQ3zshAU1DDHAwsBTTK6QBKMJPcDpwEMSjAwFEAY4IOkCQ+JezASMJDAA6IJDoD4kBIgiNADoBEEKwjLgkNADrCksj9UEdUIgjcEZQwQWJ/r0SOGkiCIyQ5HpLiiEgEYZM478xyCOKEpDn8EkEEYYIkOtwSQQQRBA9JdXglgggiiCCCCCKIIIJwQdo8/QoiiCCFEqdDEEG4IG3ej/SBtHmHqLe6dJA2Jx/6QNqcDupzXqvPCbo2Zxr7QNqc++1zErvP2fg+kDbfj4AkcYe+sXofweDQd4gfU6oZKEibb3XdEtDqAwdxUWBrDyTELsEtPaAQIwW58ABDDBTssgMOWaSgFx0JkDG1JKw4ciCvuTsRrwXzRn9oMhcayZCdCcKWIGwJwpYgbGVC/v8jSoen36khS4McZ0DgMbj/K3lDrY+ZEguyBcSMeIBNECggFpY3VmEKz1vdIIXp5EOIwnU6KEAhO3jml9Adl/VS+M7GOyWOe9IZLorjjj1lQzYx7BTr5TtLhGx12CS2i3eXBNnusEgsl1aEh5QwDJTl6+qCQgodi5LDIKWONcnaRdWBINWMa0WycglDAEg14TdByBxTyfR3ngQhc0wkk1+5EqR64386HVK97ZvOhlRv+raTIdVbfkgQtsyQ6g0/JghbRkj1dr8kCFtnQqo3+zVB2BKErdsd/wCoZWRKJcmHUAAAAABJRU5ErkJggg==
"""},
                                         {'profiledetails':{'id':name,'name':name,'bod':'06/06/2002','address':'chandrapalli','email':conemail,'number':8328267589}},
                                         {'uploads':[]},
                                         {'friends':{}},
                                         {'friendsrequest':[{'4':4}]}
                                         ]},'_id':name+email})
                                        names = database.name()
                                        passwords = database.password()
                                        length = len(names)
                                        for i in range(length):
                                            if name == names[i]:
                                                if password == passwords[i]:
                                                    details, id = database.find(name, password)
                                                    profileimage = details[0]
                                                    profileimage = profileimage['profileimage']
                                                    alldetails = dict()
                                                    alldetails['profile'] = profileimage
                                                    alldetails['name']=name
                                        return render(request,'image.html',alldetails)
                                else:
                                    return render(request,'verify.html')


        keys=['csrfmiddlewaretoke','myfile']
        key=len(keys)
        keyvalue=[]
        for samekeys1 in all:
            keyvalue.append(samekeys1)
        if len(keyvalue)==key:
            for i in range(key) :
                if keyvalue[i]==keys[i]:
                    name=accounts.account2('name')
                    password=accounts.account2('password')
                    names = database.name()
                    passwords = database.password()
                    length = len(names)
                    for i in range(length):
                        if name == names[i]:
                            if password == passwords[i]:
                                details, mainid = database.find(name, password)
                                profileimage = details[0]
                                profileimage = profileimage['profileimage']
                                profiledetails = details[1]
                                profiledetails = profiledetails['profiledetails']
                                uploads = details[2]
                                uploads = uploads['uploads']
                                friends = details[3]
                                friends = friends['friends']
                                length = len(friends)
                                alldetails = profiledetails
                                alldetails['profile'] = profileimage
                                alldetails['image'] = uploads
                                alldetails['friends'] = friends
                                friendsaccount.insert_one(friends)
                                for i in friends:
                                    data = friendsaccount.find(i)
                                    data = find.find(i + data)
                                    for data6 in data:
                                        name2 = data6
                                    name = data[name2]
                                    for password in name:
                                        password1 = password
                                    details = database.find(name2, password1)
                                    profiledetails = details[1]
                                    profiledetails = profiledetails['profiledetails']
                                    profileimage = details[0]
                                    profileimage = profileimage['profileimage']
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    friends = details[3]
                                    friends = friends['friends']
                                    all1 = profiledetails
                                    all1['profile'] = profileimage
                                    all1['image'] = uploads
                                    all1['friends'] = friends
                                allids = database.idid()
                                length = len(allids)
                                data1 = []
                                for i in range(length):
                                    recamand = allids[i]
                                    data = find.find(recamand)
                                    for data6 in data:
                                        name2 = data6
                                    name = data[name2]
                                    for password in name:
                                        password1 = password
                                    details, id = database.find(name2, password1)
                                    if mainid == id:
                                        None
                                    else:
                                        profileimage = details[0]
                                        profileimage = profileimage['profileimage']
                                        profiledetails = details[1]
                                        profiledetails = profiledetails['profiledetails']
                                        emailid = profiledetails['email']
                                        uploads = details[2]
                                        uploads = uploads['uploads']
                                        friends = details[3]
                                        friends = friends['friends']
                                        all1 = profiledetails
                                        all1['profile'] = profileimage
                                        all1['image'] = uploads
                                        all1['friends'] = friends
                                        data1.append({i + 1: [all1, {name2: emailid}]})
                                alldetails['sergesions'] = data1
                                return render(request,'homepage.html',alldetails)

        if request.FILES.get('pro') is not None:
            name = accounts.account2('name')
            password = accounts.account2('password')
            details, _id = database.find(name, password)
            details, id1 = database.find(name, password)
            if _id == id1:
                names = database.name()
                passwords = database.password()
                length = len(names)
                for i in range(length):
                    if name == names[i]:
                        if password == passwords[i]:
                            profileimage=request.FILES.get('pro')
                            profile = image_object(profileimage)
                            database.update(_id, name + "." + password + ".0.profileimage", profile)
                            details, mainid = database.find(name, password)
                            profileimage = details[0]
                            profileimage = profileimage['profileimage']
                            profiledetails = details[1]
                            profiledetails = profiledetails['profiledetails']
                            uploads = details[2]
                            uploads = uploads['uploads']
                            friends = details[3]
                            friends = friends['friends']
                            length = len(friends)
                            alldetails = profiledetails
                            alldetails['profile'] = profileimage
                            alldetails['image'] = uploads
                            alldetails['friends'] = friends
                            friendsaccount.insert_one(friends)
                            for i in friends:
                                data = friendsaccount.find(i)
                                data = find.find(i + data)
                                for data6 in data:
                                    name2 = data6
                                name = data[name2]
                                for password in name:
                                    password1 = password
                                details = database.find(name2, password1)
                                profiledetails = details[1]
                                profiledetails = profiledetails['profiledetails']
                                profileimage = details[0]
                                profileimage = profileimage['profileimage']
                                uploads = details[2]
                                uploads = uploads['uploads']
                                friends = details[3]
                                friends = friends['friends']
                                all1 = profiledetails
                                all1['profile'] = profileimage
                                all1['image'] = uploads
                                all1['friends'] = friends
                            allids = database.idid()
                            length = len(allids)
                            data1 = []
                            for i in range(length):
                                recamand = allids[i]
                                data = find.find(recamand)
                                for data6 in data:
                                    name2 = data6
                                name = data[name2]
                                for password in name:
                                    password1 = password
                                details, id = database.find(name2, password1)
                                if mainid == id:
                                    None
                                else:
                                    profileimage = details[0]
                                    profileimage = profileimage['profileimage']
                                    profiledetails = details[1]
                                    profiledetails = profiledetails['profiledetails']
                                    emailid = profiledetails['email']
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    friends = details[3]
                                    friends = friends['friends']
                                    all1 = profiledetails
                                    all1['profile'] = profileimage
                                    all1['image'] = uploads
                                    all1['friends'] = friends
                                    data1.append({i + 1: [all1, {name2: emailid}]})
                            alldetails['sergesions'] = data1
            return render(request, 'homepage.html', alldetails)

        keys=['csrfmiddlewaretoke','proimage']
        key=len(keys)
        keyvalue=[]
        for samekeys1 in all:
            keyvalue.append(samekeys1)
        if len(keyvalue)==key:
            for i in range(key) :
                if keyvalue[i]==keys[i]:
                    name=accounts.account2('name')
                    password=accounts.account2('password')
                    names = database.name()
                    passwords = database.password()
                    length = len(names)
                    for i in range(length):
                        if name == names[i]:
                            if password == passwords[i]:
                                details, mainid = database.find(name, password)
                                profileimage = details[0]
                                profileimage = profileimage['profileimage']
                                profiledetails = details[1]
                                profiledetails = profiledetails['profiledetails']
                                uploads = details[2]
                                uploads = uploads['uploads']
                                friends = details[3]
                                friends = friends['friends']
                                length = len(friends)
                                alldetails = profiledetails
                                alldetails['profile'] = profileimage
                                alldetails['image'] = uploads
                                alldetails['friends'] = friends
                                friendsaccount.insert_one(friends)
                                for i in friends:
                                    data = friendsaccount.find(i)
                                    data = find.find(i + data)
                                    for data6 in data:
                                        name2 = data6
                                    name = data[name2]
                                    for password in name:
                                        password1 = password
                                    details = database.find(name2, password1)
                                    profiledetails = details[1]
                                    profiledetails = profiledetails['profiledetails']
                                    profileimage = details[0]
                                    profileimage = profileimage['profileimage']
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    friends = details[3]
                                    friends = friends['friends']
                                    all1 = profiledetails
                                    all1['profile'] = profileimage
                                    all1['image'] = uploads
                                    all1['friends'] = friends
                                allids = database.idid()
                                length = len(allids)
                                data1 = []
                                for i in range(length):
                                    recamand = allids[i]
                                    data = find.find(recamand)
                                    for data6 in data:
                                        name2 = data6
                                    name = data[name2]
                                    for password in name:
                                        password1 = password
                                    details, id = database.find(name2, password1)
                                    if mainid == id:
                                        None
                                    else:
                                        profileimage = details[0]
                                        profileimage = profileimage['profileimage']
                                        profiledetails = details[1]
                                        profiledetails = profiledetails['profiledetails']
                                        emailid = profiledetails['email']
                                        uploads = details[2]
                                        uploads = uploads['uploads']
                                        friends = details[3]
                                        friends = friends['friends']
                                        all1 = profiledetails
                                        all1['profile'] = profileimage
                                        all1['image'] = uploads
                                        all1['friends'] = friends
                                        data1.append({i + 1: [all1, {name2: emailid}]})
                                alldetails['sergesions'] = data1
                    return render(request,'homepage.html',alldetails)
        keys=['csrfmiddlewaretoke','id','name','bod','address','email','number']
        key=len(keys)
        keyvalue=[]
        for samekeys1 in all:
            keyvalue.append(samekeys1)
        if len(keyvalue)==key:
            for i in range(key) :
                if keyvalue[i]==keys[i]:
                   name=accounts.account2('name')
                   password=accounts.account2('password')
                   details,_id=database.find(name,password)
                   details,id1=database.find(name,password)
                   if _id==id1:
                       names = database.name()
                       passwords = database.password()
                       length = len(names)
                       for i in range(length):
                           if name == names[i]:
                               if password == passwords[i]:
                                   id, name1, bod, address, email1, number = alldata(all)
                                   data = {'id': id, 'name': name1, 'bod': bod, 'address': address, 'email': email1,
                                           'number': number}
                                   database.update(_id, name + "." + password + ".1.profiledetails", data)
                                   details, mainid = database.find(name, password)
                                   profileimage = details[0]
                                   profileimage = profileimage['profileimage']
                                   profiledetails = details[1]
                                   profiledetails = profiledetails['profiledetails']
                                   uploads = details[2]
                                   uploads = uploads['uploads']
                                   friends = details[3]
                                   friends = friends['friends']
                                   length = len(friends)
                                   alldetails = profiledetails
                                   alldetails['profile'] = profileimage
                                   alldetails['image'] = uploads
                                   alldetails['friends'] = friends
                                   friendsaccount.insert_one(friends)
                                   for i in friends:
                                       data = friendsaccount.find(i)
                                       data = find.find(i + data)
                                       for data6 in data:
                                           name2 = data6
                                       name = data[name2]
                                       for password in name:
                                           password1 = password
                                       details = database.find(name2, password1)
                                       profiledetails = details[1]
                                       profiledetails = profiledetails['profiledetails']
                                       profileimage = details[0]
                                       profileimage = profileimage['profileimage']
                                       uploads = details[2]
                                       uploads = uploads['uploads']
                                       friends = details[3]
                                       friends = friends['friends']
                                       all1 = profiledetails
                                       all1['profile'] = profileimage
                                       all1['image'] = uploads
                                       all1['friends'] = friends
                                   allids = database.idid()
                                   length = len(allids)
                                   data1 = []
                                   for i in range(length):
                                       recamand = allids[i]
                                       data = find.find(recamand)
                                       for data6 in data:
                                           name2 = data6
                                       name = data[name2]
                                       for password in name:
                                           password1 = password
                                       details, id = database.find(name2, password1)
                                       if mainid == id:
                                           None
                                       else:
                                           profileimage = details[0]
                                           profileimage = profileimage['profileimage']
                                           profiledetails = details[1]
                                           profiledetails = profiledetails['profiledetails']
                                           emailid = profiledetails['email']
                                           uploads = details[2]
                                           uploads = uploads['uploads']
                                           friends = details[3]
                                           friends = friends['friends']
                                           all1 = profiledetails
                                           all1['profile'] = profileimage
                                           all1['image'] = uploads
                                           all1['friends'] = friends
                                           data1.append({i + 1: [all1, {name2: emailid}]})
                                   alldetails['sergesions'] = data1
                               return render(request, 'homepage.html',alldetails)
        if request.FILES is not None:
                uploadfile=request.FILES.get('myfile')
                profileimage=request.FILES.get('proimage')
                if profileimage is not None and uploadfile is None:
                    name=accounts.account2('name')
                    password=accounts.account2('password')
                    details, _id = database.find(name, password)
                    details, id1 = database.find(name, password)
                    if _id == id1:
                        names = database.name()
                        passwords = database.password()
                        length = len(names)
                        for i in range(length):
                            if name == names[i]:
                                if password == passwords[i]:
                                    profile = image_object(profileimage)
                                    database.update(_id, name + "." + password + ".0.profileimage", profile)
                                    details, mainid = database.find(name, password)
                                    profileimage = details[0]
                                    profileimage = profileimage['profileimage']
                                    profiledetails = details[1]
                                    profiledetails = profiledetails['profiledetails']
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    friends = details[3]
                                    friends = friends['friends']
                                    length = len(friends)
                                    alldetails = profiledetails
                                    alldetails['profile'] = profileimage
                                    alldetails['image'] = uploads
                                    alldetails['friends'] = friends
                                    friendsaccount.insert_one(friends)
                                    for i in friends:
                                        data = friendsaccount.find(i)
                                        data = find.find(i + data)
                                        for data6 in data:
                                            name2 = data6
                                        name = data[name2]
                                        for password in name:
                                            password1 = password
                                        details = database.find(name2, password1)
                                        profiledetails = details[1]
                                        profiledetails = profiledetails['profiledetails']
                                        profileimage = details[0]
                                        profileimage = profileimage['profileimage']
                                        uploads = details[2]
                                        uploads = uploads['uploads']
                                        friends = details[3]
                                        friends = friends['friends']
                                        all1 = profiledetails
                                        all1['profile'] = profileimage
                                        all1['image'] = uploads
                                        all1['friends'] = friends
                                    allids = database.idid()
                                    length = len(allids)
                                    data1 = []
                                    for i in range(length):
                                        recamand = allids[i]
                                        data = find.find(recamand)
                                        for data6 in data:
                                            name2 = data6
                                        name = data[name2]
                                        for password in name:
                                            password1 = password
                                        details, id = database.find(name2, password1)
                                        if mainid == id:
                                            None
                                        else:
                                            profileimage = details[0]
                                            profileimage = profileimage['profileimage']
                                            profiledetails = details[1]
                                            profiledetails = profiledetails['profiledetails']
                                            emailid = profiledetails['email']
                                            uploads = details[2]
                                            uploads = uploads['uploads']
                                            friends = details[3]
                                            friends = friends['friends']
                                            all1 = profiledetails
                                            all1['profile'] = profileimage
                                            all1['image'] = uploads
                                            all1['friends'] = friends
                                            data1.append({i + 1: [all1, {name2: emailid}]})
                                    alldetails['sergesions'] = data1
                    return render(request, 'homepage.html', alldetails)
                if uploadfile is not None and profileimage is None:
                    name=accounts.account2('name')
                    password=accounts.account2('password')
                    details, _id = database.find(name, password)
                    details, id1 = database.find(name, password)
                    if _id == id1:
                        names = database.name()
                        passwords = database.password()
                        length = len(names)
                        for i in range(length):
                            if name == names[i]:
                                if password == passwords[i]:
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    lengthupload = len(uploads)
                                    increment = str(lengthupload)
                                    upload = image_object1(uploadfile)
                                    database.update(_id, name + "." + password + ".2.uploads." + increment, upload)
                                    details, mainid = database.find(name, password)
                                    profileimage = details[0]
                                    profileimage = profileimage['profileimage']
                                    profiledetails = details[1]
                                    profiledetails = profiledetails['profiledetails']
                                    uploads = details[2]
                                    uploads = uploads['uploads']
                                    friends = details[3]
                                    friends = friends['friends']
                                    length = len(friends)
                                    alldetails = profiledetails
                                    alldetails['profile'] = profileimage
                                    alldetails['image'] = uploads
                                    alldetails['friends'] = friends
                                    friendsaccount.insert_one(friends)
                                    for i in friends:
                                        data = friendsaccount.find(i)
                                        data = find.find(i + data)
                                        for data6 in data:
                                            name2 = data6
                                        name = data[name2]
                                        for password in name:
                                            password1 = password
                                        details = database.find(name2, password1)
                                        profiledetails = details[1]
                                        profiledetails = profiledetails['profiledetails']
                                        profileimage = details[0]
                                        profileimage = profileimage['profileimage']
                                        uploads = details[2]
                                        uploads = uploads['uploads']
                                        friends = details[3]
                                        friends = friends['friends']
                                        all1 = profiledetails
                                        all1['profile'] = profileimage
                                        all1['image'] = uploads
                                        all1['friends'] = friends
                                    allids = database.idid()
                                    length = len(allids)
                                    data1 = []
                                    for i in range(length):
                                        recamand = allids[i]
                                        data = find.find(recamand)
                                        for data6 in data:
                                            name2 = data6
                                        name = data[name2]
                                        for password in name:
                                            password1 = password
                                        details, id = database.find(name2, password1)
                                        if mainid == id:
                                            None
                                        else:
                                            profileimage = details[0]
                                            profileimage = profileimage['profileimage']
                                            profiledetails = details[1]
                                            profiledetails = profiledetails['profiledetails']
                                            emailid = profiledetails['email']
                                            uploads = details[2]
                                            uploads = uploads['uploads']
                                            friends = details[3]
                                            friends = friends['friends']
                                            all1 = profiledetails
                                            all1['profile'] = profileimage
                                            all1['image'] = uploads
                                            all1['friends'] = friends
                                            data1.append({i + 1: [all1, {name2: emailid}]})
                                    alldetails['sergesions'] = data1
                    return render(request, 'homepage.html', alldetails)
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')