# Nike Size Check

A Python script to monitor Nike product availability and send notifications via email and Discord when specific shoe sizes become available. The script uses Nike's API to check real-time inventory status.

## Features

- Monitors Nike product availability through official Nike API endpoints
- Configurable shoe size, style, and product ID tracking
- Email notifications when items become available
- Discord webhook integration for instant alerts
- Customizable check frequency
- Error handling and logging

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nike-size-check.git
   cd nike-size-check
   ```
2. Install required dependencies and create virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create environment variables file:
   ```bash
   cp .env.sample .env
   ```

4. Configure your .env file with:
   - SMTP server details
   - Email login credentials 
   - Discord webhook URL
   - Nike product details (style color, product ID, size)
   - Notification email address

## Guide

To find the required product ID and style color:

1. Open Nike's website and navigate to your desired product
2. Open browser Developer Tools (F12 or right-click -> Inspect)
3. Go to the Network tab in Developer Tools
4. Add the product to your cart
5. In the Network tab, look for API calls containing:
   - `productId` - A long string like "016cc1fe-3531-5775-9f58-4a927e35171b"
   - `styleColor` - Usually in format "XXXXXX-XXX" like "BQ6817-302"
6. Copy these values and add them to your .env file

The product ID and style color are unique identifiers used by Nike's API to track specific products and variants. Make sure to copy them exactly as they appear.