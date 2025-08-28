from shop.models import Product

Product.objects.create(
    name="Wireless Mouse",
    description="Ergonomic design, long battery life, smooth tracking.",
    price=25.00,
    image_url="https://img.icons8.com/color/96/000000/wireless-mouse.png"
)

Product.objects.create(
    name="Bluetooth Headphones",
    description="High-fidelity sound, noise cancellation, comfortable fit.",
    price=60.00,
    image_url="https://img.icons8.com/color/96/000000/headphones.png"
)

Product.objects.create(
    name="USB-C Charger",
    description="Fast charging, compact size, universal compatibility.",
    price=18.00,
    image_url="https://img.icons8.com/color/96/000000/usb-c.png"
)

Product.objects.create(
    name="Laptop Stand",
    description="Adjustable height, sturdy build, portable design.",
    price=32.00,
    image_url="https://img.icons8.com/color/96/000000/laptop-stand.png"
)
