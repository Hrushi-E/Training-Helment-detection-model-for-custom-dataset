import random

def main():
    # Load image addresses from whole.txt
    with open('/content/darknet/data/whole.txt', 'r') as file:
        image_addresses = file.readlines()

    # Randomly select a portion for the test set
    total_images = len(image_addresses)
    test_size = int(0.1 * total_images)  # 10% of total images

    test_image_addresses = random.sample(image_addresses, test_size)
    train_image_addresses = [address for address in image_addresses if address not in test_image_addresses]

    # Write to test.txt and train.txt
    with open('/content/darknet/data/test.txt', 'w') as file:
        file.writelines(test_image_addresses)

    with open('/content/darknet/data/train.txt', 'w') as file:
        file.writelines(train_image_addresses)

if __name__ == "__main__":
    main()
