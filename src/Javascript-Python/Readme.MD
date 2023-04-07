***How to setup***

***Download and install Google-Chrome***
    - wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    - sudo apt install ./google-chrome-stable_current_amd64.deb

***Setup Google Chrome***
    ***Open Google Chrome Browser and create 5 separate profiles, each of them connects an Instagram profile, remember to store caches and cookies***
    ***Once you have prepared the profiles you should be able to switch from one profile to another and enter Instagram without logging in anymore***
    ***For every profiles go to chrome://version to check "Profile Path" name, for example ---> /home/$USER/.config/google-chrome/Profile3***
    ***Copy and create the user_data_dir for five times***
    - sudo cp -r /home/$USER/.config/google-chrome /home/$USER/.config/google-chrome2
    - sudo cp -r /home/$USER/.config/google-chrome /home/$USER/.config/google-chrome3
    - sudo cp -r /home/$USER/.config/google-chrome /home/$USER/.config/google-chrome4
    - sudo cp -r /home/$USER/.config/google-chrome /home/$USER/.config/google-chrome5
    ***Give permissions***
    - sudo chmod 777 -R /home/$USER/.config/google-chrome2 home/$USER/.config/google-chrome3 /home/$USER/.config/google-chrome4 /home/$USER/.config/google-chrome5 

***Edit pyppeteer "launcher.py""***
    - sudo nano usr/lib/python3/dist-packages/pyppeteer/launcher.py
    ***Comment all args except "--enable-automation",should look like this:***
            DEFAULT_ARGS = [
        #    '--disable-background-networking',
        #    '--disable-background-timer-throttling',
        #    '--disable-breakpad',
        #    '--disable-browser-side-navigation',
        #    '--disable-client-side-phishing-detection',
        #    '--disable-default-apps',
        #    '--disable-dev-shm-usage',
        #    '--disable-extensions',
        #    '--disable-features=site-per-process',
        #    '--disable-hang-monitor',
        #    '--disable-popup-blocking',
        #    '--disable-prompt-on-repost',
        #    '--disable-sync',
        #    '--disable-translate',
        #    '--metrics-recording-only',
        #    '--no-first-run',
        #    '--safebrowsing-disable-auto-update',
            '--enable-automation',
        #    '--password-store=basic',
        #    '--use-mock-keychain',
        ]

***Setup sources***
    ***For the logic of the sources you need to have up and running these profiles***
    - /home/$USER/.config/google-chrome/Default
    - /home/$USER/.config/google-chrome/Profile1
    - /home/$USER/.config/google-chrome/Profile2
    - /home/$USER/.config/google-chrome/Profile3
    - /home/$USER/.config/google-chrome/Profile4
    ***Otherwhise you need to edit profiles on "app.py"***
        self.profile_one = "Default"
        self.profile_two = "Profile 1"
        self.profile_three = "Profile 2"
        self.profile_four = "Profile 3"
        self.profile_five = "Profile 4"

***You need to handle different dirs for python venv***