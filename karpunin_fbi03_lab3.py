import http.client
import json

con=http.client.HTTPConnection("167.172.172.227:8000")

con.request('GET','/number/2')
a=con.getresponse()
res=a.read().decode()
print ('Данные: ',res)
num=json.loads(res)
num=num['number']
num_res=num
print("Ответ: ", num_res)
con.close

con.request("GET","/number/?option=2")
a=con.getresponse()
res1=a.read().decode()
print ('Данные: ', res1)
num=json.loads(res1)
oper=num['operation']
num=num["number"]
if oper=='sum':
    num_res1=num_res+num
if oper=='sub':
    num_res1=num_res-num
if oper=='mul':
    num_res1=num_res*num
if oper=='div':
    num_res1=int(num_res/num)
print("Ответ на операцию с числом: ", num_res1)
con.close


he={'Content-Type': 	'application/x-www-form-urlencoded'}
con.request("POST","/number/", "option=2", headers=he)
a=con.getresponse()
res2=a.read().decode()
print ('Данные:',res2)
num=json.loads(res2)
oper=num['operation']
num=num["number"]
if oper=='sum':
    num_res2=num_res1+num
if oper=='sub':
    num_res2=num_res1-num
if oper=='mul':
    num_res2=num_res1*num
if oper=='div':
    num_res2=int(num_res1/num)
print("Ответ на задание 3: ", num_res2)
con.close



h={'Content-Type': 'application/json'}
b= {"option": 2}
con.request("PUT","/number/", body=json.dumps(b), headers=h)
a=con.getresponse()
print ('Данные:',res)
res=a.read().decode()
num=json.loads(res)
oper=num['operation']
num=num["number"]
if oper=='sum':
    num_res3=num_res2+num
if oper=='sub':
    num_res3=num_res2-num
if oper=='mul':
    num_res3=num_res2*num
if oper=='div':
    num_res3=int(num_res2/num)
print("Ответ на 4 задание: ", num_res3)
con.close



k = {"option": 2}
con.request("DELETE","/number/", json.dumps(k))
a=con.getresponse()
res=a.read().decode()
print ('Данные: ',res)
num=json.loads(res)
oper=num['operation']
num=num["number"]
if oper=='sum':
    num_res4=num_res3+num
if oper=='sub':
    num_res4=num_res3-num
if oper=='mul':
    num_res4=num_res3*num
if oper=='div':
    num_res4=int(num_res3/num)
print("Ответ на 5 задание: ", num_res4)
con.close
