# desk_buddy
A Raspberry Pi-powered ambient desk assistant with a Tamagotchi-style companion, local LLM, and e-ink display.

Designed to be a low-distraction, voice-first device that lives on your desk — showing essential information like weather and calendar, while interacting through a simple AI companion.

## 🧠 Concept

 - 🖼️ Runs inside a photo frame
 - ⚫ Uses an e-ink display (low power, no glare) 
 - 🐣 Features a Tamagotchi-style AI companion
 - 🎤 Voice-first interaction (with minimal screen UI)

## 🚀 Features

| Feature            | Description                        | Status         |
| ------------------ | ---------------------------------- | -------------- |
| ⛅ Weather Forecast | Current conditions + 3-day outlook | 🟡 In Progress |
| 📆 Calendar        | Monthly calendar view              | 🔴 Not Started |
| 🐣 Tamagotchi      | Interactive companion UI           | 🔴 Not Started |
| 🤖 Local LLM       | Voice assistant with TTS           | 🔴 Not Started |

## 🧰 Hardware

| Component            | Purpose               |
| -------------------- | --------------------- |
| Raspberry Pi 5 (8GB) | Main computer          |
| Waveshare 7.5" e-ink display   | Low-power display     |
| Photo frame          | Enclosure / aesthetic |

## 🧪 Current Progress
- [X] Weather API integration
- [ ] UI rendering pipeline
- [ ] Tamagotchi state system
- [ ] Voice input
- [ ] LLM integration

## 🧭 Roadmap

- Apply for data.gov.sg API key to access higher rate limits and improved reliability
- Optimize weather data fetching by reducing redundant API calls and consolidating endpoint usage per update cycle
- Main UI set-up
- Design Tamagotchi behavior system
- Integrate local LLM
- Add voice interaction pipeline
