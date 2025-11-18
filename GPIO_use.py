import lgpio
import time

# Open the GPIO chip (e.g., chip 0)
h = lgpio.gpiochip_open(0)

# Claim a pin as output (e.g., pin 17)
lgpio.gpio_claim_output(h, 17)

# Write a high value
lgpio.gpio_write(h, 17, 1)
time.sleep(1)

# Write a low value
lgpio.gpio_write(h, 17, 0)

# Release the pin
lgpio.gpio_free(h, 17)

# Close the GPIO chip
lgpio.gpiochip_close(h)