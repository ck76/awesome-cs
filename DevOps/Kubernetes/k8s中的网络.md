[TOC]

# 一、网络前提条件-网络模型

- k8s组网要求
  - 所有的Pods之间可以在不使用[NAT网络地址转换](https://links.jianshu.com/go?to=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F网络地址转换)的情况下相互通信
  - 所有的Nodes之间可以在不使用NAT网络地址转换的情况下相互通信
  - 每个Pod自己看到的自己的ip和其他Pod看到的一致
- k8s网络模型设计原则
  - 每个Pod都拥有一个独立的 IP地址，而且 假定所有 Pod 都在一个可以直接连通的、扁平的网络空间中 。
  - 不管它们是否运行在同 一 个 Node (宿主机)中，都要求它们可以直接通过对方的 IP 进行访问。
  - 设计这个原则的原因 是，用户不需要额外考虑如何建立 Pod 之间的连接，也不需要考虑将容器端口映射到主机端口等问题。

**由于 Kubemetes 的网络模型假设 Pod 之间访问时使用的是对方 Pod 的实际地址，所以一个Pod 内部的应用程序看到的自己的 IP 地址和端口与集群内其他 Pod 看到的一样。它们都是 Pod 实际分配的IP地址 (从dockerO上分配的)。将IP地址和端口在Pod内部和外部都保持一致， 我们可以不使用 NAT 来进行转换，地址空间也自然是平的。**

# 二、需要解决的网络问题

根据以上的一些要求，需要解决的问题

- Docker容器和Docker容器之间的网络
- Pod与Pod之间的网络
- Pod与Service之间的网络
- Internet与Service之间的网络

## 1.容器和容器之间的网络

pod有多个容器，它们之间怎么通信？

**pod中每个docker容器和pod在一个网络命名空间内，所以ip和端口等等网络配置，都和pod一样**，主要通过一种机制就是，docker的一种网络模式，container，新创建的Docker容器不会创建自己的网卡，配置自己的 IP，而是和一个指定的容器共享 IP、端口范围等

## 2.pod与pod之间的网络

**pod与pod之间的网络：首先pod自身拥有一个IP地址，不同pod之间直接使用IP地址进行通信即可**

### 同一台node节点上pod和pod通信

**疑问**：那么不同pod之间，也就是不同网络命名空间之间如何进行通信（现在还是，同一台node节点上）

**解决**：

简单说veth对就是一个成对的端口，所有从这对端口一端进入的数据包，都将从另一端出来。

 **为了让多个Pod的网络命名空间链接起来，我们可以让veth对的一端链接到root网络命名空间（宿主机的），另一端链接到Pod的网络命名空间。**

嗯，那么继续。

 **还需要用到一个Linux以太网桥，它是一个虚拟的二层网络设备，目的就是把多个以太网段连接起来，它维护一个转发表，通过查看每个设备mac地址决定转发，还是丢弃数据**

- pod1-->pod2（同一台node上），pod1通过自身eth0网卡发送数据，eth0连接着veth0，网桥把veth0和veth1组成了一个以太网，然后数据到达veth0之后，网桥通过转发表，发送给veth1，veth1直接把数据传给pod2的eth0。

### 不同node节点上pod和pod通信

**CIDR的介绍：**

CIDR（Classless Inter-Domain Routing，无类域间路由选择）它消除了传统的A类、B类和C类地址以及划分子网的概念，因而可以更加有效地分配IPv4的地址空间。它可以将好几个IP网络结合在一起，使用一种无类别的域际路由选择算法，使它们合并成一条路由从而较少路由表中的路由条目减轻Internet路由器的负担。

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygoze3s5ej30rs0sqdhb.jpg)

看图，接着往下捋。

**k8s集群中，每个node节点都会被分配一个CIDR块，（把网络前缀都相同的连续地址组成的地址组称为CIDR地址块）用来给node上的pod分配IP地址，另外还需要把pod的ip和所在nodeip进行关联**

- 比如node1上pod1和node2上的pod4进行通信
  1. 首先pod1上网卡eth0将数据发送给已经管理到root命名空间的veth0上，被虚拟网桥收到，查看自己转发表之后，并没有pod4的mac地址。
  2. 就会把包转发到默认路由，（root命名空间的eth0上，也就是已经到了node节点的往卡上）通过eth0，发送到网络中。
  3. 寻址转发后包来到了node2，首先被root命名空间的eth0设备接受，查看目标地址是发往pod4的，交给虚拟网桥路由到veth1，最终传给pod4的eth0上。

