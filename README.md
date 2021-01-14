# inconnect-routing-gym
* 不同的routing-algorithm
* openai-gym

论文出处: ACM/IEEE NoCS, Oct. 2019 [Arxiv](https://arxiv.org/abs/1908.04484)


[CompArch - gem5/garnet tutorial](http://tusharkrishna.ece.gatech.edu/teaching/garnet_gt/)

[Running garnet](http://pwp.gatech.edu/ece-tushar/wp-content/uploads/sites/175/2019/01/Lab1.pdf)

<img src="https://github.com/huckiyang/inconnect-routing-gym/blob/master/ok_1.png" width="400">


### Downloading gem5

使用的gem5版本
```
sudo apt install mercurial
hg clone /nethome/tkrishna3/teaching/simulators/gem5/repo/gem5
```
该地址无法找到,使用另一个链接
```
git clone https://dragonswordsman@bitbucket.org/synergy-lab/gem5_gt.git
```

### How to use it
Import the module in the src directry
* It provides integration with Garnet2.0 in gem5 with the custom-defined RL-alagirithm
* gem5和RL的接口文件`icn_gym`
```"python"
from icn_gym import ICN_env as ir_gym
```
### Example
We provide examples of baseline (xy routing)
```
example/Baseline_xyRouting_example.py
```
We provides the example of three RL-alagorithms we present in the paper
```
example/rl_QLearning_example.py
example/rl_sarsa_example.py
example/rl_expected_sarsa_example.py
```
### Example of NoC statistics from Garnet2.0 in gem5
```
network_stats.txt
```
