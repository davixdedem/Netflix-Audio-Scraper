# Netflix-Logger
A scraper to download Audio from Netflix

**How to download Audio**
-From this endpoint:
https://ipv4-c002-trn001-wind-isp.1.oca.nflxvideo.net/range/0-4095?o=1&v=139&e=1680339323&t=g24xTqAz17iAubY3FC9_OVvefiq3M8EFCGIkhJgSSjLJlPG4aeMxUUL52oEwkpyWMUWUoea61OXoiKRdCbyX5r3jBJXaLfAszI_h47BNy4dS4KiM1L6wr-4rTsZkkY6B9LSopH9ilOx8ggNH9ub0uplW5TG2lTJDhymPV982uUHGEYqX4mRcZ2i2AypLx6sSdFrWqm_Or9gKyjjMKnFTFaiOkcSdNkehSrVrXZ9ArFV18AWviyMqUw

Delete "/range/0-4095" from request url, you will get endpoint to download clear audio:
https://ipv4-c002-trn001-wind-isp.1.oca.nflxvideo.net?o=1&v=139&e=1680339323&t=g24xTqAz17iAubY3FC9_OVvefiq3M8EFCGIkhJgSSjLJlPG4aeMxUUL52oEwkpyWMUWUoea61OXoiKRdCbyX5r3jBJXaLfAszI_h47BNy4dS4KiM1L6wr-4rTsZkkY6B9LSopH9ilOx8ggNH9ub0uplW5TG2lTJDhymPV982uUHGEYqX4mRcZ2i2AypLx6sSdFrWqm_Or9gKyjjMKnFTFaiOkcSdNkehSrVrXZ9ArFV18AWviyMqUw

-The response data need to contain "ftyp" as start string

**How to download Metadata**
-From this endpoint:
https://www.netflix.com/nq/website/memberapi/v1a975618/metadata?movieid=80104412&imageFormat=jpg&withSize=true&materialize=true&_=1680297852391

-Json response should be like this:
{"version":"2.1","trackIds":{"nextEpisode":200257858,"episodeSelector":200257859},"video":{"title":"Deepwater Horizon - Inferno sull'oceano","synopsis":"Questo film sulla catastrofe del 2010 dell'omonima piattaforma petrolifera include anche le 12 ore che hanno portato a un gigantesco disastro causato dall'uomo.","rating":"13+","artwork":[{"w":1280,"h":720,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABaWUF6K_qxKZzYjLyroRkX8wXH10aP4_yz82CVrUrm2S2jxyQdzkaHoo0OflQCeZrvkNfyvleTRKU1T_2GRCMkFom383c570ikJ0.jpg?r=f23"},{"w":1280,"h":720,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABaWUF6K_qxKZzYjLyroRkX8wXH10aP4_yz82CVrUrm2S2jxyQdzkaHoo0OflQCeZrvkNfyvleTRKU1T_2GRCMkFom383c570ikJ0.jpg?r=f23"}],"boxart":[{"w":426,"h":607,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/WNk1mr9x_Cd_2itp6pUM7-lXMJg/AAAABfWzmtKmTsESmo-1Jc-maqlwn0kgvNaqX0lfQgZYSeqYxJpCEPBEWtQhi-WWXO99a8_Ut8CABRcjiwzdom9eWX_T_D9J3oAXpwkr.jpg?r=cde"},{"w":284,"h":405,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/WNk1mr9x_Cd_2itp6pUM7-lXMJg/AAAABTPxszi0yJFMdqgeLbIHlhxICGA5IXRI1szHhEpzEFtL7GZsGJ8k_NeA8FMoCc81SiLYIbQhGDMANCZl951mMVmZ8fyWrrio7e7l.jpg?r=cde"}],"storyart":[{"w":1280,"h":720,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABSVQlCLhATsgMonqD2Ulmcgio9z003r7KtjB8LDtRcXMR0x_OUY2Qw3X_WF5O967sHUeYPsvesCWlQka2_MugEAAGY-0O4t2J_1w.jpg?r=888"},{"w":1920,"h":1080,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABV0GAauzf9-m7pZJ4URargFWXKwR5tkuaZpkaCMOgaP8xxQWae931c5SMZvtazkZ5X_X6QkDTRaDrjgQ3nyfWfd9AbEWj4Imjuh8.jpg?r=888"}],"type":"movie","unifiedEntityId":"Video:80104412","id":80104412,"userRating":{"matchScore":91,"tooNewForMatchScore":true,"type":"thumb","userRating":0},"skipMarkers":{"credit":{"start":0,"end":0},"recap":{"start":0,"end":0},"content":[]},"start":1667257200000,"end":1698793200000,"year":2016,"requiresAdultVerification":false,"requiresPin":false,"requiresPreReleasePin":false,"creditsOffset":5910,"runtime":6434,"displayRuntime":6434,"autoplayable":true,"bookmark":{"watchedDate":1680297851725,"offset":4},"hd":true,"stills":[{"w":1920,"h":1080,"url":"https://occ-0-2632-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABfmHaj6hi3Rl_lADsvZ9_gc_uQ1rTrA7TH99iZ0-QirTCqhZV85eNcuATmmOCCO7fstVuASRbWREhitPMVUFrzxLG7Z6369z4Dv8TtGkJImaqKLFZclbgQB3TQ.jpg?r=e1a"}],"hiddenEpisodeNumbers":false,"merchedVideoId":null,"cinematch":{"type":"predicted","value":"3.0"},"taglineMessage":{"tagline":"","classification":"REGULAR"},"liveEvent":{"hasLiveEvent":false,"liveEventStartDate":0,"availabilityStartTime":1667257200000,"liveEventEndDate":0}}}


**How to get title**
-Insert movieId to the url:
    https://www.netflix.com/title/{movieId}
- You will be redirect to the movie page