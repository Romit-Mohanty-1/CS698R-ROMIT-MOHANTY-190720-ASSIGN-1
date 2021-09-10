from gym import Env
from gym.spaces import  Discrete
import gym
import numpy as np
import random
class two_armed_bernoulli_bandit(Env):
    def __init__(self,prob):
        # action space left =0, right=1;
        self.action_space = Discrete(2)
        # state spaces are 1 -non-terminal, 0,2 terminal
        self.observation_space=Discrete(3)
        # initial state is 1
        self.state=1
        # no. of steps per episode= 1
        self.epLength=1
        # stochastic probability
        self.prob=prob

    def step(self,action):
        # stochasticity in the walk.
        # bernoulli like coin toss.
        # ac -0,1
        if action==0:
            stoch_action=np.random.binomial(1,1- self.prob[0], 1)[0]
        else:
            stoch_action=np.random.binomial(1, self.prob[1], 1)[0]
        if stoch_action == action:
          reward=1
        else:
          reward =0
        self.epLength-=1
        self.state+=int(2*(stoch_action-0.5))        
        done= True
        info={}
        # return step information
        return self.state,reward,done,info

    def render(self):
        pass

    def reset(self):
        # reset state
        self.state=1
        # reset number of steps
        self.epLength=1
# init_prob=[0.5,0.5]
# checking code
# env=two_armed_bernoulli_bandit() 
# # print(env.action_space.sample())
# # print(env.observation_space.sample())       
# episodes = 10
# for episode in range(1,episodes+1):
#     state=env.reset()
#     done= False
#     # env.render()
#     action =random.choice([0,1])
#     # action =0
#     prob=[1,1]
#     end_state, reward, done, info =env.step(action,prob)
    
#     print('Episode:{} End State: {} Reward:{} Action:{}'.format(episode,end_state,reward,action))