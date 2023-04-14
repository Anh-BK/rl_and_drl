## Description
For this project, you will train an agent to navigate (and collect bananas!) in a large, square world.
A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

0 - move forward.

1 - move backward.

2 - turn left.

3 - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

## Installation
To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__: 

    Using conda
	```bash
	conda create --name drlnd python=3.6
	conda activate drlnd
	```
    Using virtualenv and virtualenvwrapper
	```bash
	mkvirtualenv drld -p python3.6
    workon drld
	```
2. Install dependencies
    Unzip file: `Value-baseed-methods.zip`, then:

    ```bash
    cd Value-based-methods/python
    pip3 install .
    ```
3. Install kernel for jupyter notebook
    ```bash
    python3 -m ipykernel install --user --name drlnd --display-name "drlnd"
    ```
4. Start jupyter notebook
    ```bash
    jupyter notebook --ip 0.0.0.0 --port 8.8.8.8
    ```
    After running the commandline above, a new notebook will appear then you select "drlnd" kernel