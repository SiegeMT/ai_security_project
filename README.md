# AI Security Platform for Log Anomaly Detection

## Overview

This project implements a robust AI-powered system to analyze server logs, detect anomalies, and ensure high levels of security through HSM/CAC authentication. It leverages modern AI techniques and a modular Python architecture.

## Features

- **AI-Powered Anomaly Detection**: Uses transformer models to identify unusual patterns in logs.
- **Secure Authentication**: HSM/CAC authentication via NGINX.
- **Dynamic Dashboard**: Built with Panel, offering interactive visualizations powered by Holoviews.
- **Efficient Log Handling**: Processes large log datasets using Polars.
- **Modular Design**: Flexible configuration with Param and python-decouple.

## Technologies

- **Backend**: Django, Polars, LangChain, python-decouple.
- **Frontend**: Panel, Holoviews, TailwindCSS.
- **Security**: NGINX, PKCS11, HSM/CAC.
- **Database**: PostgreSQL with pgvector.

## Getting Started

1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Configure `constants.py` using python-decouple.
4. Deploy using Docker or Ansible scripts provided in the `deployment/` directory.
