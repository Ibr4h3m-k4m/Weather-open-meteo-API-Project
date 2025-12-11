# Weather Open-Meteo API Project

A Python-based weather application that integrates with the Open-Meteo API to provide comprehensive weather forecasting and meteorological data. This project features a well-structured, modular architecture following best practices for API development.

## 🌤️ Overview

This application serves as a wrapper and enhancement layer for the Open-Meteo API, providing easy access to weather forecasts, historical weather data, and various meteorological information. The Open-Meteo API is a free, open-source weather API that requires no API key and offers lightning-fast response times.

## ✨ Features

- **Real-time Weather Data**: Access current weather conditions for any location
- **Weather Forecasts**: Get detailed weather predictions
- **Historical Weather Data**: Query past weather information
- **Modular Architecture**: Clean separation of concerns with organized code structure
- **RESTful API Design**: Easy-to-use endpoints following REST principles
- **No API Key Required**: Leverages Open-Meteo's free service
- **Fast Response Times**: Optimized for performance

## 📁 Project Structure

```
Weather-open-meteo-API-Project/
├── models/              # Data models and schemas
├── routes/              # API route definitions and endpoints
├── services/            # Business logic and external API integrations
├── utils/               # Helper functions and utilities
├── __pycache__/         # Python cache files
├── .env                 # Environment variables configuration
├── __init__.py          # Package initialization
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── readme.md            # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ibr4h3m-k4m/Weather-open-meteo-API-Project.git
   cd Weather-open-meteo-API-Project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the .env file and adjust settings if needed
   cp .env.example .env
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage

### Basic Example

```python
# Example of using the weather service
from services import WeatherService

# Initialize the service
weather_service = WeatherService()

# Get current weather for a location
weather_data = weather_service.get_current_weather(
    latitude=48.8566,
    longitude=2.3522
)

print(weather_data)
```

### API Endpoints

The application exposes several endpoints for accessing weather data:

- `GET /weather/current` - Get current weather conditions
- `GET /weather/forecast` - Get weather forecast
- `GET /weather/historical` - Get historical weather data

## 🛠️ Technology Stack

- **Python**: Core programming language
- **Open-Meteo API**: Weather data provider
- **Flask/FastAPI**: Web framework (depending on implementation)
- **Requests**: HTTP library for API calls

## 🌐 Open-Meteo API

This project leverages the [Open-Meteo API](https://open-meteo.com/), which provides:

- Free access for non-commercial use
- No API key requirement
- High-resolution weather models
- Sub-10ms response times
- CORS support
- Attribution 4.0 International (CC BY 4.0) license

## 📦 Dependencies

All required Python packages are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

Common dependencies typically include:
- `requests` - HTTP library
- `python-dotenv` - Environment variable management
- `flask` or `fastapi` - Web framework
- `pydantic` - Data validation

## ⚙️ Configuration

Configuration is managed through the `.env` file. Key settings include:

```env
# Application settings
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True

# API settings
OPEN_METEO_BASE_URL=https://api.open-meteo.com/v1
```

## 🧪 Testing

```bash
# Run tests (if available)
python -m pytest

# Run with coverage
python -m pytest --cov=.
```

## 📚 API Documentation

### Weather Endpoints

#### Get Current Weather

```http
GET /weather/current?lat={latitude}&lon={longitude}
```

**Parameters:**
- `lat` (float, required): Latitude coordinate
- `lon` (float, required): Longitude coordinate

**Response:**
```json
{
  "temperature": 22.5,
  "humidity": 65,
  "wind_speed": 12.3,
  "weather_code": 0,
  "time": "2024-12-11T14:00:00"
}
```

#### Get Weather Forecast

```http
GET /weather/forecast?lat={latitude}&lon={longitude}&days={days}
```

**Parameters:**
- `lat` (float, required): Latitude coordinate
- `lon` (float, required): Longitude coordinate
- `days` (int, optional): Number of forecast days (default: 7)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Open-Meteo](https://open-meteo.com/) for providing free weather API access
- National weather services for providing the underlying data
- All contributors to this project

## 📧 Contact

**Project Maintainer:** Ibr4h3m-k4m

**Repository:** [https://github.com/Ibr4h3m-k4m/Weather-open-meteo-API-Project](https://github.com/Ibr4h3m-k4m/Weather-open-meteo-API-Project)

For questions, issues, or suggestions, please open an issue on GitHub.

## 🔗 Useful Links

- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [Open-Meteo GitHub Repository](https://github.com/open-meteo/open-meteo)
- [Python Documentation](https://docs.python.org/3/)

---

**Note:** This project is for non-commercial use. If you plan to use it commercially, please review Open-Meteo's terms of service and consider contacting them for commercial licensing.

Made with ☀️ by Ibr4h3m-k4m