## 3.pod与service之间的网络

**pod的ip地址是不持久的，当集群中pod的规模缩减或者pod故障或者node故障重启后，新的pod的ip就可能与之前的不一样的。所以k8s中衍生出来Service来解决这个问题。**

Service管理了多个Pods，每个Service有一个虚拟的ip,要访问service管理的Pod上的服务只需要访问你这个虚拟ip就可以了，这个虚拟ip是固定的，当service下的pod规模改变、故障重启、node重启时候，对使用service的用户来说是无感知的，因为他们使用的service的ip没有变。

**当数据包到达Service虚拟ip后，数据包会被通过k8s给该servcie自动创建的负载均衡器路由到背后的pod容器。**

- 在k8s里，iptables规则是由kube-proxy配置，kube-proxy监视APIserver的更改，因为集群中所有service（iptables）更改都会发送到APIserver上，所以每台kubelet-proxy监视APIserver，当对service或pod虚拟IP进行修改时，kube-proxy就会在本地更新，以便正确发送给后端pod
- **pod到service包的流转：**

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygozcre97j30rs0jawf9.jpg)

1. 数据包从pod1所在eth0离开，通过veth对的另一端veth0传给网桥cbr0，网桥找不到service的ip对应的mac，交给了默认路由，到达了root命名空间的eth0
2. root命名空间的eth0接受数据包之前会经过iptables进行过滤，iptables接受数据包后使用kube-proxy在node上配置的规则响应service，然后数据包的目的ip重写为service后端指定的pod的ip了

- **service到pod包的流转**

1. 收到包的pod会回应数据包到源pod，源ip是发送方ip，目标IP是接收方，数据包进行回复时经过iptables，iptables使用内核机制conntrack记住它之前做的选择，又将数据包源ip重新为service的ip，目标ip不变，然后原路返回至pod1的eth0

## 4.Internet与service之间的网络

将k8s集群服务暴露给互联网上用户使用，有两个问题；

**（1）从k8s的service访问Internet，以及（2）从Internet访问k8s的service.**

根据参考文章，通过Internet网关，node可以将流量路由到Internet，但是pod具有自己的IP地址，Internet王冠上的NAT转换并不适用。**参考方案：就是node主机通过iptables的nat来解决**

- node到internet包的流转

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5pqijgj30rs0kndgz.jpg)

1. 数据包源自pod1网络命名空间，通过veth对连接到root网络命名空间，紧接着，转发表里没有IP对应的mac，会发送到默认路由，到达root网络命名空间的eth0
2. **那么在到达root网络明明空间之前，iptables会修改数据包，现在数据包源ip是pod1的，继续传输会被Internet网关拒绝掉，因为网关NAT仅转发node的ip，解决方案：使iptables执行源NAT更改数据包源ip，让数据包看起来是来自于node而不是pod**
3. iptables修改完源ip之后，数据包离开node，根据转发规则发给Internet网关，Internet网关执行另一个NAT，内网ip转为公网ip，在Internet上传输。
4. 数据包回应时，也是按照：Internet网关需要将公网IP转换为私有ip，到达目标node节点，再通过iptables修改目标ip并且最终传送到pod的eth0虚拟网桥。

### Internet到k8s的流量

让Internet流量进入k8s集群，这特定于配置的网络，可以在网络堆栈的不同层来实现：

（1） NodePort

（2）Service LoadBalancer

（3）Ingress控制器。

这里只介绍第三种，如果想看详细的，文章开始有一个链接

- **第七层流量入口：Ingress Controller**

通过一个公开的ip地址来公开多个服务，第7层网络流量入口是在网络堆栈的HTTP / HTTPS协议范围内运行，并建立在service之上。

**工作**：客户端现针对www.1234.com执行dns解析，DNS服务器返回ingress控制器的ip，客户端拿到ip后，向ingress控制器发送http的get请求，将域名加在host头部发送。控制器接收到请求后，**从host头部就知道了该访问哪一个服务，通过与该service关联的endpoint对象查询podIP地址，将请求进行转发**

第7层负载均衡器的一个好处是它们具有HTTP感知能力，因此它们了解URL和路径。 这允许您按URL路径细分服务流量。 它们通常还在HTTP请求的X-Forwarded-For标头中提供原始客户端的IP地址。



----

