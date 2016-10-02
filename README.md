# test_picture_location

## Prerequisites

- Python 2.7
- ```exiftool``` available on the path.

## Usage

```
$ ./test_picture_location.py <image_file_path> <latitude> <longitude> <radius>
```

Where...

- ```image_file_path``` -- Path to the file which location you want to test.
- ```latitude``` -- Latitude of the target location in decimal format (e.g. -37.1234567)
- ```longitude``` -- Longitude of the target location in decimal format (e.g. 145.7654321)
- ```radius``` -- The radius from the target location.
If the image file was taken within this radius, the file is considered a match.

If the file matches, it outputs the path of the file to ```stdout```, and the script exits with a ```0``` exit code.

If the file does not match, nothing is output to ```stdout```, and the script exits with a non-zero exit code.

### Example #1

The following command tests if ```IMG_1234.JPG``` was taken within one kilometer of the Eureka Tower in Melbourne Australia.

```
$ ./test_picture_location.py ~/Picture/IMG_1234.JPG -37.821638 144.9645348 1
```

### Example #2

The following command find all the JPEG pictures in the ```Pictures``` folder that were taken within one kilometer of the Eureka Tower in Melbourne Australia.

```
find ~/Pictures -iname '*.jpg' -exec ./test_picture_location.py {} -37.8859748 145.0826936 1 \;
```
