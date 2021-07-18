from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager


def parse_host(hostfile, active_dc, passive_dc):
    variable_manager = VariableManager()
    loader = DataLoader()
    ms_ip_list = []
    inventory = InventoryManager(loader=loader, sources=hostfile)
    ms1 = inventory.get_groups_dict()['ms-{}'.format(active_dc)][0]
    ms2 = inventory.get_groups_dict()['ms-{}'.format(passive_dc)][0]
    ms_ip_list.append(ms1)
    ms_ip_list.append(ms2)
    return ms_ip_list


if __name__ == '__main__':
    hostfile = ""
    active_dc = ""
    passive_dc = ""
    iplist = parse_host(hostfile, active_dc, passive_dc)
    print(iplist)


