# BauResQ - Autonomous Rescue Robot

![BauResQ Logo](https://i.ibb.co/dpgVQpD/Bau-Res-Q-2.png)

**BauResQ** is an autonomous rescue robot designed to assist in search and rescue missions. Powered by NVIDIA's Jetson Nano and programmed in Python, BauResQ can navigate through challenging environments, identify obstacles, and assist in locating individuals in need. This project showcases the integration of robotics, AI, and edge computing to create a life-saving solution.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Installation](#software-installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Autonomous Navigation**: Utilizes advanced algorithms for pathfinding and obstacle avoidance.
- **Object Detection**: Powered by deep learning models to detect objects and persons in real-time.
- **Real-time Communication**: Sends live data and video feeds to a control center.
- **Edge Computing**: Leverages Jetson Nano's GPU for on-device AI inference.
- **Modular Design**: Easily extendable and customizable for various missions.

## Hardware Requirements

- **NVIDIA Jetson Nano Developer Kit**
- **4GB microSD Card (minimum)**
- **Camera Module** (e.g., Raspberry Pi Camera v2)
- **Ultrasonic Sensors** for obstacle detection
- **Servo Motors** for movement control
- **Li-Po Battery** (7.4V, 2200mAh)
- **Chassis and Frame** for assembly

## Software Installation

### Prerequisites

Ensure your Jetson Nano is set up with a proper OS and has internet access. Follow these steps to get BauResQ up and running:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/BauResQ.git
    cd BauResQ
    ```

2. **Install Dependencies**:
    ```bash
    sudo apt-get update
    sudo apt-get install -y python3-pip
    pip3 install -r requirements.txt
    ```

3. **Setup Jetson Inference**:
    - Follow [NVIDIA's guide](https://github.com/dusty-nv/jetson-inference) to set up the inference environment on your Jetson Nano.

4. **Configure the Camera and Sensors**:
    - Refer to the hardware documentation in the `docs/hardware_setup.md` file for detailed setup instructions.

## Usage

Once the installation is complete, you can start using BauResQ with the following commands:

### Run the Autonomous Mode
```bash
python3 src/autonomous.py
