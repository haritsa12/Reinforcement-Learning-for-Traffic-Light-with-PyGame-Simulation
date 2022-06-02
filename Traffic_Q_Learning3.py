#call library
import random
import json
from numpy import log as ln

#print_qtable: print q_table
# def print_qtable(Q_table):
# 	print("State \t\t North \t\t East \t\t South \t\t West")
# 	for i in range(81):
# 	# for i in range(256):
# 		print(i+1, end="\t\t")					
# 		for j in range (4):
# 			if(j!=4-1):
# 				print("{:.4f}".format(Q_table[i][j],), end="\t\t");
# 			else:
# 				print("{:.4f}".format(Q_table[i][j],))

def print_qtable(Q_table, lane, level):
	print("State \t North \t East \t South \t West")
	for i in range(pow(level,lane)):
		print(i+1, end="\t")
		for j in range (lane):
			if(j!=lane-1):
				print(format(Q_table[i][j],'.5f'), end="\t");
			else:
				print(format(Q_table[i][j],'.5f'))

#get_state: get state representation from traffic condition
# def get_state(kondisi):
# 	return kondisi[0]*pow(3,3) + kondisi[1]*pow(3,2) + kondisi[2]*pow(3,1) + kondisi[3]*pow(3,0)      	#untuk 81 states
# 	# return kondisi[0]*pow(4,3) + kondisi[1]*pow(4,2) + kondisi[2]*pow(4,1) + kondisi[3]*pow(4,0)		#untuk 256 states
#update_kondisi: update traffic condition based on action

def get_state(kondisi, lane, level):
	state = 0
	temp = 0
	for i in range(lane):
		temp = kondisi[i]*pow(level,lane-1-i)
		state += temp
	return state


# def update_kondisi(green, kondisi):
# 	new_kondisi = kondisi[:]
# 	for i in range(4):
# 		if(i == green):
# 			new_kondisi[i] -= 1
# 			if(new_kondisi[i] <= 0):
# 				new_kondisi[i] = 0
# 		else:
# 			new_kondisi[i] += 1
# 			if(new_kondisi[i] >= 2):
# 				new_kondisi[i] = 2
		
# 	return new_kondisi

def update_kondisi(green, kondisi, lane, level):
	new_kondisi = kondisi[:]

	for i in range(lane):
		if(i == green):
			new_kondisi[i] -= 1
			if(new_kondisi[i] <= 0):
				new_kondisi[i] = 0
		else:
			new_kondisi[i] += 1
			if(new_kondisi[i] >= level-1):
				new_kondisi[i] = level-1
	

	return new_kondisi


#action: choose action based on condition and q-table
# def action(epsilon, state, kondisi, q_table):
	
# 	randomnum = random.random();
# 	if(epsilon <= randomnum):
# 		max_value = max(q_table[state])
# 		for j in range(4):
# 			if(max_value == q_table[state][j]):
# 				green = j
# 	else:
# 		number = random.random()
# 		if(number <= 0.25):
# 			green = 0 #lane north
# 		elif(number <= 0.5):
# 			green  = 1 #lane east
# 		elif(number <= 0.75):
# 			green = 2 #lane south
# 		else:
# 			green = 3 #lane west
	
# 	new_kondisi = update_kondisi(green, kondisi)
	
# 	return new_kondisi, green


# def action(epsilon, state, kondisi, q_table, lane, level):
	
# 	randomnum = random.random();
# 	if(epsilon <= randomnum):
# 		max_value = max(q_table[state])
# 		for j in range(lane):
# 			if(max_value == q_table[state][j]):
# 				green = j
# 	else:
# 		number = random.random()
# 		if(number <= 0.25):
# 			green = 0 #lane north
# 		elif(number <= 0.5):
# 			green  = 1 #lane east
# 		# elif(number <= 0.75):
# 		# 	green = 2 #lane south
# 		else:
# 			green = 2  #lane west
	
# 	new_kondisi = update_kondisi(green, kondisi, lane, level)
	
# 	return new_kondisi, green

#action: choose action based on condition and q-table
def action(epsilon, state, kondisi, q_table, lane, level):
	green = 0
	randomnum = random.random()
	if(epsilon <= randomnum):
		max_value = max(q_table[state])
		for j in range(lane):
			if(max_value == q_table[state][j]):
				green = j
	else:
		number = random.random()
		for i in range(lane):
			if(number >= (i)*1/lane)and(number < (i+1)*1/lane):
				green = i
		# ~ if(number <= 0.25):
			# ~ green = 0 #lane north
		# ~ elif(number <= 0.5):
			# ~ green  = 1 #lane east
		# ~ elif(number <= 0.75):
			# ~ green = 2 #lane south
		# ~ else:
			# ~ green = 3 #lane west
	
	new_kondisi = update_kondisi(green, kondisi, lane, level)
	
	return new_kondisi, green
