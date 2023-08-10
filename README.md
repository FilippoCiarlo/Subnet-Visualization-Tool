# Subnet Visualization Tool

This project provides a tool to visualize IP Subnets within a given Network. It takes a network in [CIDR notation](https://it.wikipedia.org/wiki/Classless_Inter-Domain_Routing), a list of occupied Subnets, and an end prefix length to determine the depth of the subnet tree. The tool then generates a visual representation of the Subnets using the Graphviz library.

## Features

- Visualize a given network's Subnets up to a specified Subnet Mask.
- Highlight Occupied Subnets within the Network.
- Option for a full representation of Occupied Subnets.

## Requirements

- Python 3.x
- [`ipaddress`](https://docs.python.org/3/library/ipaddress.html) module (standard library)
- [`graphviz`](https://graphviz.org) library

## Usage

1. Clone the repository:
    ```
    git clone https://github.com/FilippoCiarlo/Subnet-Visualization-Tool.git
    cd Subnet-Visualization-Tool
    ```

2. Install the required libraries:
    ```
    pip install ipaddress
    pip install graphviz
    ```

3. Run the main script:
    ```
    python main.py
    ```

4. Follow the on-screen prompts to input the Network, Occupied Subnets, and other required information.

5. The tool will generate a PDF visualization named `subnets_tree.pdf` in the project directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.