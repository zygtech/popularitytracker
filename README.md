# popularitytracker

[Example Tracking Site](https://zygtech.pl/tracker/)

Python written scripts to monitor popularity of chosen places every hour between 10:00-20:00. Uses:
1. [Populartimes](https://github.com/m-wrzr/populartimes/)
2. [SimpleXLSXGen](https://github.com/shuchkin/simplexlsxgen/)
3. [Chart.js](https://www.chartjs.org/)

For legal concerns please read [Issue #90](https://github.com/m-wrzr/populartimes/issues/90)

Installation:
1. Get a Google Maps API key. [Get a Google Maps API key](https://developers.google.com/places/web-service/get-api-key)
2. `clone` or unpack ZIP on server in example to home folder
3. Browse to folder `populartimes` and install it running `pip install .`
4. Edit both `init.py` and `stat.py` by changing API KEY, and PLACE IDs in lines with `saveid` (any amount). [Find PlaceIDs](https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder)
5. Run `python3 init.py` to initialize script and fill `names` folder with data.
6. Add `stat.py` to CRON by running `crontab -e` and adding in example line 
   `0 10-20 * * 1-6 python3 /home/pi/popularitytracker/stat.py`
7. Copy folder `tracker` to Apache/Nginx WWW folder in example `/var/www/html`
8. Edit `config.php` in this folder with `popularitytracker` path.
9. Browse to `https://yourserver.com/tracker` and monitor any places on the world.

