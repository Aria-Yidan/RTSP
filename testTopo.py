from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI

def main():
    lg.setLogLevel('info')

    net = Mininet(SingleSwitchTopo(k=2))
    net.start()

    h1 = net.get('h1')

    print("h1.ip: %s" % h1.IP())
    h2 = net.get('h2')

    CLI( net )
    net.stop()

if __name__ == '__main__':
    main()
