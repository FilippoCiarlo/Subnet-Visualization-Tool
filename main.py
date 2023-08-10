import os
from subnetting import calculate_subnets
import ipaddress


def validate_cidr(input_str):
    """
    Validates if input string is a valid CIDR notation
    """
    try:
        ipaddress.ip_network(input_str)
        return True
    except ValueError:
        print(f"Invalid network input: {input_str}")
        return False


def validate_netmask(min_subnet_mask, input_str):
    """
    Validates if input string is a valid netmask
    """
    try:
        val = int(input_str)
        if min_subnet_mask <= val <= 32:
            return val
        else:
            print(f"Input is not within the range [{min_subnet_mask},32]: {input_str}")
            return False
    except ValueError:
        print(f"Invalid integer input: {input_str}")
        return False


def validate_occupied_subnets_number(input_str):
    """
    Validates if input string is a valid number of occupied Subnets
    """
    try:
        val = int(input_str)
        if val >= 0:
            return val
        else:
            print(f"Input is not a non-negative integer: {input_str}")
            return False
    except ValueError:
        print(f"Invalid integer input: {input_str}")
        return False


def get_network():
    """
    Prompts the user for a Network
    """
    while True:
        network = input("Enter the Network [CIDR Notation] \n> ")
        if validate_cidr(network):
            return network, int(network.split("/")[-1])


def get_occupied_subnets(min_subnet_mask):
    """
    Prompts the user for Occupied Subnets if any
    """
    occupied_subnets = []
    while True:
        num_occupied_subnets = input("Enter the number of occupied Subnets \n> ")
        num_occupied_subnets = validate_occupied_subnets_number(num_occupied_subnets)
        if num_occupied_subnets is not False:
            break

    for i in range(num_occupied_subnets):
        while True:
            subnet = input(f"\t{i+1}° Occupied Subnet [CIDR Notation] > ")
            if validate_cidr(subnet):
                occupied_subnets.append(subnet)
                new_min_subnet_mask = int(subnet.split("/")[-1])
                if min_subnet_mask < new_min_subnet_mask:
                    min_subnet_mask = new_min_subnet_mask
                break
    return occupied_subnets, min_subnet_mask


def get_full_representation():
    """
    Prompt the user if he needs a full representation of the Subnets
    """
    while True:
        full_representation = input(
            "\nDo you need a full representation of the occupied Subnets? [Y/N]\n> "
        )
        if full_representation.upper() == "Y":
            return True
        elif full_representation.upper() == "N":
            return False
        else:
            print(f"Invalid input: {str(full_representation)}")


def get_max_subnet_mask(min_subnet_mask):
    """
    Prompts the user for the Maximum Subnet Mask needed
    """
    while True:
        max_subnet_mask = input("Enter the Maximum Subnet Mask needed \n> /")
        max_subnet_mask = validate_netmask(min_subnet_mask, max_subnet_mask)
        if max_subnet_mask is not False:
            return max_subnet_mask


def calculate_subnets_tree(
    network, max_subnet_mask, occupied_subnets, full_representation
):
    """
    Calls the calculate_subnets function and handles exceptions
    """
    try:
        calculate_subnets(
            network, max_subnet_mask, occupied_subnets, full_representation
        )
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def print_centered_title(title):
    """
    Prints a given title centered on the terminal width with "-" padding
    """
    term_width = os.get_terminal_size().columns
    centered_title = title.center(term_width, "-")
    print(centered_title)


def main():
    print_centered_title(" N E T W O R K ")
    network, min_subnet_mask = get_network()
    print_centered_title("")

    print_centered_title(" O C C U P I E D   S U B N E T S ")
    occupied_subnets, min_subnet_mask = get_occupied_subnets(min_subnet_mask)
    full_representation = get_full_representation()
    print_centered_title("")

    print_centered_title(" T R E E   D E P T H ")
    max_subnet_mask = get_max_subnet_mask(min_subnet_mask)
    print_centered_title("")

    calculate_subnets_tree(
        network, max_subnet_mask, occupied_subnets, full_representation
    )


if __name__ == "__main__":
    main()
