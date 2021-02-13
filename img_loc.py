import os, colorama, time


class Positions:
    def target_dir():
        return os.chdir('/home/kali/Desktop')


    def local_dir():
        return os.chdir('/home/kali/Documents/imloc/')


class Disk:
    def mount(seconds):
        os.system('sudo mount /dev/sda3 ~/Desktop')
        print(colorama.Fore.YELLOW,
                '\nDisk Mounted\n', colorama.Style.RESET_ALL)
        time.sleep(seconds)
        return 'Disk Mounted'


    def unmount():
        os.system('sudo umount /dev/sda3 ~/Desktop')
        print(colorama.Fore.YELLOW,
                '\nDisk Unmounted\n', colorama.Style.RESET_ALL)
        return 'Disk Unmounted'


def find_photos():
    Positions.target_dir()
    Disk.mount(2)
    for root, dirs, files in os.walk(os.getcwd()):
        for photo in files:
            if photo.endswith('.png') or photo.endswith('.jpeg') or photo.endswith('jpg'):
                found.append(os.path.join(root, photo))
                print(colorama.Fore.GREEN,
                        f'[*] {photo}', colorama.Style.RESET_ALL)

                if not os.path.exists(os.path.join(root, photo)):
                    non_existent.append(os.path.join(root, photo))
                    continue

                sizes.append(os.path.getsize(os.path.join(root, photo)))
            else:
                pass
    Disk.unmount()


if __name__ == '__main__':
    found, sizes, non_existent = [], [], []
    colorama.init()
    find_photos()
    Positions.local_dir()

    i = 0
    with open('Photos_Found.txt', 'w') as f:
        for photo in found:
            i += 1
            f.write(f'{photo}\n')

    print('Total photos: {:,}'.format(i))
    print('Size of Found Photos: {:,}'.format(sum(sizes)))

    i = 0
    with open('Ex_Photos.txt', 'w') as f:
        for ex_photo in non_existent:
            i += 1
            f.write(f'{ex_photo}\n')

    print(f'Total Non Existent Photos: {i}')
