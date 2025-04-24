# Phonopass— Intelligent Voice Assistant with Secure OTP Verification

**Phonopass** is a Python-powered voice assistant that integrates cutting-edge **speech recognition** and **email-based OTP authentication**, enabling seamless interaction and enhanced security. This project demonstrates how voice commands can be used not just to control applications but also to initiate sensitive actions with verification mechanisms.

---

## 🎯 Project Overview

In today's digital world, integrating speech interfaces and authentication into everyday systems brings both convenience and security. **Phonopass** enables users to:

- Communicate via voice using real-time speech recognition.
- Trigger actions such as opening websites or verifying identity through email-based OTP.
- Get spoken responses, making the interaction feel more natural and intuitive.

Whether you're working on a personal assistant, smart automation system, or secure application workflows, this project provides a solid foundation for real-world voice-activated applications.

---

## 🌟 Features

✅ **Voice-Activated Interface**  
Command your assistant using natural speech via the Google Speech Recognition API.

✅ **Text-to-Speech (TTS) Responses**  
Your assistant speaks back to you using the `pyttsx3` engine.

✅ **Secure OTP Verification**  
Generates and sends a One-Time Password (OTP) to the user's email and validates it to proceed.

✅ **Smart Web Integration**  
Automatically opens websites like Amazon, Flipkart, or a custom link using simple voice commands.

✅ **Interactive Command Line Interface**  
Prompts the user in real time and supports OTP verification via CLI.

## 📂 Project Structure

├── sample.py        # Main voice assistant logic
├── otp.py           # Email-based OTP sending & verification
├── README.md        # Project documentation
└── requirements.txt # Python package requirements
