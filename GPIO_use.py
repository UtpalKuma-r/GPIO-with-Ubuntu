import lgpio
import time

# Open the GPIO chip (e.g., chip 0)
h = lgpio.gpiochip_open(0)

# Claim a pin as output (e.g., pin 17)
lgpio.gpio_claim_output(h, 14)

while True:
# Write a high value
    lgpio.gpio_write(h, 14, 1)
    time.sleep(1)
    print("ON")

    # Write a low value
    lgpio.gpio_write(h, 14, 0)
    print("OFF")
    time.sleep(1)

# Release the pin
lgpio.gpio_free(h, 14)

# Close the GPIO chip
lgpio.gpiochip_close(h)