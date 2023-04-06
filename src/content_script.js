injectScripts();

async function injectScripts() 
{
    // await injectScript('lib/pbf.3.0.5.min.js');
    // await injectScript('lib/cryptojs-aes_0.2.0.min.js');
    // await injectScript('protobuf-generated/license_protocol.proto.js');


    // await injectScript('content_key_decryption.js');
    // await injectScript('eme_interception.js');
    await injectScript('lib/cadmium-playercore-6.0039.582.911.js');
    // await injectScript('lib/akiraClient.js.330fa72168f2bc5c9730.js');
}

function injectScript(scriptName) 
{
    return new Promise(function(resolve, reject) 
    {
        var s = document.createElement('script');
        s.src = chrome.extension.getURL(scriptName);
        s.onload = function() {
            this.parentNode.removeChild(this);
            resolve(true);
        };
        (document.head||document.documentElement).appendChild(s);
    });
}
