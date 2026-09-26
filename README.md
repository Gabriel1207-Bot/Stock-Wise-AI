# Stockwise AI - Intelligent Warehouse Management System

**Theme:** AI Solution for Industries
**Project:** Business Analysis 3.2 Capstone

## Overview
Stockwise AI is an AI-powered Warehouse Management System (WMS) designed to transform manual, paper-based municipal and industrial warehouses into autonomous, data-driven hubs. It uses Computer Vision, Predictive Analytics, and Natural Language Processing to eliminate stockouts, theft, and waste.

## Key Features
- **Computer Vision (YOLOv8):** Drones and CCTV auto-count stock.
- **Predictive Analytics (LSTM/Prophet):** Forecasts winter pipe bursts and auto-generates purchase orders.
- **Intelligent Slotting (K-Means):** Places fast-moving items near dispatch to save time.
- **Anomaly Detection (Isolation Forest):** Flags unusual stock movements (e.g., theft).
- **Multilingual Chatbot (BERT + Whisper):** Voice queries in English, Sesotho, and IsiZulu.

## Repository Structure
- `data/` - Simulated municipal consumption data.
- `src/` - Python AI modules (Forecasting, Anomaly Detection, Slotting, Chatbot).
- `app.py` - Streamlit dashboard prototype.
- `docs/` - Project documentation, site visit report, and final report.

## Getting Started
```bash
pip install pandas scikit-learn streamlit
python src/stockwise_ai.py
streamlit run app.py
