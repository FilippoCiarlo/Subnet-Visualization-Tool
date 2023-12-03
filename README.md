# Subnet Visualization Tool

#### Video Demo:
https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/a3f8e114-be07-486a-b711-8c1ddf6f6fb3

#### Description:
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

### 1. Clone the repository:
```
git clone https://github.com/FilippoCiarlo/Subnet-Visualization-Tool.git
cd Subnet-Visualization-Tool
```

### 2. Install the required libraries:
```
pip install ipaddress
pip install graphviz
```

### 3. Run the main script:
```
python main.py
```    
### 4. Enter the Target Network Address in [CIDR notation](https://it.wikipedia.org/wiki/Classless_Inter-Domain_Routing):
Input the IP address of the network you wish to analyze, using Classless Inter-Domain Routing (CIDR) notation. CIDR notation is a method used to create unique identifiers for networks and individual devices. This notation combines the standard IP address with a suffix that indicates the number of bits that represent the network portion of the address. For example, '192.168.1.0/24' indicates a network IP address of '192.168.1.0' with a subnet mask of 24 bits. This step is crucial for accurately defining the scope and range of the network for your analysis.

<img width="819" alt="Network" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/1464e550-e250-4447-a979-249a8f02a733">

### 5. Enter the Count and Details of Occupied Subnets in [CIDR notation](https://it.wikipedia.org/wiki/Classless_Inter-Domain_Routing):
Specify the number of subnets that are currently in use within your network, and provide their corresponding IP addresses using Classless Inter-Domain Routing (CIDR) notation. 

<img width="819" alt="Occupied Subnets" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/1cd17e08-a364-47db-a61f-f2fb447a91d2">

### 6. Choose for a Full or Compact Representation of the Subnet:

<img width="819" alt="Full or Compact Representation" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/f465b03f-71a4-4462-ac67-e867ebf456d9">

#### 6.1 Full Representation
This approach is comprehensive in nature, showcasing every layer of the network without exception. In Full Representation, all subnets, including subnets within occupied subnets, are displayed. This method ensures a complete, detailed view of the network's structure, leaving no stone unturned. It’s particularly useful for in-depth analysis, allowing network administrators to see every component and their interconnections.

<img width="1423" alt="Full Representation" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/00a25305-8bc7-4a1b-9a61-7f6d27a8f793">

#### 6.2 Compact Representation
In contrast, the Compact Representation adopts a more streamlined approach. When a subnet is occupied, its internal subnets are not visualized in the diagram. This form of representation focuses on the broader picture, omitting the finer details of occupied subnets. It’s akin to viewing a tree without examining the occpied leafs. This method is beneficial for general overviews or when the details of internal occupied subnets are not necessary for the task at hand.

<img width="1440" alt="Compact Representation" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/9593ba34-d89b-4ecb-9722-2c657654de87">

### 7. Define the Maximum Subnet Mask Value:<br>
By specifying the maximum subnet mask for your network, you are effectively setting the tree depth in your network structure. This value determines how detailed or granular your network tree will be, representing the deepest level of subnetting possible within your network hierarchy. A more specific subnet mask correlates with a deeper tree depth, allowing for finer segmentation and organization of network addresses.

<img width="819" alt="Maximum Subnet Mask Value" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/90196351-5576-4263-9805-0d587ff88188">

### 8. Automatic Generation of Subnet Tree PDF:
Upon completion of the analysis, the tool will automatically generate a visual representation of the Subnet Tree. This visualization will be saved as a PDF file, named `subnets_tree.pdf`, and it will be located in your project's directory. This file provides a comprehensive graphical representation of the network's subnet structure, making it easier to understand and analyze the network's hierarchy and segmentation. You can access this file in the specified directory to view, share, or print the subnet tree for further use or documentation purposes.

<img width="693" alt="subnets_tree file" src="https://github.com/FilippoCiarlo/Subnet-Visualization-Tool/assets/26838702/85634924-ed15-4c5f-ac76-ef8797d5e092">

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