```text
kubernetes组件
Kubernetes Master：kube-apiserver, kube-controller-manager, kube-scheduler
Kubernetes Node：kube-proxy,kubelet

kube-apiserver:  API-server 负载输出RESTful风格的Kubernetes API， 它是集群的所有REST操作命令的
接入点，并负责接收、校验并响应所有REST请求，结果状态被持久存储于etcd中。
因此API server 是整个集群网关

kube-scheduler: 负责调度
kube-controller-manager: 负责容器编排，集群内部的管理控制中心，负责集群内的Node、Pod副本、服务端点
（Endpoint）、命名空间（Namespace）、服务账号（ServiceAccount）、资源定额（ResourceQuota）的管理。

kubelet：kubelet 是用行在node 上的守护进程，它从API server接收关于pod对象的配置信息并确保它们的
处于期望状态（desired state目标状态）。kubelet会在API server上注册当前节点，定期向Master汇报节点
资源使用情况，并通过cAdvisor监控容器和节点资源占用情况

kube-proxy：一个网络代理，每个node上都运行一个kube-proxy守护进程，它能够按需为server资源对象生成
iptables或ipvs规则，从而捕获访问当前server和GlusterIP 的流量并将其转发至后端正真pod对象
```

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5ntktpj30ai06z0sx.jpg)

```text
CNI (Container Network Interface):eg:flannel.calico
CRI (Container Runtime Interface):eg:docker
CSI (Container Storage Interface):eg:PV
OCI(Open Container Initiative, 开放容器标准):eg:runC
```

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5mk8jjj30jy0i1wfs.jpg)



![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5lfxfij30o208nwf1.jpg)

```text
pod：解析
1.Pod是K8s进行创建、调度和管理的最小单位
2.Pod运行于Node节点上, 若干相关容器的组合
3.Pod内包含的容器运行在同一宿主机上，使用相同的网络命名空间、IP地址和端口，能够通过localhost进行通信
4.Pod可以指定一组共享存储。Volumes Pod中,Pod中的所有容器都可以访问共享卷，从而使这些容器可以共享数据
5.Pod 就是 k8s 世界里的"应用",而一个应用，可以由多个容器组成。

ps:Pod本身无法自我修复,K8s中使用kube-controller-manager管理Pod
pause容器：
 1）每个Pod中都有一个pause容器，pause容器做为Pod的网络接入点
 2）属于同一个Pod的所有容器共享网络的namespace
 3）一个Pod里的容器与另外主机上的Pod容器能够直接通信（lo）
 4）属于同一个Pod的所有容器共享Volume挂载卷
```



```text
一、K8s网络设计
1.每个Pod都拥有一个独立IP地址，Pod内所有容器共享一个网络命名空间
2.集群内所有Pod都在一个直接连通的扁平网络中，可通过IP直接访问
 (1) 所有容器之间无需NAT就可以直接互相访问
 (2) 所有Node和所有容器之间无需NAT就可以直接互相访问
 (3) 容器自己看到的IP跟其他容器看到的一样

二、K8s网络要求
K8s对网络的要求总的来讲主要有两个最基本的要求，分别是：
 1)要能够为每一个Node上的Pod分配互相不冲突的IP地址
 2)要所有Pod之间能够互相访问
 

三、K8s网络规范
 CNI是由CoreOS提出的一个容器网络规范。已采纳规范的包括Apache Mesos, Cloud Foundry, Kubernetes, Kurma 和 rkt。
 另外 Contiv Networking, Project Calico 和 Weave这些项目也为CNI提供插件。
 
四、K8s网络实现
隧道方案
隧道方案在IaaS层的网络中应用也比较多，将pod分布在一个大二层的网络规模下。网络拓扑简单，但随着节点规模的增长复杂度会提升。
Weave：UDP广播，本机建立新的BR，通过PCAP互通
Open vSwitch（OVS）：基于VxLan和GRE协议，但是性能方面损失比较严重
Flannel：UDP广播，VxLan
Racher：IPsec

路由方案
路由方案一般是从3层或者2层实现隔离和跨主机容器互通的，出了问题也很容易排查。
Calico：基于BGP协议的路由方案，支持很细致的ACL控制，对混合云亲和度比较高。
Macvlan：从逻辑和Kernel层来看隔离性和性能最优的方案，基于二层隔离，所以需要二层路由器支持，大多数云服务商不支持，所以混合云上比较难以实现。

五、K8s Pod的网络创建流程
1.每个Pod除了创建时指定的容器外，都有一个kubelet启动时指定的基础容器
2.kubelet创建基础容器，生成network namespace
3.kubelet调用网络CNI driver，由它根据配置调用具体的CNI 插件(eg:calico,flannel)
4.CNI 插件给基础容器配置网络
5.Pod 中其他的容器共享使用基础容器的网络
```



