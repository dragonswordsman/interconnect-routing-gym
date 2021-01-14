import random
import os
from collections import defaultdict, deque #defaultdict-字典的子类，deque-双向队列
import numpy as np
import matplotlib as mpl
import matplotlib
matplotlib.use('agg') #png格式，类似还有svg
import matplotlib.pyplot as plt #必须在matplotlib.use('agg')后面
import csv #表格文件，数据以分隔符隔开，按行读取
from src.icn_gym import *

## Global Parameters
actions = ["xy", "random", "west_first", "adaptive_random","adaptive_west_first"]
a_size = len(actions) # space size of action=4
Q = defaultdict(lambda: np.zeros(a_size)) # Q-Table 2d
dicts = defaultdict(list) #https://www.cnblogs.com/herbert/archive/2013/01/09/2852843.html 调用方式dicts[a].append=b, for a,b in Q
action_index = random.randint(0, 100)%2  #0和1的用意？
action = actions[action_index]
iter_step = 6 # injection from 0.1 to 0.6
total_episodes = 1 # Game Playing times

epsilon = 1.0       # exploration rate
eps_min = 0.01
eps_decay = 0.999

### Plot Notebooks
time_history = []
rew_history = []
Q = defaultdict(lambda: np.zeros(a_size))

state = 0.1 # = Injection_rate as reset state env.reset()
# dicts = ICN_env(state, action) # ICM simulate() --强化学习算法
for i in range(iter_step):
	state = (i+1)/10 # get next state
	action = "xy"
	dicts = ICN_env(state, action)
	
	# action = actions[random.randint(0, 100)%2]

rew_history.append(0) # Recording rewards



print('Q-Table = ', Q)

print('Reward = ', rew_history)

# print('Dicts = ',dicts)

csv_columns = ['average_flit_latency','average_packet_queueing_latency','average_flit_network_latency','average_flit_queueing_latency','packets_injected', 'average_packet_network_latency', 'average_hops',  'flits_injected', 'packets_received',  'flits_received', 'average_packet_latency']
csv_file = 'Inter_Connect_Networks/Tables/env_base_'+str(iter_step)+'_' +str(total_episodes)+ '.csv'

try:
	with open(csv_file, 'w', newline='') as csvfile: #w文件对象
		writer = csv.writer(csvfile)
		writer.writerow(csv_columns)
		for i in range(len(dicts['average_flit_latency'])):
			writer.writerow([dicts[key][i] for key in csv_columns])  #写行
except IOError:
    print("I/O error")
# np.savetxt("Reward_history.csv", rew_history, delimiter=",")
### Plotting 

# print("Learning Performance")
mpl.rcdefaults()
mpl.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(10,4)) #ax->axies 10-宽, 4-高
# plt.grid(True, linestyle='--')
plt.title('ICNs Learning')
# plt.plot(range(len(time_history)), time_history, label='Steps', marker="^", linestyle=":")#, color='red')
plt.plot(range(len(rew_history)), rew_history, label='Reward', marker="", linestyle="-")#, color='k')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.savefig('Inter_Connect_Networks/Figures/shuffle_SARSA_'+str(iter_step)+'_'+str(total_episodes)+'_ICN.png', bbox_inches='tight')
