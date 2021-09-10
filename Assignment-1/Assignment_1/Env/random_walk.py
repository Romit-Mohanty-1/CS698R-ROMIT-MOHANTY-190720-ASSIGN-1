from gym import Env
from gym.spaces import  Discrete
import numpy as np
import random
from scipy.stats import bernoulli


class RandomWalk(Env):
    def __init__(self,params):
        # action space left =0, right=1;
        self.action_space = Discrete(2)
        # state spaces are 0,6 -terminal; 1-5 - non-terminal
        self.observation_space=Discrete(7)
        # initial state is random
        self.state=random.randint(1,5)
        # no. of steps per episode= 500
        self.goInDirection=params["goInDirection"]
        # self.maxSteps=params["maxSteps"]
    def step(self,action):
        # stochasticity in the walk.
        # bernoulli like coin toss.
        if action ==0:
            action = bernoulli.rvs(size=1,p=(1-self.goInDirection))[0]
        else:
            action=bernoulli.rvs(size=1,p=self.goInDirection)[0]
        # after sampling we move using action
        if action ==0:
            self.state-=1
        else:
            self.state+=1
        # reduce remaining number of steps by 1
        # self.maxSteps-=1
        # reward for state 6
        if self.state == 6:
            reward = 1
        else: 
            reward=0
        # check wether we reached a terminal state or not
        if self.state==6 or self.state==0:
            done = True
        else: 
            done = False
        # set placeholder for information
        info={}
        # return step information
        return self.state,reward,done,info
    def render(self):
        pass
    def currState(self):
        return self.state
    def reset(self):
        # reset state
        self.state=random.randint(1,5)
        # reset number of steps
        self.epLength=100
        done=False
        return self.state,done


# checking code
# env=RandomWalk() 
# # print(env.action_space.sample())
# # print(env.observation_space.sample())       
# episodes = 10
# for episode in range(1,episodes+1):
#     state=env.reset()
#     done= False
#     score=0

#     while not done:
#         # env.render()
#         action =0
#         end_state, reward, done, info =env.step(action)
#         score+=reward
#     print('Episode:{} End State: {} Score:{} Timesteps:{}'.format(episode,end_state,score,100-env.epLength))