#update_qvalue: update q-value in q-table based on action and reward
# def update_qvalue(green, state, kondisi, new_state, new_kondisi, q_table, alpha, gamma):
# 	#derajat 2 diberi hijau
# 	if(kondisi[green] == 2):
# 		reward = 50
		
# 	#derajat 1 diberi hijau
# 	elif(kondisi[green] == 1):
# 		reward = 0
	
# 	#derajat 0 diberi hijau
# 	elif(kondisi[green] == 0):
# 		reward = -50
		
# 	else:
# 		reward = 0
	
# 	#print(reward)
# 	q_table[state][green] = (1 - alpha) * q_table[state][green] + alpha * (reward +  gamma * max(q_table[new_state]))
	
# 	return q_table

def update_qvalue(green, state, kondisi, new_state, new_kondisi, q_table, alpha, gamma, lane, level):
	#derajat 1 diberi hijau
	for i in range (level):
		# print(i)
		if (kondisi[green] == 0):
			reward=-75

		elif(kondisi[green] == i):
			reward = 60*ln(i)
	
	
	#print(reward)
	q_table[state][green] = (1 - alpha) * q_table[state][green] + alpha * (reward +  gamma * max(q_table[new_state]))
	
	return q_table




def choose_action():
	for choose_action.i in range (0,4096):

		if q_table[choose_action.i][0] > q_table[choose_action.i][1] and q_table[choose_action.i][0] > q_table[choose_action.i][2] and q_table[choose_action.i][0] > q_table[choose_action.i][3]:
			choose_action.green_1=0
		elif  q_table[choose_action.i][1] > q_table[choose_action.i][0] and q_table[choose_action.i][1] > q_table[choose_action.i][2] and q_table[choose_action.i][1] > q_table[choose_action.i][3]:
			choose_action.green_1=1
		elif q_table[choose_action.i][2] > q_table[choose_action.i][1] and q_table[choose_action.i][2] > q_table[choose_action.i][0] and q_table[choose_action.i][0] > q_table[choose_action.i][3]:
			choose_action.green_1=2
		elif q_table[choose_action.i][3] > q_table[choose_action.i][1] and q_table[choose_action.i][3] > q_table[choose_action.i][2] and q_table[choose_action.i][3] > q_table[choose_action.i][0]:
			choose_action.green_1=3
		#print (i,j)
		choose_action._state=choose_action.i+1
		# print (str(choose_action._state) +'.' , str(green_1))


def state_action_pair():
	state_action_pair.action_pair=[0 for i in range (4096)]
	# for i in range (0,81):
	for i in range (0,4096):
		state_action_pair.action_pair[i] = max(q_table[i])
		for j in range(4):
			if(state_action_pair.action_pair[i] == q_table[i][j]):
				state_action_pair.action_pair[i] = j
				#j==0
				if j==0 and q_table[i][j]==q_table[i][j+1]:
					state_action_pair.action_pair[i] = random.choice([j,j+1])
				elif j==0 and q_table[i][j]==q_table[i][j+2]:
					state_action_pair.action_pair[i] = random.choice([j,j+2])
				elif j==0 and q_table[i][j]==q_table[i][j+3]:
					state_action_pair.action_pair[i] = random.choice([j,j+3])
				elif j==0 and q_table[i][j]==q_table[i][j+1] and q_table[i][j]==q_table[i][j+3] : 
					state_action_pair.action_pair[i] = random.choice([j,j+1,j+3])
				elif j==0 and q_table[i][j]==q_table[i][j+1] and q_table[i][j]==q_table[i][j+2] : 
					state_action_pair.action_pair[i] = random.choice([j,j+1,j+2])
				elif j==0 and q_table[i][j]==q_table[i][j+2] and q_table[i][j]==q_table[i][j+3] : 
					state_action_pair.action_pair[i] = random.choice([j,j+3,j+2])
				elif j==0 and q_table[i][j]==q_table[i][j+1] and q_table[i][j]==q_table[i][j+3] and q_table[i][j]==q_table[i][j+2] : 
					state_action_pair.action_pair[i] = random.choice([j,j+1,j+3,j+2])

				#j==1
				elif j==1 and q_table[i][j]==q_table[i][j+1]:
					state_action_pair.action_pair[i] = random.choice([j,j+1])
				elif j==1 and q_table[i][j]==q_table[i][j+2]:
					state_action_pair.action_pair[i] = random.choice([j,j+2])
				
				elif j==1 and q_table[i][j]==q_table[i][j+1] and q_table[i][j]==q_table[i][j+2] : 
					state_action_pair.action_pair[i] = random.choice([j,j+1,j+2])
				
				#j==2
				elif j==2 and q_table[i][j]==q_table[i][j+1]:
					state_action_pair.action_pair[i] = random.choice([j,j+1])
				([j,j+1,j-1,j-2])
				
	return state_action_pair.action_pair[i]
				

