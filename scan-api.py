from typing import Optional
import logging
import time

import requests

from notifications import send_mail, send_discord_message
from config import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():

    API_GTIN_URL = (
        "https://api.nike.com/deliver/available_gtins/v3/?filter=styleColor("
        + config.STYLE_COLOR
        + ")&filter=merchGroup(EU)"
    )
    API_PRODUCT_URL = (
        "https://api.nike.com/merch/skus/v2?filter=productId("
        + config.PRODUCT_ID
        + ")&filter=country(PL)"
    )
    PAGE_URL = "https://www.nike.com/pl/t/buty-do-skateboardingu-sb-dunk-low-pro-Rj3hwM/BQ6817-302"

    logger = logging.getLogger(__name__)

    while True:
        logger.info("started")
        try:
            sku_response = requests.request("GET", API_PRODUCT_URL)
            gtin = get_gtin_by_shoe_size(sku_response.json(), config.SHOE_SIZE)
            response = requests.request("GET", API_GTIN_URL)
            if not gtin:
                logger.info("no gtin found")
                continue
            logger.info(f"Status code: {response.status_code}")
            data = response.json()
            for obj in data["objects"]:
                if obj["gtin"] == gtin:
                    if obj["available"]:
                        logger.info("available!!!")
                        send_mail("Shoe available!!!!!", PAGE_URL, config.NOTIFICATION_RECEIVER)
                        send_discord_message("@everyone Shoe available!!!!! \n" + PAGE_URL)
                    else:
                        logger.info(f'not available - {obj["modificationDate"]}')
        except Exception as e:
            logger.error(f"error occurred: {e}")
        logger.info("sleeping")
        time.sleep(15)


def get_gtin_by_shoe_size(data: dict, shoe_size: str) -> Optional[str]:
    for item in data.get("objects", []):
        if item.get("nikeSize") == shoe_size:
            return item.get("gtin")
    return None


if __name__ == "__main__":
    main()