**K8s 网络**

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5inorgj30k00b5dgn.jpg)

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5eia06j30g90k5gpk.jpg)

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5gh3cuj30gk0c0dgu.jpg)

```text
三种 IP 定义
 1.Node IP：Node 节点的 IP 地址，即物理机(虚拟机)的 IP 地址。
 2.Pod IP：Pod 的 IP 地址，即 docker 容器的 IP 地址，此为虚拟 IP 地址。
 3.Cluster IP：Service 的 IP 地址，此为虚拟 IP 地址。

三种 IP 的理解
  Node IP：是物理机的IP（或虚拟机IP）。每个Service都会在Node节点上开通一个端口，外部可以通过http://NodeIP:NodePort 
  即可访问 Service 里的 Pod 提供的服务。
  
  Pod IP：是每个Pod的IP地址，Docker Engine根据 docker 网桥的 IP 地址段进行分配的，通常是一个虚拟的二层网络。
     同Service下的pod可以直接根据PodIP相互通信
     不同Service下的pod在集群间pod通信要借助于 cluster ip
     pod和集群外通信，要借助于node ip
     
  Cluster IP: 是Service的IP地址，此为虚拟 IP 地址，外部网络无法 ping 通，只有k8s集群内部访问使用。
     Cluster IP仅仅作用于K8s Service这个对象，并由K8es管理和分配P地址 Cluster
     IP无法被ping，他没有一个“实体网络对象”来响应 Cluster IP只能结合Service
     Port组成一个具体的通信端口，单独的Cluster IP不具备通信的基础，并且他们属于K8s集群这样一个封闭的空间。
     在不同Service下的pod节点在集群间相互访问可以通过Cluster IP
```



```text
K8s的网络中pod的通信：
1. 同一Pod内的容器间通信:
    因为pause容器提供pod内网络共享，所以容器直接可以使用localhost(lo)访问其他容器
    
2. 各Pod彼此之间的通信(两个pod在一台主机上面, 两个pod分布在不同主机之上)
   1)两个pod在一台主机上面: 通过docker默认的docker网桥互连容器(docker0), ifconfig 查了docker0
   2)两个pod分布在不同主机之上: 通过CNI插件实现，eg: flannel,calico

3. Pod与Service间的通信
   Service分配的ip叫cluster ip是一个虚拟ip（相对固定，除非删除service），这个ip只能在k8s集群内部使用，
   如果service需要对外提供，只能使用Nodeport方式映射到主机上，使用主机的ip和端口对外提供服务。
   节点上面有个kube-proxy进程，这个进程从master apiserver获取信息，感知service和endpoint的创建，然后做两个事：
    1.为每个service 在集群中每个节点上面创建一个随机端口，任何该端口上面的连接会代理到相应的pod
    2.集群中每个节点安装iptables/ipvs规则，用于clusterip + port路由到上一步定义的随机端口上面，
    所以集群中每个node上面都有service的转发规则:iptables -L -n -t filter
```



**Pod Network**

K8s的一个Pod中包含有多个容器，这些容器共享一个Network Namespace，即是共享一个Network Namespace中的一个IP。创建Pod时，首先会生成一个pause容器，然后其他容器会共享pause容器的网络。

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5clbpqj30my0433zd.jpg)

```text
pause的ip又是从哪里分配到的？如果还是用一个以docker0为网关的内网ip就会出现问题了。
docker默认的网络是为同一台宿主机的docker容器通信设计的，K8s的Pod需要跨主机与其他Pod通信，
所以需要设计一套让不同Node的Pod实现透明通信（without NAT）的机制。
docker0的默认ip是172.17.0.1，docker启动的容器也默认被分配在172.17.0.1/16的网段里。跨主机的Pod
通信要保证Pod的ip不能相同，所以还需要设计一套为Pod统一分配IP的机制。
以上两点，就是K8s在Pod network这一层需要解决的问题，可以利用插件解决如:flannel,calico
```

![img](https://tva1.sinaimg.cn/large/008i3skNly1gygp5bnk1fj30km02aq3s.jpg)



----



- https://blog.csdn.net/m0_37055174/article/details/99957377
- https://jiayi.space/post/kubernetescong-ru-men-dao-fang-qi-3-wang-luo-yuan-li
- https://zhuanlan.zhihu.com/p/126116540

- https://www.cnblogs.com/jojoword/p/11214256.html