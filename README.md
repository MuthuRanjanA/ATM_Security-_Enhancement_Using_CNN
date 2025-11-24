# 🏦 IoT-Based ATM Burglary Prevention System

An IoT-based security system designed to detect and prevent burglary attempts in ATM machines using sensors, Python automation, and alert mechanisms.  
This project focuses on real-time monitoring and automatic alert generation to protect ATM infrastructure from physical attacks.

---

## 📌 Project Overview

The **IoT ATM Burglary Prevention System** uses sensors such as vibration sensors, ultrasonic sensors, gas/fire sensors, and PIR motion detectors to monitor suspicious activities around an ATM machine.

Whenever unusual movement, break-in attempts, or smoke/fire is detected, the system instantly sends alerts and triggers automated safety actions through Python.

This project demonstrates how IoT + Python can provide an additional security layer for banking systems.

---

## 🚀 Key Features

### ✔ Real-Time Intrusion Detection
- Detects vibration or shock (hammer, drilling attempts)
- Detects unauthorized motion inside ATM cabin
- Identifies attempts to break open or tilt the ATM machine

### ✔ Sensor-Based Monitoring
- **PIR Sensor** → Human motion detection  
- **Vibration Sensor** → Break/open attempts  
- **Ultrasonic Sensor** → Distance-based intrusion detection  
- **Gas/Smoke Sensor** → Fire or explosion alerts  

### ✔ Automated Alert System (Python)
- Sends **SMS/email alerts** to security personnel  
- Triggers **buzzer alarm**  
- Can activate **camera recording** (if connected)  
- Logs timestamped events

### ✔ Continuous Monitoring
- Real-time data streaming from sensors  
- Python-based processing loop  
- Safe shutdown and recovery features  

### ✔ Easy Integration
- Can be linked with:
  - CCTV systems  
  - GSM modules  
  - Central security dashboard  
  - Bank security network  

---

## 🛠 Tech Stack

| Component        | Technology / Hardware |
|------------------|------------------------|
| **Controller**   | Arduino / Raspberry Pi |
| **Programming**  | Python (alert & logic scripts) |
| **Sensors**      | PIR, Ultrasonic, Vibration, Gas/Smoke |
| **Communication**| GSM / WiFi / MQTT |
| **Alerts**       | Email/SMS APIs, Buzzer |

---

## 📂 Project Structure

