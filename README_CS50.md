# Subnet Visualization Tool

#### Video Demo:  <URL HERE>


#### Description:

This project provides a tool to visualize IP Subnets within a given Network. It takes a network in [CIDR notation](https://it.wikipedia.org/wiki/Classless_Inter-Domain_Routing), a list of occupied Subnets, and an end prefix length to determine the depth of the subnet tree. The tool then generates a visual representation of the Subnets using the Graphviz library.

*Features*

- Visualize a given network's Subnets up to a specified Subnet Mask.
- Highlight Occupied Subnets within the Network.
- Option for a full representation of Occupied Subnets.

*Installation*

1. Install the required libraries:
    ```
    pip install ipaddress
    pip install graphviz
    ```

2. Run the main script:
    ```
    python main.py
    ```

3. Follow the on-screen prompts to input the Network, Occupied Subnets, and other required information.

4. The tool will generate a PDF visualization named `subnets_tree.pdf` in the project directory.