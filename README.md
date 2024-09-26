The source code for **FedMut: Generalized Federated Learning via Stochastic Mutation** (Accepted by AAAI2024)

https://ojs.aaai.org/index.php/AAAI/article/view/29146

## 1. Environment setting requirements
* Python 3.7
* PyTorch

## 2. Instruction
### 2.1 Parameter
#### 2.1.1 Dataset Setting
`--dataset <dataset name>`

We can set ‘cifar10’, ‘cifar100’ and ‘femnist’ for CIFAR-10, CIFAR-100, and FEMNIST.

#### 2.1.2 Model Settings
`--num_classes <number>`

Set the number of classes Set 10 for CIFAR-10

Set 20 for CIFAR-100

Set 62 for FEMNIST

`--num_channels <number>`

Set the number of channels of data Set 3 for CIFAR-10 and CIFAR-100. Set 1 for FEMNIST.

#### 2.1.3 Data heterogeneity
`--iid <0 or 1>`

0 – set non-iid 1 – set iid

`--data_beta <𝛼>`

Set the 𝛂 for the Dirichlet distribution

`--generate_data <0 or 1>`

0 – use the existing configuration of 𝑫𝒊𝒓(𝜶) 1 – generate a new configuration of 𝑫𝒊𝒓(𝜶)

#### 2.1.2 FL Settings
`--epochs <number of rounds>`

Set the number of training rounds.

#### 2.1.2 FedMut and Baseline Settings
`-- algorithm <baseline name>`

Set the baseline name:
* FedMut
* FedAvg
* FedProx
* FedGen
* ClustererSampling

`-- radius <float>`

Set the range of mutation for FedMut

`-- mut_acc_rate <float>`

Set the acceleration rate for FedMut

#### 2.1.3 Loss-landscape
Please use the tool as follows to generate the figure of loss-landscape：

https://github.com/tomgoldstein/loss-landscape

## 3. Citation
```
@inproceedings{hu2024fedmut,
  title={FedMut: Generalized Federated Learning via Stochastic Mutation},
  author={Hu, Ming and Cao, Yue and Li, Anran and Li, Zhiming and Liu, Chengwei and Li, Tianlin and Chen, Mingsong and Liu, Yang},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={38},
  number={11},
  pages={12528--12537},
  year={2024}
}
```
