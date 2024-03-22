# Morganblackhand wakeup samurai
# pre.py

def main():
    # Common settings
    ospf_enabled = input("Do you want to activate OSPF? (yes/no): ").lower() == 'yes'

    # Prompting for Router R1 settings
    print("Enter the configuration for Router R1:")
    r1_interface_g0 = input("Enter the interface name for Router R1 GigabitEthernet0/0 (e.g., GigabitEthernet0/0/0): ")
    r1_int_g0_ip = input(f"Enter the IP address for Router R1 {r1_interface_g0} (e.g., 192.168.1.1): ")
    r1_int_g0_mask = input("Enter the subnet mask for this interface (e.g., 255.255.255.0): ")
    r1_interface_g1 = input("Enter the interface name for Router R1's second interface (e.g., GigabitEthernet0/0/1): ")
    r1_int_g1_ip = input(f"Enter the IP address for Router R1 {r1_interface_g1} (e.g., 1.1.1.1): ")
    r1_int_g1_mask = input("Enter the subnet mask for this interface (e.g., 255.255.255.0): ")
    r1_network_1 = f"{r1_int_g0_ip} 0.0.0.255"
    r1_network_2 = f"{r1_int_g1_ip} 0.0.0.255"

    # Prompting for Router R2 settings
    print("\nEnter the configuration for Router R2:")
    r2_interface_g0 = input("Enter the interface name for Router R2 GigabitEthernet0/0 (e.g., GigabitEthernet0/0/0): ")
    r2_int_g0_ip = input(f"Enter the IP address for Router R2 {r2_interface_g0} (e.g., 1.1.1.2): ")
    r2_int_g0_mask = input("Enter the subnet mask for this interface (e.g., 255.255.255.0): ")
    r2_interface_g1 = input("Enter the interface name for Router R2's second interface (e.g., GigabitEthernet0/0/1): ")
    r2_int_g1_ip = input(f"Enter the network for Router R2 {r2_interface_g1} (e.g., 192.168.2.1): ")
    r2_int_g1_mask = input("Enter the subnet mask for this interface (e.g., 255.255.255.0): ")
    r2_network_1 = f"{r2_int_g1_ip} 0.0.0.255"
    r2_network_2 = f"{r2_int_g0_ip} 0.0.0.255"

    # Configuration for Router R1
    config_r1 = f"""
enable
configure terminal
hostname R1
interface {r1_interface_g0}
ip address {r1_int_g0_ip} {r1_int_g0_mask}
no shutdown
exit
interface {r1_interface_g1}
ip address {r1_int_g1_ip} {r1_int_g1_mask}
no shutdown
exit
"""
    if ospf_enabled:
        config_r1 += f"""
router ospf 1
network {r1_network_1} area 0
network {r1_network_2} area 0
exit
"""

    # Configuration for Router R2
    config_r2 = f"""
enable
configure terminal
hostname R2
interface {r2_interface_g0}
ip address {r2_int_g0_ip} {r2_int_g0_mask}
no shutdown
exit
interface {r2_interface_g1}
ip address {r2_int_g1_ip} {r2_int_g1_mask}
no shutdown
exit
"""
    if ospf_enabled:
        config_r2 += f"""
router ospf 1
network {r2_network_1} area 0
network {r2_network_2} area 0
exit
"""

    # Print the configurations to console (or send to device)
    print("\nConfiguration for Router R1:")
    print(config_r1)
    print("Configuration for Router R2:")
    print(config_r2)

if __name__ == "__main__":
    main()
