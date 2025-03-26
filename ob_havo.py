import random

def ob_havo(shahar):
    ob_havo_malumotlari = [
        f"{shahar} shahrida quyoshli, harorat 25°C.",
        f"{shahar} shahrida biroz bulutli, harorat 18°C.",
        f"{shahar} shahrida yomg‘irli, harorat 12°C.",
        f"{shahar} shahrida tuman, harorat 15°C.",
        f"{shahar} shahrida kuchli shamol, harorat 10°C.",
        f"{shahar} shahrida qor yog‘moqda, harorat -2°C.",
        f"{shahar} shahrida momaqaldiroq bilan yomg‘ir, harorat 14°C.",
        f"{shahar} shahrida jazirama, harorat 35°C.",
        f"{shahar} shahrida sovuq, harorat -5°C."
    ]
    
    return random.choice(ob_havo_malumotlari)