# Mod headers

## Introduction

Now that we have an oauth token we need to be able to add it to selenium either via:
• an [extensions](https://vimmaniac.com/blog/bangal/modify-and-add-custom-headers-in-selenium-chrome-driver) (But I worry if that will work for [Authorization](https://developer.chrome.com/extensions/webRequest))
• A proxy https://github.com/QAutomatron/docker-browsermob-proxy
• or look into running on gitlabs docker network.
