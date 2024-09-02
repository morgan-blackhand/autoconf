# Script to generate DHCP configuration for Cisco Router

# Step 1: Ask how many networks
num_networks = int(input("Enter the number of networks: "))

# Initialize lists to store user inputs
pool_names = []
networks = []
subnet_masks = []
exclusions = []
default_gateways = []
dns_servers = []

# Step 2: Ask for pool names, networks, exclusions, default gateway, and DNS server for each network
for i in range(num_networks):
    print(f"\nNetwork {i+1}:")
    
    # Pool Name
    pool_name = input(f"Enter the name for pool {i+1}: ")
    pool_names.append(pool_name)
    
    # Network Address and Subnet Mask
    network = input(f"Enter the network address for {pool_name} (e.g., 10.1.10.0): ")
    subnet_mask = input(f"Enter the subnet mask for {pool_name} (e.g., 255.255.255.0): ")
    networks.append(network)
    subnet_masks.append(subnet_mask)
    
    # Exclusion Range
    exclusion_range = input(f"Enter the exclusion range for {pool_name} (e.g., 10.1.10.1 10.1.10.10): ")
    exclusions.append(exclusion_range)
    
    # Default Gateway
    default_gateway = input(f"Enter the default gateway for {pool_name}: ")
    default_gateways.append(default_gateway)
    
    # DNS Server
    dns_server = input(f"Enter the DNS server for {pool_name}: ")
    dns_servers.append(dns_server)

# Step 3: Generate the configuration script
print("\nGenerated Cisco Router DHCP Configuration Script:\n")

# Exclude addresses
for i in range(num_networks):
    print(f"ip dhcp excluded-address {exclusions[i]}")

# DHCP Pool configurations
for i in range(num_networks):
    print(f"\nip dhcp pool {pool_names[i]}")
    print(f"network {networks[i]} {subnet_masks[i]}")
    print(f"default-router {default_gateways[i]}")
    print(f"dns-server {dns_servers[i]}")

# Interface configuration example
print("\n# Example interface configuration (you may need to adjust the interface names):")
for i in range(num_networks):
    print(f"interface GigabitEthernet0/0.{i+1}")
    print(f"encapsulation dot1Q {i+1}")
    print(f"ip address {default_gateways[i]} {subnet_masks[i]}")
    print("no shutdown")
