# Netflix-Logger
A scraper to download High Quality Audio from Netflix.
This vulnerability has already been reported to bugcrowd.com at: https://bugcrowd.com/submissions/59e26094-303f-4c40-ae73-f3dc46270370

**How use it**
1. Click "F12" to open console debugger.
2. Filter for "Logs" only.
3. Go to https://www.netflix.com/browse/genre/34399?so=az
4. Injector will start to log all audio urls a json dicts with an'automatic scroll.

![Screencast-from-13-04-2023-10-42-57](https://user-images.githubusercontent.com/94486728/231745882-4739c2fb-192f-4e15-9cdb-996cac0194f2.gif)
**How to install**
If you use Firefox, install the source as a debug extension.
1. Clone repository.
2. Click on "Load Temporary Add-on".
3. Select repository directory.

![Screenshot from 2023-04-13 13-14-05](https://user-images.githubusercontent.com/94486728/231741939-33f0a409-68c2-4e58-93b1-d73665365774.png)

If you use Google Chrome install the source as a debug extension.
1. Clone repository.
2. Click on "Extensions".
3. Click on "Load unpacked".
4. Select repository directory.

![Screenshot from 2023-04-13 13-16-22](https://user-images.githubusercontent.com/94486728/231742512-d13cccac-19f4-418e-8d13-0be90fe5b754.png)

**How to get movie title from audio**
-Insert movieId to the url:
    https://www.netflix.com/title/{movieId}
- You will be redirect to the movie page
