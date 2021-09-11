from gym import Env
from gym.spaces import  Discrete
import gym
import numpy as np
import random
from scipy.stats import bernoulli
class ten_armed_gaussian_bandit(Env):
    def __init__(self,mu,sigma,arms):
        # action space left =0, right=1;
        self.action_space = Discrete(10)
        # state spaces are 1 -non-terminal, 0,2 terminal
        self.observation_space=Discrete(11)
        # initial state is 1
        self.state=0
        self.mu=mu
        self.sigma=sigma
        self.arms=arms
        # mean rewards of each bandit 
        self.mean_rewards=np.random.normal(mu,sigma,arms)
        # no. of steps per episode= 1 greedy horizon

    def step(self,action):
        # rewards to be sample from a gaussian distribution
        reward = np.random.normal(self.mean_rewards[action],self.sigma,1)[0]
        self.state=action+1      
        done= True
        info={}
        # return step information
        return self.state,reward,done,info

    def render(self):
        pass

    def reset(self):
        # reset state
        self.state=0
# env = ten_armed_gaussian_bandit() 
# checking code
# env = ten_armed_gaussian_bandit() 
# # print(env.action_space.sample())
# # print(env.observation_space.sample())       
# episodes = 10
# for episode in range(1,episodes+1):
#     state=env.reset()
#     done= False
#     # env.render()
#     action =random.choice(list(range(0,10)))
#     # action =0
#     end_state, reward, done, info =env.step(action)
    
#     print('Episode:{} End State: {} Reward:{} Action:{}'.format(episode,end_state,reward,action))