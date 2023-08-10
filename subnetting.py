import ipaddress
from graphviz import Digraph
from color_mapping import cidr_to_color
from typing import List


def calculate_subnets(
    network_cidr: str,
    end_prefixlen: int,
    occupied_subnets: List[str],
    full_representation: bool,
):
    """
    Calculates the subnets of a given network and creates a visual representation of these subnets.
    """

    # Check if end_prefixlen is within acceptable range
    if end_prefixlen < 1 or end_prefixlen > 30:
        raise ValueError("end_prefixlen must be between 1 and 30")

    # Create a new Digraph object
    dot = Digraph(comment="Subnets Tree", format="pdf")

    # Convert the network from CIDR notation to an IP network object
    network = ipaddress.ip_network(network_cidr)

    # Initialize a dictionary to hold the subnets for each prefix length
    prefixlen_to_subnets = {network.prefixlen: [network]}

    # Determine whether the network is occupied
    subnet_occupancy = {network: network in occupied_subnets}

    # Get information about the network
    subnet_info = get_subnet_info(network, subnet_occupancy[network])

    # Add the network as the root node of the graph
    dot.node(
        str(network),
        label=subnet_info,
        fontcolor="black",
        fontsize="20.0",
        fontname="Helvetica-bold",
        shape="none",
    )

    # Convert occupied_subnets to a set of IP networks for faster lookup
    occupied_subnets = set(ipaddress.ip_network(subnet) for subnet in occupied_subnets)

    # Create subnets for each prefix length from the network's prefix length to the end prefix length
    for prefixlen in range(network.prefixlen + 1, min(end_prefixlen + 1, 31)):
        # Initialize a list to hold the subnets for the current prefix length
        prefixlen_to_subnets[prefixlen] = []

        # Iterate over the parent subnets
        for parent_subnet in prefixlen_to_subnets[prefixlen - 1]:
            # Skip occupied parent subnets if not doing a full representation
            if parent_subnet in occupied_subnets and not full_representation:
                continue

            # Create subnets of the current prefix length from the parent subnet
            for subnet in parent_subnet.subnets(new_prefix=prefixlen):
                # Determine whether the subnet is occupied
                is_occupied = (
                    subnet in occupied_subnets or subnet_occupancy[parent_subnet]
                )

                # Record the occupancy status of the subnet
                subnet_occupancy[subnet] = is_occupied

                # Get information about the subnet
                subnet_info = get_subnet_info(subnet, is_occupied)

                # Add the subnet as a node to the graph
                dot.node(
                    str(subnet),
                    label=subnet_info,
                    fillcolor="white",
                    style="filled",
                    fontname="Helvetica",
                    shape="none",
                )

                # Add an edge from the parent subnet to the subnet
                dot.edge(str(parent_subnet), str(subnet), color="blue")

                # Add the subnet to the list of subnets for the current prefix length
                prefixlen_to_subnets[prefixlen].append(subnet)

    # Render the graph to a PDF file, open it for viewing, and clean up the DOT file after rendering
    dot.render("subnets_tree", view=True, cleanup=True)


def get_subnet_info(subnet, is_occupied=False):
    """
    Generates the HTML markup to visualize information about a subnet.
    """

    # If the subnet is occupied, create a row for the table to indicate this. Otherwise, create an empty string.
    occupied_row = (
        '<TR><TD COLSPAN="2" BGCOLOR="red"><b>OCCUPIED</b></TD></TR>'
        if is_occupied
        else ""
    )

    # Use an f-string to generate the HTML markup for the table.
    # This table includes information about the subnet's prefix length, network address, netmask,
    # minimum host address, maximum host address, and broadcast address.
    subnet_info = f"""< 
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    {occupied_row}
    <TR><TD COLSPAN="2" BGCOLOR="{cidr_to_color.get(subnet.prefixlen)}"><b>Subnet: {subnet}</b></TD></TR>
    <TR><TD BGCOLOR="lightgrey">Network</TD><TD BGCOLOR="white">{subnet.network_address}</TD></TR>
    <TR><TD BGCOLOR="lightgrey">Netmask</TD><TD BGCOLOR="white">{subnet.netmask}</TD></TR>
    <TR><TD BGCOLOR="lightgrey">HostMin</TD><TD BGCOLOR="white">{subnet.network_address + 1}</TD></TR>
    <TR><TD BGCOLOR="lightgrey">HostMax</TD><TD BGCOLOR="white">{subnet.broadcast_address - 1}</TD></TR>
    <TR><TD BGCOLOR="lightgrey">Broadcast</TD><TD BGCOLOR="white">{subnet.broadcast_address}</TD></TR>
    </TABLE>
    >"""

    # Return the HTML markup
    return subnet_info
