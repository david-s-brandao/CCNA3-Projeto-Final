# CCNAv7 ENSA Final Project: Enterprise Network Deployment

This repository contains the configuration files, documentation, and automation scripts for the final comprehensive lab of the CCNAv7 Enterprise Networking, Security, and Automation (ENSA) course.

## Project Overview

The project simulates the network infrastructure of a Croatian service company specializing in tech gadgets. The topology interconnects the headquarters in **Zagreb** with two branch offices in **Pula** and **Split**.

The objective is to plan the IP addressing scheme and configure all network equipment to guarantee full connectivity, security, and service availability across all locations.

## Network Scenario & Topology

The infrastructure consists of three main sites connected via simulated Internet links. The connectivity relies on GRE/IPSec VPN tunnels to establish secure communications between sites.

**Locations:**
* **Zagreb (HQ):** Central hub, hosts DHCP Server and NTP Master.
* **Pula (Branch):** Coastal branch, VPN connected.
* **Split (Branch):** Coastal branch, VPN connected.

**Hardware Resources:**
* 3x Routers (Cisco 4221/2911 with IOS XE)
* 4x Switches (Cisco 2960)
* 2x Multi-Layer Switches (Cisco 3560/3650/3750)
* 1x Wireless LAN Controller (2100/2500)
* 3x Lightweight Access Points (1702)
* End devices: PCs, Laptops, IP Phones

## Technical Implementation

### 1. Connectivity & Routing
* **Addressing:** Custom IPv4 subnetting plan implemented for LANs and WAN links.
* **Routing Protocol:** OSPF (Process ID 100) configured in Area 0 for internal routing.
* **Redistribution:** Default routes are redistributed into the OSPF process.
* **NAT:**
    * **Dynamic NAT:** Allows internal networks access to the Internet.
    * **Static NAT (Port Forwarding):** Configured on RT1-Zg to allow external access to HTTP/HTTPS/SSH services.

### 2. VPN Infrastructure (Site-to-Site)
Secure tunnels are established between all three locations using the following IPSec parameters:
* **ISAKMP Policy:** 100
* **Encryption:** AES 128
* **Hash:** SHA
* **Diffie-Hellman:** Group 5
* **Authentication:** Pre-shared keys
* **Tunnel Addresses:**
    * Zagreb-Pula: 10.0.0.0/30
    * Zagreb-Split: 10.0.0.4/30
    * Pula-Split: 10.0.0.8/30

### 3. Services & Telephony
* **VoIP:** Cisco Call Manager Express (CME) configured on routers in Pula, Split, and the DHCP Server in Zagreb.
    * Includes VLAN 40 configuration for Voice traffic.
    * DHCP Pools configured with Option 150.
* **NTP:** Hierarchical time synchronization. RT1-Zg syncs with external stratum; all other devices sync with RT1-Zg.

### 4. Security & Access Control
* **ACLs (Access Control Lists):**
    * Guest networks restricted to Internet-only access.
    * VoIP network restricted from Internet access.
    * Management access (SSH) restricted to ADMIN/STAFF networks.
    * SNMP requests restricted to the monitoring server.

## Monitoring & Automation

### Network Monitoring
* **SNMP:** SNMPv2c configured on all devices (Community string: `cisco`, Read-Only).
* **Syslog:** Centralized logging configured with Trap Level 'Informational'.
* **LibreNMS:** A virtual machine is deployed with LibreNMS to monitor device health and act as the syslog server.

### Configuration Backup (Ansible)
* **Tool:** Ansible installed via WSL (Windows Subsystem for Linux).
* **Playbook:** A custom playbook exports the running configuration of all intermediate devices for backup purposes.

## Repository Structure

```text
/
├── configs/             # Startup configurations for Routers and Switches
├── docs/                # Addressing tables and topology diagrams
├── ansible/             # Playbooks and inventory files for backup
├── scripts/             # Snippets for ACLs and Crypto Maps
└── README.md            # Project documentation
```

## Setup Instructions

    Physical/Simulation Setup: Replicate the topology in Packet Tracer or physical labs using the provided diagrams.
    Base Configuration: Apply the initial interface and VLAN configurations found in configs/.

    Deploy Services: Configure OSPF and NAT verify connectivity.

    VPN Establishment: Apply crypto maps to WAN interfaces based on Annex 1 guidelines.

    Monitoring: Start the LibreNMS VM and ensure reachability to the management network.

    Automation: Run the Ansible playbook to verify SSH access and backup capability.

## Authors
*    Student 1 - Zagreb HQ Infrastructure
 *   Student 2 - Pula Branch & Monitoring
  *  Student 3 - Split Branch & Automation