# def state_action_pair():
# 	state_action_pair.action_pair=[0 for i in range (512)]
# 	# for i in range (0,81):
# 	for i in range (0,512):
# 		state_action_pair.action_pair[i] = max(q_table[i])
# 		for j in range(3):
# 			if(state_action_pair.action_pair[i] == q_table[i][j]):
# 				state_action_pair.action_pair[i] = j
# 				#j==0
# 				if j==0 and q_table[i][j]==q_table[i][j+1]:
# 					state_action_pair.action_pair[i] = random.choice([j,j+1])
# 				elif j==0 and q_table[i][j]==q_table[i][j+2]:
# 					state_action_pair.action_pair[i] = random.choice([j,j+2])
				
			
# 				elif j==0 and q_table[i][j]==q_table[i][j+1] and q_table[i][j]==q_table[i][j+2] : 
# 					state_action_pair.action_pair[i] = random.choice([j,j+1,j+2])
				

# 				#j==1
# 				elif j==1 and q_table[i][j]==q_table[i][j+1]:
# 					state_action_pair.action_pair[i] = random.choice([j,j+1])
				
				
				
# 				#j==2
				
				
# 	return state_action_pair.action_pair[i]

#parameter


# lane = int(input("Enter Total Lane: "))
level = int(input("Enter Total Congestion Level: "))

# alpha = 0.6
# gamma = 0.9
lane = 4
# level = 4
with open('alpha & gamma.json', 'r') as file:
	data = json.load(file)


alpha = float(data['Parameters']['Alpha'])
gamma = float(data['Parameters']['Gamma'])


#make q-table
# q_table = [[random.random() for i in range(4)] for j in range(81)]
# # q_table = [[random.random() for i in range(4)] for j in range(256)]
# print_qtable(q_table)

q_table = [[random.random() for i in range(lane)] for j in range(pow(level,lane))]
print_qtable(q_table, lane, level)


# for episode in range(5000):   #berhasil untuk 81 states
# # for episode in range(500000):
# 	kondisi = [random.randrange(0,3,1) for i in range(4)]
# 	#print(kondisi)
	
# 	epsilon = 1 - ((episode+1) / 50001)
	
# 	for t in range(20):			#berhasil untuk 81 states
# 	# for t in range(1000):
# 		#print(kondisi)
# 		state =  get_state(kondisi)
# 		#print(state)
		
# 		[new_kondisi, green_light] = action(epsilon, state, kondisi, q_table)
# 		# print(kondisi)
# 		# print(new_kondisi)
# 		# print(green_light)
		
# 		new_state = get_state(new_kondisi)
# 		#print(new_state)
		
# 		q_table = update_qvalue(green_light, state, kondisi, new_state, new_kondisi, q_table, alpha, gamma)
# 		# print_qtable(q_table)
# 		kondisi = new_kondisi
# 		#print(kondisi, "\n")
# 		#break
# 		#print_qtable(q_table)
# 		#break
# 	#break
# print_qtable(q_table)

for episode in range(5000):
	kondisi = [random.randrange(0,level,1) for i in range(lane)]
	#red_count = [0 for i in range(lane)]
	#print(kondisi)
	
	epsilon = 1 - ((episode+1) / 5001)
	
	for t in range(20):
		#print(kondisi)
		state =  get_state(kondisi, lane, level)
		#print(state)
		
		[new_kondisi, green_light] = action(epsilon, state, kondisi, q_table, lane, level)
		#print(kondisi)
		#print(new_kondisi)
		#print(green_light)
		
		new_state = get_state(new_kondisi, lane, level)
		#print(new_state)
		
		q_table = update_qvalue(green_light, state, kondisi, new_state, new_kondisi, q_table, alpha, gamma, lane, level)
		
		kondisi = new_kondisi
		#print(kondisi, "\n")
		#break
		#print_qtable(q_table)
		#break
	#break
print_qtable(q_table, lane, level)

state_action_pair()
for i in range (27):
	print(i+1,state_action_pair.action_pair[i])
print (state_action_pair.action_pair[5])
#test
kondisi = [0,1,0,1]
print(kondisi)
# state = get_state(kondisi)
state = get_state(kondisi, lane, level)
# temp = action(epsilon,state, kondisi, q_table)
temp = action(epsilon, state, kondisi, q_table, lane, level)
print(temp[0])
print(temp[1])

execfile("simulation_master_without_arduiono.py")
