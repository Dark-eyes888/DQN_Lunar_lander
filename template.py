import os

dirs=[
    os.path.join('action_critic','A2C'),
    os.path.join('action_critic','A3C'),
    'Deep_q_learning',
    'DDPG',

]

for dirs_ in dirs:
    os.makedirs(dirs_)
    with open(os.path.join(dirs_,'.gitkeep'),'w') as f:
        pass

files=[
    'READ.MD',
    'requirement.txt',
    '.gitignore',
]

for files_ in files :
    with open(files_,'w') as f:
        pass