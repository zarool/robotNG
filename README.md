# robotNG

* The robot model was prepared in the 3DExperience software.
* Controlling the manipulator using an ESP32 microcontroller - communication over LAN network via a UDP server created
  as a docker compose.
* Controlling the robot through an application launched by the user, which then connects to the UDP server and ESP32
* By using dockers, each of modules are launched separately which results in easier to find a bug or core of a problem (
  similar to [ROS](https://www.ros.org/))

## Description of modules

|          | Short desc                                                                                  |
|----------|---------------------------------------------------------------------------------------------|
| app      | contain GUI (pygame) which connects with UDP Server<br>Separate docker image                |
| env      | UDP server, manage received and sent brackets, calculate movement<br> Separate docker image |
| firmware | ESP32 module - connection with env (server UDP), control servos                             |
| hardware | Servos, connections on breadboard (later PCB), 3D model                                     |

## Dependencies

## Hardware

## UML diagram

Diagram showing simplified image of how structure works

```mermaid
graph LR
A[app] -- UDP socket, port 8000 --> B[env: UDP server]
B -- UDP socket, connection --> D[ESP32: controlling servos]
B --> C[env: Calcuations]
C -- UDP socket, port 9000 --> D
```

