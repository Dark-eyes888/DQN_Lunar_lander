from DQN import Agent
import numpy as np
from utils import plotLearning
import gym

if __name__== '__main__':
    env =gym.make('LunarLander')
    n_games= 500
    agent=Agent(gamma=0.99,epsilon=1.0,alpha=0.0005,input_dims=8,
                n_actions=4,mem_size=1000000,batch_size=64,epsilon_end=0.01)

    scores=[]
    eps_history=[]

    for i in range(n_games):
        done=False
        scores=0
        observation=env.reset()
        while not done:
            actions= agent.choose_action(observation)
            observation_, reward,done ,info= env.step(actions)
            scores +=reward
            agent.remember(observation,actions,reward,observation_,done)
            observation= observation_
            agent.learn()

        eps_history.append*=(agent.epsilon)
        scores.append(scores)

        avg_score=np.mean(scores[max(0,i-100):(i+1)])
        print('episode',i,'scores %.2f'%avg_score)
        
        if i % 10 ==0 and i>0:
            agent.save_mode()

    filename='lunarlander.png'
    x=[i+1 for i in range(n_games)]
    plotLearning(x,scores,eps_history,filename)



