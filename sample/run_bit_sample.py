import base64
from os import getenv
from yk_bit import BaseUrl, Key, capture, verify_images, verify, status, setup, BiTStatus, \
    hardware_reset

"""
First time running:
 - Run the BiT App
 - Run this SDK App
 - If the setup was successful:
   - Comment the "setup" block
"""


# BiometricInThings API Environment Variables
EV_BASE_URL = getenv('YK_BIT_BASE_URL')
EV_API_KEY = getenv('YK_BIT_X_API_KEY')


BaseUrl.set(EV_BASE_URL)
Key.set(EV_API_KEY)


def base64_to_file(filename: str, data: str):
    with open(f"{filename}.png", "wb") as fh:
        fh.write(base64.decodebytes(data.encode('utf-8')))


if __name__ == "__main__":

    # Setup
    try:
        print("Setting up BiT")
        setup()
        print(f"BiT Setup Successful. \n")
    except Exception as ex:
        print(f"BiT Setup unsuccessful. \n")
        print(ex)
        exit()

    # Status
    bit_availability = status()
    print(f"BiT Availability: {bit_availability} \n")

    if bit_availability == BiTStatus.Available:
        # Capture
        captured = capture(capture_timeout=10)
        print(f"Capture: \n"
              f"\t Status: {captured.capture_status} \n"
              # f"\t Image: {captured.image} \n"
              )
        if captured.image is not None:
            base64_to_file("captured", captured.image)

            # Verify
            verified = verify(reference_image=captured.image, capture_time_out=10, anti_spoofing=True)
            print(f"Verify: \n"
                  f"\t Matching Score: {verified.matching_score} \n"
                  f"\t Status: {verified.verify_status} \n"
                  # f"\t Verified Image: {verified.verified_image} \n"
                  )
            base64_to_file("verified", verified.verified_image)

            # Verify Images
            verified_images = verify_images(probe_image=captured.image, reference_image=verified.verified_image)
            print(f"Verify Images: \n"
                  f"\t Matching Score: {verified_images.matching_score} \n"
                  f"\t Status: {verified_images.verify_images_status} \n")

            # Hardware Reset
            hardware_reset = hardware_reset()
            print(f"Hardware reset: {hardware_reset.message}")
