import subprocess

def recognize_license_plate(image_path):
    """Recognizes license plates using OpenALPR."""
    command = f"alpr -c us {image_path}"  # Change 'us' to your country
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode()

# Test
if __name__ == "__main__":
    print("Detected License Plate:", recognize_license_plate("static/car_plate.jpg"))