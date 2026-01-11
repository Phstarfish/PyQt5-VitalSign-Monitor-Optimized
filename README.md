**Project Overview**
This project is a high-performance upper computer software designed for real-time physiological parameter monitoring, developed using Python 3 and the PyQt5 framework. It serves as the software interface for the LY-M501 physiological signal acquisition system, capable of parsing, processing, and visualizing five key vital signs: Electrocardiogram (ECG), Pulse Oxygen Saturation (SpO2), Respiration (RESP), Non-Invasive Blood Pressure (NIBP), and Body Temperature (TEMP).

The system features a completely refactored Graphical User Interface (GUI) optimized for clinical environments, integrating digital signal processing algorithms and a multi-modal safety alarm mechanism to ensure diagnostic accuracy and operational efficiency.

**Key Features & Optimizations**
**1. Medical-Grade Visual Ergonomics**
Dark Mode Interface: The GUI has been redesigned with a high-contrast "Dark Mode" (pure black background #000000) to minimize screen glare and reduce visual fatigue during long-term monitoring in low-light clinical settings.
Anti-Aliased Rendering: Integrated QPainter.Antialiasing technology to eliminate jagged artifacts in waveform rendering. This ensures smooth, high-fidelity visualization of physiological curves (e.g., ECG P-waves and T-waves) on high-resolution displays.
Color-Coded Visualization: Adopted an industry-standard color coding system (Green for ECG, Yellow for SpO2, Cyan for RESP) to enhance parameter distinction and readability.

**2. Advanced Signal Processing**
Real-Time Noise Suppression: Implemented a Moving Average Filter algorithm within the data processing pipeline. This software-defined filter effectively suppresses high-frequency random noise, power line interference, and baseline drift in raw ECG signals, significantly improving the Signal-to-Noise Ratio (SNR) for clinical diagnosis.

**3. Multi-Modal Safety Alarm System**
Audiovisual Feedback Loop: Built a closed-loop alarm mechanism compliant with medical safety standards.
Visual Alert: Numerical indicators turn bold red immediately when parameters exceed preset safety thresholds (e.g., HR > 100 or < 60 bpm, SpO2 < 90%).
Auditory Alert: Synchronized 2500Hz high-frequency buzzer (via winsound) ensures immediate awareness of critical patient conditions even when the display is not being actively viewed.

**4. Enhanced Interactivity & Control**
Waveform Freeze Function: Introduced a non-blocking "Freeze" feature based on the Signal and Slot mechanism. This allows clinicians to pause the waveform display for detailed analysis of transient events (like arrhythmias) without interrupting the background serial data buffering, ensuring no data loss during the freeze period.
Streamlined UX: Removed redundant UI components (e.g., non-functional dropdowns) and standardized typography using SimHei (Black Body) and Arial fonts for a modern, professional look.

**Hardware & Environment**
**Hardware Platform:** LY-M501 Human Physiological Parameter Monitoring System.
**Development Environment:** Python 3.11, PyQt5, PyCharm Professional.
**OS Compatibility:** Windows 10/11 (64-bit).
